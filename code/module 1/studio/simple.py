import random 
from typing_extensions import TypedDict
from typing import Literal
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    graph_state: str

# Conditional edge
def decide_mood(state) -> Literal["node_2", "node_3"]:
    return "node_2" if random.random() < 0.5 else "node_3"

# Nodes
def node_1(state):
    print("---Node 1---")
    return {"graph_state" : state['graph_state'] +" I am"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state" : state['graph_state'] +" happy!"}

def node_3(state):
    print("---Node 3---")
    return {"graph_state" : state['graph_state'] +" sad!"}

# Build graph
builder = StateGraph(State)

builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Compile graph
graph = builder.compile()