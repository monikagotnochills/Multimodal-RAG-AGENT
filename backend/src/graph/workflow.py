''' 
This module which we are building the workflow model defines the DAG  it is directed acyclic graph it orchestrates thwe video compliannce audit video process
it conncts nodes to state graph from langgraph

Start -> index_video_node -> audit_content_node -> END



'''
from langgraph.graph import END, StateGraph
from backend.src.graph.state import VideoAuditState
from backend.src.graph.nodes import (
    index_video_node,
    audit_content_node
)


def create_graph():
    '''
    Constructs and compile the Langgraph workflow
    Return :
    Compiled Graph: runnnable graph objevct for execution 
     '''
    # initialize the graph with state schema
    workflow = StateGraph(VideoAuditState)
    # add the nodes
    workflow.add_node("indexer", index_video_node)
    workflow.add_node("auditor", audit_content_node)
    # define the edges
    workflow.add_edge("indexer", "auditor")
    # once the auditor does his job the whole workflow ends
    workflow.add_edge("auditor", END)
    # COMPILE THE GRAPH
    app = workflow.compile()
    return app


# expose this runnable app
app = create_graph()
