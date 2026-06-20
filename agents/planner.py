from agents import memory


def run():

    items = memory.load_memory()

    if not items:

        return "Nothing to prioritize."

    output = "Priorities:\n\n"

    for i, item in enumerate(items, 1):

        output += f"{i}. {item}\n"

    return output