
def generate_resolution(ticket, solution, severity):

    if "No matching solution found" in solution:
        return "No resolution could be generated. Please contact human IT support."

    resolution = f"""
AI GENERATED SUPPORT RESPONSE

Ticket:
{ticket}

Severity:
{severity}

Recommended Actions:
{solution}

Please follow the recommended actions and check whether
the issue has been resolved.

If the issue continues, contact the human IT support team.
"""

    return resolution
