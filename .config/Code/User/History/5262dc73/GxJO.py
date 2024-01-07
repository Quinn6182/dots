import lodestone
import threading
def multitask(action):
    pass
bots = []
type(multitask)
for i in range(2*2):
    bots.append(lodestone.createBot('localhost', auth="offline", username=str(i),ls_disable_viewer=True))
for i in bots:
    i.goto(0, -60, 0)
    