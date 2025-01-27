import os
import yaml

# const var
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__)) + "/config.yaml"
SYSTEM = os.name
MODELS = ["llama", "chatgpt", "gemini"]
LANG = ["python", "bash"]


class APP:
    def __init__(self):
        # set variables
        self.config = {}

        # first time running code, ymal

        #check if config file exists
        if not os.path.exists(CONFIG_DIR):
            self.create_config()
        else:
            self.load_config()
        
        

    def create_config(self):
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
            with open(CONFIG_DIR, "r") as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            print(f"Failed to read existing config file")
            self.create_config()


    def save_config(self):
        with open(CONFIG_DIR, "w") as f:
            yaml.dump(self.config, f)
        print("Saved new configuration to: {CONFIG_DIR}.")

    
    def print_help(self):
        print("Commands: ")


    def load_template(self, name, print):
        if print == True:
            print("Choose a template: ")
            name = input()
        
        # attempt to load template
        


    # process first user input
    # promts: list of words
    def processPrompt(self, prompts):
        # man, template, exit/CTRL+C, help, model, lang, (default)
        match(prompts[0]):
            case "man":
                self.print_help()
            case "help":
                self.print_help()

            case "exit":
                exit(0)
            
            case "model":
                # >model chatgpt   -will change the default model to python
                if len(prompts) == 2 and prompts[1] in MODELS:
                    self.config["model"] = prompts[1]
                # change default
                self.change_default("model", MODELS)

            case "lang":
                # >lang python   -will change the default language to python
                if len(prompts) == 2 and prompts[1] in LANG:
                    self.config["lang"] = prompts[1]
                # change default
                self.change_default("lang", LANG)

            case "template":
                # choose a template
                if len(prompts) == 2:
                    # load existing template
                    self.load_template(prompts[1], False)
                
                self.load_template("", True)

        if prompts[0] in MODELS:
            # run with model
        
        if prompts[0] in LANG:
            # run with lang

        # run with default model and lang


            
                
    def main():

        

        

    