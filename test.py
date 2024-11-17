from llama_cpp import Llama

llm = Llama(model_path="C:\gemma-1.1-7b-it.Q4_K_M.gguf")

def generate_operations(user_input):
    prompt = f"User: {user_input}\nAssistant:"
    response = llm(prompt)
    return response


def main():
    # test 1
    # user_input = "Provide only the Bash code. Do not include any explanation or additional text. Task: Create folders named \"fol\" followed by every letter of the alphabet."
    # print(generate_operations(user_input)["choices"])
    # \n\n```bash\nfor i in {a..z}; do mkdir fol$

    #response = llm("Output only Bash code. Create folders named 'fol' followed by every letter of the alphabet.", max_tokens=100, temperature=0.2)
    #print(response["choices"][0]["text"])
    #for i in {a..z} ; do mkdir "fol$i" ; done

    response = llm("Output only Bash code. Create folders named 'fol' followed by every letter of the alphabet. Inside each folder create 10 txt files numbered the letter a + num from 1 to 20", max_tokens=100, temperature=0.2)
    print(response["choices"][0]["text"])
    # 0.2 temp
    """```bash
    mkdir -p fol{a..z}
    for i in {a..z}; do
        for j in {1..20}; do
            touch fol$i/$(printf %02d $j).txt
        done
    done
    ```""" 
    #incorrect output




    

if __name__ == "__main__":
    main()