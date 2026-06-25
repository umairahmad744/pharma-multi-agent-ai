def recommendation_agent(state):
    root_causes = state.get("root_causes", [])

    recommendations = []

    for item in root_causes:
        cause = item.get("cause", "Unknown cause")
        batch = item.get("batch", "Unknown batch")
        issue = item.get("issue", "Unknown issue")

        if "Cooling system" in cause:
            action = "Inspect HVAC system and recalibrate temperature sensors"
        elif "raw material" in cause:
            action = "Audit supplier quality and test incoming raw materials"
        elif "machine calibration" in cause:
            action = "Recalibrate production equipment and run validation batch"
        else:
            action = "Perform full QA investigation"

        recommendations.append({
            "batch": batch,
            "issue": issue,
            "cause": cause,
            "action": action
        })

    return {"recommendations": recommendations}