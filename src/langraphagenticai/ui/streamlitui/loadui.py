import streamlit as st
import os

from src.langraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())


        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)

        return self.user_controls



































# class LoadStreamlitUI:
#     def __init__(self):
#         self.config = Config()
#         self.page_title = self.config.get_page_title()
#         self.llm_options = self.config.get_llm_options()
#         self.usecase_options = self.config.get_usecase_options()
#         self.groq_model_options = self.config.get_groq_model_options()

#     def load_ui(self):
#         st.set_page_config(page_title=self.page_title)
#         st.title(self.page_title)

#         # LLM Options
#         selected_llm = st.selectbox("Select LLM Option", self.llm_options)

#         # Use Case Options
#         selected_usecase = st.selectbox("Select Use Case", self.usecase_options)

#         # GROQ Model Options
#         selected_groq_model = st.selectbox("Select GROQ Model", self.groq_model_options)

#         # Display selections
#         st.write(f"Selected LLM: {selected_llm}")
#         st.write(f"Selected Use Case: {selected_usecase}")
#         st.write(f"Selected GROQ Model: {selected_groq_model}")

