import os
import yaml
from config import Config
from app import App


# main class
# handles config and command function map
# handles user input and inital command processing
# 


# const var
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__)) + "/config.yaml"
SYSTEM = os.name
MODELS = ["llama", "chatgpt", "gemini"]
LANG = ["python", "bash"]


class Main:
    def __init__(self):
        # get config
        self.config = Config(CONFIG_DIR, LANG, MODELS)

        # create app
        app = App(self.config)

        # specify commands
        self.commands = {
            'man': app.print_manual,
            'manual': app.print_manual,
            'help': app.print_manual,
            'exit': app.exit,
            'model': app.change_model_default,
            'lang': app.change_lang_default,
            'template': app.load_template
        }

        # add model commands
        for model in MODELS:
            self.commands[model] = self.run_certain_model
        
        # add lang commands
        for lang in LANG:
            self.commands[lang] = self.run_certain_lang


        # execute main loop
        self.main()


    # handles very first user input
    # args: list of words
    def processPrompt(self, args):
        # man, template, exit/CTRL+C, help, model, lang, (default)
        
        # check if prompt exists in commands
        prompt = args[0]
        if prompt in self.commands:
            # pass all args including prompt
            self.commands[prompt](args)
        else:
            # run default llm and lang
            self.run_defaults(args)


            
    def main():
        # handle > and line input