import openai
import os

OPEN_API_KEY='OPENAI_API_KEY'
#openai.api_key = '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'


def main():
    openai.api_key = os.getenv(f'"{OPEN_API_KEY}"')

    print(openai.api_key)
    
    if open.api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    print("PyChat v0.1")
    query = input('Input: ')

    completion = openai.Completion.create(engine='text-davinci-003',prompt=query,max_tokens=4000)
    output = completion.choices[0].text
    print("Output: {}".format(output))

if __name__ == '__main__': # will execute if the __main__.py is launched
    main() 