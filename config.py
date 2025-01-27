import os
import yaml


# improvements
# add numbers for selecting options
# validate config file

class Config:
    def __init__(self, directory, lang, models):
        # set variables
        self.config = {}
        self.directory = directory

        # first time running code, ymal

        #check if config file exists
        if not os.path.exists(directory):
            self.create_config(lang, models)
        else:
            self.load_config()

    
    def create_config(self, LANG, MODELS):
        data = {}

        print("ENTER CONFIG DETAILS (leave blank to disable): ")
        print("Llama model path: ", end="")
        data["llama_path"] = input()

        print("ChatGPT api key: ", end="")
        data["chatgpt_api_key"] = input()

        print("Gemini api key: ", end="")
        data["gemini_api_key"] = input()

        self.change_default("lang", LANG)

        self.change_default("model", MODELS)

        self.config = data

        # write to config file
        self.save_config()



    # add number to choose
    def change_default(self, name, options):
        while True:
            print(f"Change default {name} to: ", end="")
            new = input()
            if new == "": 
                self.config[name] = options[0]
                break
            elif new in options:
                self.config[name] = new
                break
            else:
                print(f"Invalid option. Please choose from: {options}")



    def load_config(self):
        # read config file
        try:
            with open(self.directory, "r") as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            print(f"Failed to read existing config file")
            self.create_config()


    def save_config(self):
        with open(self.directory, "w") as f:
            yaml.dump(self.config, f)
        print(f"Saved new configuration to: {self.directory}.")