from typing_extensions import TypedDict, list
from langgraph.graph.message import add_messages
from typing import Annotated



class State(TypedDict):
    """
    Represents the structure of the state used in graph, including the LLM model and messages.
    This class is used to define the structure of the state dictionary for the graph.
    """
    messages: Annotated[list, add_messages]


