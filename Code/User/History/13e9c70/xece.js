const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
const bot_logger = require("./randomstuff/bot-logger");
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
    bot_logger.log(bot, "loaded plugin pathfinder", 1);
});
