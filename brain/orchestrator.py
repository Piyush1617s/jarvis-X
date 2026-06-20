from agents import memory
from agents import planner
from tools import apps

def route(query):

    query = query.lower()
    if query == "open vscode":

        return apps.open_vscode()
    if query.startswith("remember"):

        text = query.replace("remember", "", 1)

        return memory.remember(text.strip())

    if query == "show memory":

        return memory.show()

    if query == "show priorities":

        return planner.run()

    return "I don't know how to do that yet."