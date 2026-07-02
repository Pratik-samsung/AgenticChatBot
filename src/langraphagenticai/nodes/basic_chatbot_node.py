from src.langraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot login implementation
    
    """

    def __init__(self, model):
        self.llm=model

    def process(self, state:State) -> dict:
