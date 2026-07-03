from src.langraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot login implementation
    
    """

    def __init__(self, model):
        self.llm=model

    # def process(self,state:State)->dict:
    #     """
    #     Processes the input state and generates a chatbot response.

    #     """
    #     return {"messages":self.llm.invoke(state['messages'])}
    
    
    def process(self, state: State) -> dict:
        print("STATE:", state)

        if state is None:
            raise ValueError("State is None")

        if "messages" not in state:
            raise ValueError("messages key missing")

        response = self.llm.invoke(state["messages"])

        return {
            "messages": [response]
        }

    

    
