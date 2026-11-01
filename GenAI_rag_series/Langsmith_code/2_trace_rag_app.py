from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()



from langsmith import traceable # <- IMPORT a

RAW_TEXT =  open("assets/content.txt","r").read()


# ---------- Indexing (runs once at startup) ----------

# 1. Load: your knowledge base (replace with your own text, files, PDFs, etc.)
@traceable(name="load_documents", run_type="chain")
def load_documents() -> list[Document]:
    return [Document(page_content=RAW_TEXT, metadata={"source": "acme_faq"})]


# 2. Split: break the text into small chunks
@traceable(name="split_documents", run_type="chain")
def split_documents(docs: list[Document], chunk_size: int = 200, chunk_overlap: int = 30) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)


# 3. Embed + store: turn chunks into vectors and keep them in memory
@traceable(name="build_vector_store", run_type="embedding")
def build_vector_store(chunks: list[Document]) -> InMemoryVectorStore:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return InMemoryVectorStore.from_documents(chunks, embeddings)


# Parent run that groups the whole indexing process into one trace
@traceable(name="setup_index", run_type="chain", tags=["indexing"])
def setup_index() -> InMemoryVectorStore:
    docs = load_documents()
    chunks = split_documents(docs)
    return build_vector_store(chunks)


vector_store = setup_index()


# ---------- Querying (runs for every question) ----------

# 4. Retrieve: find the most relevant chunks for a question
#    run_type="retriever" + this output format makes LangSmith show the docs nicely
@traceable(name="retrieve_context", run_type="retriever")
def retrieve(question: str, k: int = 3) -> list[dict]:
    docs = vector_store.similarity_search(question, k=k)
    return [
        {"page_content": d.page_content, "type": "Document", "metadata": d.metadata}
        for d in docs
    ]


@traceable(name="format_docs", run_type="parser")
def format_docs(docs: list[dict]) -> str:
    return "\n\n".join(d["page_content"] for d in docs)


# 5. Prompt: tell the LLM to answer ONLY from the retrieved context
prompt = ChatPromptTemplate.from_template(
    """Answer the question using only the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question: {question}
"""
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()
answer_chain = prompt | model | parser


# 6. Generate: LangChain's own runs (prompt, LLM, parser) nest under this automatically
@traceable(name="generate_answer", run_type="chain")
def generate_answer(question: str, context: str) -> str:
    return answer_chain.invoke({"context": context, "question": question})


# Parent run: one trace per question in LangSmith
@traceable(name="rag_pipeline", run_type="chain", tags=["simple-rag"], metadata={"version": "v1"})
def rag_pipeline(question: str) -> str:
    docs = retrieve(question)
    context = format_docs(docs)
    return generate_answer(question, context)


# 7. Run it
if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or 'exit'): ").strip()
        if question.lower() == "exit":
            break
        print("Answer:", rag_pipeline(question))