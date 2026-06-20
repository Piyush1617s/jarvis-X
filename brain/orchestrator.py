from agents import memory
from agents import planner
from tools import apps
from tools import apps
def route(query):

    query = query.lower()
    
    if query.startswith("remember"):

        text = query.replace("remember", "", 1)

        return memory.remember(text.strip())
    if query.startswith("open"):

        app = query.replace("open", "", 1)

        return apps.open_app(app.strip())
    if query == "show memory":

        return memory.show()

    if query == "show priorities":

        return planner.run()

    return "I don't know how to do that yet."