import lodestone
bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("messagestr")
def chat(this, message, messagePosition, jsonMSG, *args):
    print(jsonMSG)