from javascript import require
from time import sleep
mineflayer = require('mineflayer')
bots = []
for i in range(4):
    bots.append(mineflayer.createBot({
        "host": 'localhost',
        "port": 25565,
        "username": str(i)
    }))
