
# app class
# functions for each command
# validate args
# pass to Model class for result


class App:
    def __init__(self, config):
        self.config = config
        

    def print_manual(self, args):
        print("Commands: ")

    def exit(self, args):
        exit(0)

    def change_model_default(self, args):
        pass

    def change_lang_default(self, args):
        pass

    def load_template(self, args):
        pass 

    # for any model prompt
    def run_certain_model(self, args):
        pass

    # for any lang prompt
    def run_certain_lang(self, args):
        pass



    # for default llm and lang
    def run_defaults(self, args):
        pass


