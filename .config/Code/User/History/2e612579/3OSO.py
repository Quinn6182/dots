import lodestone
import useful

bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("messagestr")
def chat(this, message, *args):
    print(f"Got message: {useful.get_msg(message)} from {useful.get_sender(message)}")