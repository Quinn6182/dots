const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
const logger = require("randomstuff/logger");
let bots = [];
for (let i = 0; i < 100; i++) {
    bots.push(mineflayer.createBot({
        username: `bot${i}`,
        auth: "offline",
        host: "localhost",
        port: 25565,
    }))
}
bots.forEach(bot => {
    bot.loadPlugin(pathfinder);
    logger.log(bot, "loaded plugin pathfinder", 1);
});