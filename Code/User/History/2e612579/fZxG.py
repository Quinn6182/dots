import lodestone
import useful
bots = []
for i in range(100):
    bots.append(lodestone.createBot(
    "localhost", auth='offline', port=25565, username=f"bot{i}"
    ))

# for i in range(1, 10):
#     for j in range(1, 10):
#         bot.goto(i, -60, j)