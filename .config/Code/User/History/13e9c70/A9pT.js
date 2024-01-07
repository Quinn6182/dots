const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
function log(bot, message, level) {
    let log_prefix;
    switch (level) {
        case 2:
            log_prefix = "[WARNING]";
            break;
        case 3:
            log_prefix = "[ERROR]";
            break
        default:
            log_prefix = "[INFO]";
            break;
    }
    console.log(`${bot.username} | ${log_prefix}: ${message}`)
}
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
    log(bot, "loaded plugin pathfinder", 1);
});
