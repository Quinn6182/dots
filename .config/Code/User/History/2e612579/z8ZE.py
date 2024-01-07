import lodestone
import useful
def openai_request(send: str):
    return client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": send,
        }
    ],
    model="gpt-3.5-turbo",)
bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("messagestr")
def chat(this, message, *args):
    print(f"Got message: '{useful.get_msg(message)}' from '{useful.get_sender(message)}'")
    if useful.get_sender(message) != 'bot':
        bot.chat(useful.openai_request(useful.get_msg(message)).choices[0].message.content)