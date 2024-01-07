import lodestone
def get_sender(msg: str):
    return msg.split('>')[0].split('<')[1]
bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("messagestr")
def chat(this, message, *args):
    print(f"Got message: {message}")