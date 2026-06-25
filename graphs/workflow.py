from typing import TypedDict

from langgraph.graph import StateGraph

from agents.router_agent import router_agent
from agents.rag_agent import rag_agent
from agents.anomaly_agent import anomaly_agent
from agents.root_cause_agent import root_cause_agent
from agents.recommendation_agent import recommendation_agent
from agents.report_agent import report_agent


class AgentState(TypedDict, total=False):

    query: str

    route: str

    response: str

    anomalies: list

    root_causes: list

    recommendations: list

    report: str


builder = StateGraph(AgentState)


builder.add_node(
    "router",
    router_agent
)

builder.add_node(
    "rag_agent",
    rag_agent
)

builder.add_node(
    "anomaly_agent",
    anomaly_agent
)

builder.add_node(
    "root_cause_agent",
    root_cause_agent
)

builder.add_node(
    "recommendation_agent",
    recommendation_agent
)

builder.add_node(
    "report_agent",
    report_agent
)


def route_decision(state):

    return state["route"]


builder.set_entry_point(
    "router"
)


builder.add_conditional_edges(

    "router",

    route_decision,

    {

        "rag_agent": "rag_agent",

        "anomaly_agent": "anomaly_agent"

    }

)


builder.add_edge(

    "anomaly_agent",

    "root_cause_agent"

)

builder.add_edge(

    "root_cause_agent",

    "recommendation_agent"

)

builder.add_edge(

    "recommendation_agent",

    "report_agent"

)


builder.set_finish_point(

    "rag_agent"

)

builder.set_finish_point(

    "report_agent"

)


graph = builder.compile()