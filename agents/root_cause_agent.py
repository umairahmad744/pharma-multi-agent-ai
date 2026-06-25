def root_cause_agent(state):
    anomalies = state.get("anomalies", [])

    root_causes = []

    for item in anomalies:
        batch = item.get("batch", "Unknown batch")
        issue = item.get("issue", "Unknown issue")

        # simple deterministic logic (you can later replace with LLM)
        if issue == "High temperature":
            cause = "Cooling system malfunction or improper storage conditions"
        elif issue == "Low yield":
            cause = "Possible raw material inconsistency or machine calibration issue"
        else:
            cause = "Unknown cause - requires investigation"

        root_causes.append({
            "batch": batch,
            "issue": issue,
            "cause": cause
        })

    return {"root_causes": root_causes}