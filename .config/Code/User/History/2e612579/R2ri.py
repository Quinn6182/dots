import lodestone
import useful

bot = lodestone.createBot(
    "localhost", auth='offline', port=25565, username="bot"
)
for i in range(1, 100):
    for j in range(1, 100):
        bot.goto(i, -60, j)