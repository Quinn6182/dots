import lodestone
import useful

bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("whisper")
def chat(this, message, *args):
    print(f"Got message: '{useful.get_msg(message)}' from '{useful.get_sender(message)}'")
    message_split = useful.get_msg(message).split(' ')
    print(message_split)
    if message_split[1] == "goto":
        bot.goto(int(message_split[2]), int(message_split[3]), int(message_split[4]))