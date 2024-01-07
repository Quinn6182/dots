module.exports = function log(bot, message, level) {
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
    console.log(`${bot.username} | ${log_prefix}: ${messeage}`)
}