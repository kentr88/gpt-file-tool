from llama_cpp import Llama
from yaspin import yaspin

try:
    import readline
except ImportError:
    import pyreadline3 as readline


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

    while True:
        print("\nOptions: e: execute, q: quit, arrow keys: edit code")
        print("Bash code:")
        print("__________________________")
        bash_code = "\n".join(filtered_lines)
        print(bash_code)

        print("Enter option (e/q) or edit the code using the arrow keys:")
        edited_code = input("> ")

        if edited_code.lower() == 'q':
            print("Exiting...")
            break
        elif edited_code.lower() == 'e':
            print("Executing code...")
            break
        else:
            # Update the Bash code with the edited input
            filtered_lines = edited_code.split("\n")
            print("Code updated. You can edit again or choose an option.")





    

if __name__ == "__main__":
    main()