''' 
This module defines the DAG (Directed Acyclic Graph) for the video compliance audit process.
It connects nodes to the StateGraph from langgraph.

Start -> index_video_node -> audit_content_node -> END
'''
# FIX 1: Added START to the imports
from langgraph.graph import END, StateGraph, START 
from backend.src.graph.state import VideoAuditState
from backend.src.graph.nodes import (
    index_video_node,
    audit_content_node
)

def create_graph():
    '''
    Constructs and compiles the Langgraph workflow.
    Returns:
        Compiled Graph: runnable graph object for execution 
    '''
    # Initialize the graph with state schema
    workflow = StateGraph(VideoAuditState)
    
    # Add the nodes
    workflow.add_node("indexer", index_video_node)
    workflow.add_node("auditor", audit_content_node)
    
    # Define the edges
    # FIX 2: Added the entry point so the graph knows where to begin
    workflow.add_edge(START, "indexer") 
    
    workflow.add_edge("indexer", "auditor")
    
    # Once the auditor does its job, the whole workflow ends
    workflow.add_edge("auditor", END)
    
    # COMPILE THE GRAPH
    app = workflow.compile()
    return app

# Expose this runnable app
app = create_graph()