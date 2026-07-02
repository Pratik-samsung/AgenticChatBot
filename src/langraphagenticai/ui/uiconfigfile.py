#able tio read all the configurations in uiconfigfile.ini

from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()            #this type of object will be able to read configurations from the ini file
        self.config.read(config_file)


    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")





        