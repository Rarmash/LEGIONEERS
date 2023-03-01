const { AuditLogEvent, Events } = require('discord.js')
const { legionmid, legionmnotificationsid, rsfid, rsfnotificationsid, kashtanid, kashtannotificationsid, ugolokid, ugoloknotificationsid } = require('../options.js')

module.exports = {
    name: 'guildBanRemove',
    async execute(ban, client) {
        guild = ban.guild.name
        const reason = `Разбанен на сервере ${guild} // was unbanned on ${guild}`

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
        if (guild == legionm.name) {
            try {
                await rsf.members.unban(ban.user, { reason: reason })
                await rsfnotifications.send(`${ban.user.tag} был снят с хуя сервере ${legionm.name}`)
            } catch (err) {}
            try {
                await kashtan.members.unban(ban.user, { reason: reason })
                await kashtannotifications.send(`${ban.user.tag} был разбанен на сервере ${legionm.name}`)
            } catch (err) {}
            try {
                await ugolok.members.unban(ban.user, { reason: reason })
                await ugoloknotifications.send(`${ban.user.tag} был разбанен на сервере ${legionm.name}`)
            } catch (err) {}
        } else if (guild == rsf.name) {
            try {
                await legionm.members.unban(ban.user, { reason: reason })
                await legionmnotifications.send(`${ban.user.tag} был разбанен на сервере ${rsf.name} // ${ban.user.tag} was unbanned on ${rsf.name}`)
            } catch (err) {}
            try {
                await kashtan.members.unban(ban.user, { reason: reason })
                await kashtannotifications.send(`${ban.user.tag} был разбанен на сервере ${rsf.name}`)
            } catch (err) {}
            try {
                await ugolok.members.unban(ban.user, { reason: reason })
                await ugoloknotifications.send(`${ban.user.tag} был разбанен на сервере ${rsf.name}`)
            } catch (err) {}
        } else if (guild == kashtan.name) {
            try {
                await legionm.members.unban(ban.user, { reason: reason })
                await legionmnotifications.send(`${ban.user.tag} был разбанен на сервере ${kashtan.name} // ${ban.user.tag} was unbanned on ${kashtan.name}`)
            } catch (err) {}
            try {
                await rsf.members.unban(ban.user, { reason: reason })
                await rsfnotifications.send(`${ban.user.tag} был снят с хуя сервере ${kashtan.name}`)
            } catch (err) {}
            try {
                await ugolok.members.unban(ban.user, { reason: reason })
                await ugoloknotifications.send(`${ban.user.tag} был разбанен на сервере ${kashtan.name}`)
            } catch (err) {}
        } else if (guild == ugolok.name) {
            try {
                await legionm.members.unban(ban.user, { reason: reason })
                await legionmnotifications.send(`${ban.user.tag} был разбанен на сервере ${ugolok.name} // ${ban.user.tag} was unbanned on ${ugolok.name}`)
            } catch (err) {}
            try {
                await kashtan.members.unban(ban.user, { reason: reason })
                await kashtannotifications.send(`${ban.user.tag} был разбанен на сервере ${ugolok.name}`)
            } catch (err) {}
            try {
                await rsf.members.unban(ban.user, { reason: reason })
                await rsfnotifications.send(`${ban.user.tag} был снят с хуя сервере ${ugolok.name}`)
            } catch (err) {}
        }
    }
}