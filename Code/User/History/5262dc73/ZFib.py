import lodestone
import threading
import time
def get_all_threads_done(list: list):
    done = []
    for thread in list:
       done.append(not thread.is_alive())
    return all(done)
def multitask(action, bots: list, args):
    bot_threads = []
    for i in bots:
        bot_threads.append(threading.Thread(target=action, args=(i, args, )))
    for i in bot_threads:
        i.start()
        time.sleep(0.1)
    while not get_all_threads_done(bot_threads):
        time.sleep(0.5)
    print("All threads finished.")

bots = []
def goto(bot, pos):
    bot.goto(pos[0], pos[1], pos[2])
    exit
print(type(multitask))
for i in range(2*2):
    bots.append(lodestone.createBot('localhost', auth="offline", username=str(i),ls_disable_viewer=True))
#multitask(goto, bots, (0, -60, 0))
multitask(goto, bots, (10, -60, 10))
multitask(goto, bots, (0, -60, 0))