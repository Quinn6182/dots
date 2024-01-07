import lodestone
def get_sender(msg: str):
    return msg.split('>')[0].split('<')[1].split(' ')[1]
def get_msg(msg: str):
    return msg.split('>')[1]
bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("messagestr")
def chat(this, message, *args):
    print(f"Got message: {get_msg(message)} from {get_sender(message)}")