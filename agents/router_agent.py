def router_agent(state):

    query = state["query"].lower()

    if any(word in query for word in [
        "analyze",
        "batch",
        "production",
        "temperature",
        "yield",
        "pressure"
    ]):

        return {
            "route": "anomaly_agent"
        }

    return {
        "route": "rag_agent"
    }