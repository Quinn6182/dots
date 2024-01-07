import lodestone
import threading
def multitask(action: function, bots: list, *args):
    bot_threads = []
    for i in bots:
        bot_threads.append(threading.Thread(target=action, args=(i, args, )))
bots = []
print(type(multitask))
for i in range(2*2):
    bots.append(lodestone.createBot('localhost', auth="offline", username=str(i),ls_disable_viewer=True))
for i in bots:
    i.goto(0, -60, 0)
    