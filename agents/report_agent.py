def report_agent(state):
    anomalies = state.get("anomalies", [])
    root_causes = state.get("root_causes", [])
    recommendations = state.get("recommendations", [])

    report = {
        "summary": {
            "total_batches_analyzed": len(anomalies),
            "issues_found": len(root_causes)
        },
        "details": []
    }

    for i in range(len(root_causes)):
        rc = root_causes[i] if i < len(root_causes) else {}
        rec = recommendations[i] if i < len(recommendations) else {}

        report["details"].append({
            "batch": rc.get("batch", "Unknown"),
            "issue": rc.get("issue", "Unknown"),
            "cause": rc.get("cause", "Unknown"),
            "action": rec.get("action", "No action defined")
        })

    return {"report": report}