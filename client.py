from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

command = ""




completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named neha who speaks hindi as well as english. she is from India and is a coder. You analyze chat history and respond like neha"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)