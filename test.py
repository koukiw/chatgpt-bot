import openai
openai.api_key = "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"
## ChatGPTに投げる質問を記載する
content = "明日の天気は？"
response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": content},
    ],
)

# import os
# from openai import OpenAI

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key="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"
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )
print(response.choices[0].message.content)