import openai
import re
# SmashyX#0017
openai.api_key = "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"

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
    print(f"Bot: {format_message(response)}")
