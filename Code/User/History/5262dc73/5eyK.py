import lodestone
import threading
def multitask(action: function, bots: list, *args):
    bot_threads = []
    for i in bots:
        bot_threads.append(threading.Thread(target=action, args=(i, args, )))
    for i in bot_threads:
        i.start()
bots = []
def goto(bot, x, y, z):
    bot.goto(x,y,z)
print(type(multitask))
for i in range(2*2):
    bots.append(lodestone.createBot('localhost', auth="offline", username=str(i),ls_disable_viewer=True))
multitask()
    