import openai
import re
# SmashyX#0017
openai.api_key = "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" # replace with your own

def chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
 
    message = completions.choices[0].text
    return message.strip()
 
def format_message(message):
    message = message.replace("\n", " ")
    message = re.sub(" +", " ", message)
    return message

while True:
    prompt = input("You: ")
    response = chat(prompt)
    print(f"DaVinci: {format_message(response)}")