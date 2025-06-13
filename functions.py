import subprocess
from typing import TypedDict
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0)

class CustomState(TypedDict):
    query: str
    prolog_result: str
    explanation: str

def run_prolog(state: CustomState) -> CustomState:
    query = state["query"]
    try:
        result = subprocess.run(
            ["swipl", "-q", "-s", "rules.pl", "-g", f"verify({query}), halt."],
            capture_output=True, text=True
        )
        output = result.stdout.strip()
        return {
            "query": query,
            "prolog_result": output if output else "error",
            "explanation": ""
        }
    except Exception as e:
        return {
            "query": query,
            "prolog_result": "error",
            "explanation": f"Prolog execution failed: {str(e)}"
        }

def explain_output(state: CustomState) -> CustomState:
    explanation = llm.invoke(f"""The result of the Prolog query '{state['query']}' was '{state['prolog_result']}'.
Explain what this means in natural language.""").content
    return {
        **state,
        "explanation": explanation
    }
