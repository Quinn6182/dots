from openai import OpenAI
client = OpenAI(api_key='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')
def get_sender(msg: str):
    return msg.split('>')[0].split('<')[1].replace(' ', '')
def get_msg(msg: str):
    return msg.split('>')[1]
def openai_request(send: str):
    return client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": send,
        }
    ],
    model="gpt-3.5-turbo",).choices[0].message