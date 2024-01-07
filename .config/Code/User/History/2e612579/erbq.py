import lodestone
bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
@bot.on("messagestr")
def chat(a, b, *c):
    print(a,b)