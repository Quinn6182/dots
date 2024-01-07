import lodestone
import useful
import threading
bots = []
def make_ten(start):
    for i in range(10):
        bots.append(lodestone.createBot(
    "localhost", auth='offline', port=25565, username=f"bot{i+start}", ls_disable_viewer=True
    ))
for i in range(100):
    bots.append(lodestone.createBot(
    "localhost", auth='offline', port=25565, username=f"bot{i}", ls_disable_viewer=True
    ))

# for i in range(1, 10):
#     for j in range(1, 10):
#         bot.goto(i, -60, j)