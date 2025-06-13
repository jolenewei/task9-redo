from langgraph.graph import StateGraph, END
from functions import CustomState, run_prolog, explain_output

workflow = StateGraph(CustomState)
workflow.add_node("prolog_query", run_prolog)
workflow.add_node("explain", explain_output)
workflow.set_entry_point("prolog_query")
workflow.add_edge("prolog_query", "explain")
workflow.add_edge("explain", END)
