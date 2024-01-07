import lodestone
import useful
import threading
bots = []
def make_ten(start):
    for i in range(10):
        bots.append(lodestone.createBot(
    "localhost", auth='offline', port=25565, username=f"bot{i+start}", ls_disable_viewer=True
    ))
bot_threads = []
for i in range(10):
    bot_threads.append(threading.Thread(target=make_ten, args=(i*10)))
for i in bot_threads:
    i.start()
# for i in range(1, 10):
#     for j in range(1, 10):
#         bot.goto(i, -60, j)