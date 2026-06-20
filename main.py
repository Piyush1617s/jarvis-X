from brain.orchestrator import route


print("\nJARVIS ONLINE\n")

while True:

    query = input("> ")

    if query.lower() == "exit":

        break

    response = route(query)

    print("\nJARVIS:")

    print(response)

    print()