const { ActivityType } = require('discord.js')

module.exports = {
    name: 'ready',
    async execute(client) {
        console.log('------')
        console.log('Бот запущен!')
        console.log(`Вошли как ${client.user.username}`)
        console.log(`ID бота: ${client.user.id}`)
        const Guilds = client.guilds.cache.map(guild => guild.name)
        console.log(Guilds)
        client.user.setPresence({ activities: [{ name: 'резню' }], status: 'onlune' });
        //client.user.setPresence({ activities: [{ name: 'резню (ИДУТ ТЕХ. РАБОТЫ)' }], status: 'dnd' });
    }
}