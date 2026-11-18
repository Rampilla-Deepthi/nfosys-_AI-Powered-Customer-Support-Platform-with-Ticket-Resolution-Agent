
def validate_resolution(solution):

    if "No matching solution found" in solution:
        print("\nNo solution available.")
        print("Ticket escalated to human support team.")
        return "Escalated"

    print("\nDid the suggested solution resolve your issue?")
    response = input("Enter yes or no: ").lower().strip()

    if response == "yes":
        print("\nTicket successfully resolved and closed!")
        return "Resolved"

    else:
        print("\nTicket escalated to human support team!")
        return "Escalated"
