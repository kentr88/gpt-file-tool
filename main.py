from llama_cpp import Llama
import itertools
import threading
import time
from yaspin import yaspin


llm = Llama(model_path="C:\\gemma-1.1-7b-it.Q4_K_M.gguf", verbose=False)


def main():
    print("Enter task: ", end="")
    user_input = input()

    with yaspin(text="Processing...", color="cyan") as spinner:
        response = llm(f"Output only Bash code. {user_input}", max_tokens=100, temperature=0.3)
        spinner.ok("✅")


    lines = response["choices"][0]["text"].split("\n")
    # filter lines
    
    # only get lines within ```bash
    start = False
    filtered_lines = []
    for line in lines:
        if "```bash" in line:
            start = True
            continue
        if "```" in line:
            start = False
            break
        if start:
            filtered_lines.append(line)



    # remove empty lines
    filtered_lines = list(filter(lambda x: x.strip() != "", filtered_lines))
    

    if len(filtered_lines) == 0:
        print("No Bash code found.")
        return

    print("options: e:execute, q:quit, r:retry, l:larger model, arrow key: edit")
    print("Bash code:")
    print("__________________________")
    print("\n".join(filtered_lines))
    print("enter option: ", end="")
    option = input()





    

if __name__ == "__main__":
    main()