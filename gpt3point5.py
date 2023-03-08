import openai
import re
import array

openai.api_key = "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"

def add_assistant_context(assistant_context):
   return{"role": "assistant", "content": assistant_context}

def add_user_context(user_context):
   return {"role": "assistant", "content": user_context}

global messages

def chat(prompt):
  completions = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
     add_user_context(prompt)
    ]
    
  )
  messages.append(add_assistant_context(response))
  
  message = completions['choices'][0]['message']['content']
  return message.strip()

def format_message(newmessage):
    newmessage = newmessage.replace("\n", " ")
    newmessage = re.sub(" +", " ", newmessage)
    return newmessage



while True:
   prompt = input('You: ')
   response = chat(prompt)
   print(f"ChatGPT: {format_message(response)}")