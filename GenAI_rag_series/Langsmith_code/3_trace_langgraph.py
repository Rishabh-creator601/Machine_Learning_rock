from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

import os 

load_dotenv()   # loads LANGSMITH_* variables, so tracing works




os.environ["LANGCHAIN_PROJECT"] = "trace_langgraph"
# State
class LoanState(TypedDict):
    name: str
    credit_score: int
    result: str


# Nodes

def check_score(state: LoanState):
    print(f"Checking credit score for {state['name']}: {state['credit_score']}")
    return {}


def approve(state: LoanState):
    return {"result": "Loan Approved ✅"}


def reject(state: LoanState):
    return {"result": "Loan Rejected ❌"}


# Condition
def decide(state: LoanState):
    if state["credit_score"] >= 700:
        return "approve"
    return "reject"


# Graph
graph = StateGraph(LoanState)

graph.add_node("check_score", check_score)
graph.add_node("approve", approve)
graph.add_node("reject", reject)

graph.add_edge(START, "check_score")
graph.add_conditional_edges("check_score", decide)
graph.add_edge("approve", END)
graph.add_edge("reject", END)

app = graph.compile()


# Run
print(app.invoke({"name": "Rahul", "credit_score": 750}))
print(app.invoke({"name": "Amit", "credit_score": 600}))