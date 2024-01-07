import lodestone
bots = []
for i in range(5*5):
    bots.append(lodestone.createBot('localhost', auth="offline", username=str(i),ls_disable_viewer=True))