import json
from graphchain import workflow
from functions import CustomState

if __name__ == "__main__":
    with open("examples.json") as f:
        examples = json.load(f)

    graph = workflow.compile()

    for ex in examples:
        input_state = CustomState(query=ex["query"])
        result = graph.invoke(input_state)
        print("----")
        print("Query:", ex["query"])
        print("Expected:", ex["expected"])
        print("Prolog Output:", result["prolog_result"])
        print("LLM Explanation:\n", result["explanation"])