const { AuditLogEvent, Events } = require('discord.js')
const { legionmid, legionmnotificationsid, rsfid, rsfnotificationsid, kashtanid, kashtannotificationsid, ugolokid, ugoloknotificationsid } = require('../options.js')

module.exports = {
    name: 'guildBanAdd',
    async execute(ban, client) {
        guild = ban.guild.name
        const reason = `Забанен на сервере ${guild} // was banned on ${guild}`

        // Сервера
        const legionm = await client.guilds.fetch(legionmid)
        const rsf = await client.guilds.fetch(rsfid)
        const kashtan = await client.guilds.fetch(kashtanid)
        const ugolok = await client.guilds.fetch(ugolokid)


        // Каналы для уведомлений
        const legionmnotifications = await client.channels.cache.get(legionmnotificationsid)
        const rsfnotifications = await client.channels.cache.get(rsfnotificationsid)
        const kashtannotifications = await client.channels.cache.get(kashtannotificationsid)
        const ugoloknotifications = await client.channels.cache.get(ugoloknotificationsid)

        const fetchedLogs = await ban.guild.fetchAuditLogs({
            limit: 1,
            type: AuditLogEvent.MemberBanAdd,
        })
        const banLog = fetchedLogs.entries.first();
        const { executor, target } = banLog;
        if ((guild == legionm.name)) {
            await rsf.members.ban(ban.user, { reason: reason })
            await rsfnotifications.send(`${ban.user.tag} был послан нахуй из интернета на сервере ${legionm.name}`)
            await kashtan.members.ban(ban.user, { reason: reason })
            await kashtannotifications.send(`${ban.user.tag} был забанен на сервере ${legionm.name}`)
            await ugolok.members.ban(ban.user, { reason: reason })
            await ugoloknotifications.send(`${ban.user.tag} был забанен на сервере ${legionm.name}`)
        } else if (guild == rsf.name) {
            await legionm.members.ban(ban.user, { reason: reason })
            await legionmnotifications.send(`${ban.user.tag} был забанен на сервере ${rsf.name} // ${ban.user.tag} was banned on ${rsf.name}`)
            await kashtan.members.ban(ban.user, { reason: reason })
            await kashtannotifications.send(`${ban.user.tag} был забанен на сервере ${rsf.name}`)
            await ugolok.members.ban(ban.user, { reason: reason })
            await ugoloknotifications.send(`${ban.user.tag} был забанен на сервере ${rsf.name}`)
        } else if (guild == kashtan.name) {
            await legionm.members.ban(ban.user, { reason: reason })
            await legionmnotifications.send(`${ban.user.tag} был забанен на сервере ${kashtan.name} // ${ban.user.tag} was banned on ${kashtan.name}`)
            await rsf.members.ban(ban.user, { reason: reason })
            await rsfnotifications.send(`${ban.user.tag} был послан нахуй из интернета на сервере ${kashtan.name}`)
            await ugolok.members.ban(ban.user, { reason: reason })
            await ugoloknotifications.send(`${ban.user.tag} был забанен на сервере ${kashtan.name}`)
        } else if (guild == ugolok.name) {
            await legionm.members.ban(ban.user, { reason: reason })
            await legionmnotifications.send(`${ban.user.tag} был забанен на сервере ${ugolok.name} // ${ban.user.tag} was banned on ${ugolok.name}`)
            await kashtan.members.ban(ban.user, { reason: reason })
            await kashtannotifications.send(`${ban.user.tag} был забанен на сервере ${ugolok.name}`)
            await rsf.members.ban(ban.user, { reason: reason })
            await rsfnotifications.send(`${ban.user.tag} был послан нахуй из интернета на сервере ${ugolok.name}`)
        }
    }
}