from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# whole code is generated via ai for observability 
# directly go to langsmith dashboard 

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatOpenAI(model="gpt-4.1-mini")
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)