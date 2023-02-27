const synchronizeSlashCommands = require('../modules/sync_commands.js')
const { ActivityType } = require('discord.js')

module.exports = {
    name: 'ready',
    async execute(client) {
        console.log('------')
        console.log('Бот запущен!')
        console.log(`Вошли как ${client.user.username}`)
        console.log(`ID бота: ${client.user.id}`)
        client.user.setPresence({ activities: [{ name: 'резню (ИДУТ ТЕХ. РАБОТЫ)' }], status: 'dnd' });

        /*await synchronizeSlashCommands(client,
            client.commands.map((c) => c.data), {
                debug: true,
            }
        )
        */
    }

}