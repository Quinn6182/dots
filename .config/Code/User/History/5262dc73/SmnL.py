from javascript import require
mineflayer = require('mineflayer')
bots = []
for i in range(100):
    bots.append(mineflayer.createBot({
        "host": 'localhost',
        "port": 25565,
        "username": str(i)
    }))