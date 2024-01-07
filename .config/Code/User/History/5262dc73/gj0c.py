import lodestone
import threading
def multitask(action, bots: list, args):
    bot_threads = []
    for i in bots:
        bot_threads.append(threading.Thread(target=action, args=(i, args, )))
    for i in bot_threads:
        i.start()
bots = []
def goto(bot, pos):
    bot.goto(pos[0], pos[1], pos[2])
print(type(multitask))
for i in range(2*2):
    bots.append(lodestone.createBot('localhost', auth="offline", username=str(i),ls_disable_viewer=True))
multitask(goto, bots, (0, -60, 0))
    