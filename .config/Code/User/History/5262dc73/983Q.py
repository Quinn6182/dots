from javascript import require
from time import sleep
mineflayer = require('mineflayer')
bots = []
for i in range(20):
    bots.append(mineflayer.createBot({
        "host": 'localhost',
        "port": 25565,
        "username": str(i)
    }))
    sleep(1)