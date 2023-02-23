import discord
from discord.ext import commands
from options import *
from datetime import timedelta

class Bans(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        reason = f"Забанен на сервере {guild} // was banned on {guild}"
        ##################################################
        legionm = await self.Bot.fetch_guild(legionmid)
        legionmnotifications = self.Bot.get_channel(legionmnotificationsid)
        
        rsf = await self.Bot.fetch_guild(rsfid)
        rsfnotifications = self.Bot.get_channel(rsfnotificationsid)
        
        kashtan = await self.Bot.fetch_guild(kashtanid)
        kashtannotifications = self.Bot.get_channel(kashtannotificationsid)
        
        ugolok = await self.Bot.fetch_guild(ugolokid)
        ugoloknotifications = self.Bot.get_channel(ugoloknotificationsid)
        ##################
        if guild == legionm:
            await rsf.ban(member, reason=reason)
            await rsfnotifications.send(f'{member} был послан нахуй из интернета на сервере {guild}')
            await kashtan.ban(member, reason=reason)
            await kashtannotifications.send(f'{member} был забанен на сервере {guild}')
            await ugolok.ban(member, reason=reason)
            await ugoloknotifications.send(f'{member} был забанен на сервере {guild}')
        #####################
        elif guild == rsf:
            await legionm.ban(member, reason=reason)
            await legionmnotifications.send(f'{member} был забанен на сервере {guild} // {member} was banned on {guild}')
            await kashtan.ban(member, reason=reason)
            await kashtannotifications.send(f'{member} был забанен на сервере {guild}')
            await ugolok.ban(member, reason=reason)
            await ugoloknotifications.send(f'{member} был забанен на сервере {guild}')
        ############################
        elif guild == kashtan:
            await legionm.ban(member, reason=reason)
            await legionmnotifications.send(f'{member} был забанен на сервере {guild} // {member} was banned on {guild}')
            await rsf.ban(member, reason=reason)
            await rsfnotifications.send(f'{member} был послан нахуй из интернета на сервере {guild}')
            await ugolok.ban(member, reason=reason)
            await ugoloknotifications.send(f'{member} был забанен на сервере {guild}')
        #############################
        elif guild == ugolok:
            await legionm.ban(member, reason=reason)
            await legionmnotifications.send(f'{member} был забанен на сервере {guild} // {member} was banned on {guild}')
            await kashtan.ban(member, reason=reason)
            await kashtannotifications.send(f'{member} был забанен на сервере {guild}')
            await rsf.ban(member, reason=reason)
            await rsfnotifications.send(f'{member} был послан нахуй из интернета на сервере {guild}')
            
    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        reason = f"Разбанен на сервере {guild} // was unbanned on {guild}"
        ##################################################
        legionm = await self.Bot.fetch_guild(legionmid)
        legionmnotifications = self.Bot.get_channel(legionmnotificationsid)
        
        rsf = await self.Bot.fetch_guild(rsfid)
        rsfnotifications = self.Bot.get_channel(rsfnotificationsid)
        
        kashtan = await self.Bot.fetch_guild(kashtanid)
        kashtannotifications = self.Bot.get_channel(kashtannotificationsid)
        
        ugolok = await self.Bot.fetch_guild(ugolokid)
        ugoloknotifications = self.Bot.get_channel(ugoloknotificationsid)
        ##################
        if guild == legionm:
            await rsf.unban(member, reason=reason)
            await rsfnotifications.send(f'{member} был снят с хуя сервере {guild}')
            await kashtan.unban(member, reason=reason)
            await kashtannotifications.send(f'{member} был разбанен на сервере {guild}')
            await ugolok.unban(member, reason=reason)
            await ugoloknotifications.send(f'{member} был разбанен на сервере {guild}')
        #####################
        elif guild == rsf:
            await legionm.unban(member, reason=reason)
            await legionmnotifications.send(f'{member} был разбанен на сервере {guild} // {member} was unbanned on {guild}')
            await kashtan.unban(member, reason=reason)
            await kashtannotifications.send(f'{member} был разбанен на сервере {guild}')
            await ugolok.unban(member, reason=reason)
            await ugoloknotifications.send(f'{member} был разбанен на сервере {guild}')
        ############################
        elif guild == kashtan:
            await legionm.unban(member, reason=reason)
            await legionmnotifications.send(f'{member} был разбанен на сервере {guild} // {member} was unbanned on {guild}')
            await rsf.unban(member, reason=reason)
            await rsfnotifications.send(f'{member} был снят с хуя на сервере {guild}')
            await ugolok.unban(member, reason=reason)
            await ugoloknotifications.send(f'{member} был разбанен на сервере {guild}')
        #############################
        elif guild == ugolok:
            await legionm.unban(member, reason=reason)
            await legionmnotifications.send(f'{member} был разбанен на сервере {guild} // {member} was unbanned on {guild}')
            await kashtan.unban(member, reason=reason)
            await kashtannotifications.send(f'{member} был разбанен на сервере {guild}')
            await rsf.unban(member, reason=reason)
            await rsfnotifications.send(f'{member} был снят с хуя на сервере {guild}')
    
    @commands.Cog.listener()
    async def on_member_update(self, ctx, after):
        ##################################################
        legionm = await self.Bot.fetch_guild(legionmid)
        legionmnotifications = self.Bot.get_channel(legionmnotificationsid)
        
        rsf = await self.Bot.fetch_guild(rsfid)
        rsfnotifications = self.Bot.get_channel(rsfnotificationsid)
        
        kashtan = await self.Bot.fetch_guild(kashtanid)
        kashtannotifications = self.Bot.get_channel(kashtannotificationsid)
        
        ugolok = await self.Bot.fetch_guild(ugolokid)
        ugoloknotifications = self.Bot.get_channel(ugoloknotificationsid)
        ##########################
        try:
            legionmuser = await legionm.fetch_member(ctx.id)
        except: pass
        try:
            rsfuser = await rsf.fetch_member(ctx.id)
        except: pass
        try:
            kashtanuser = await kashtan.fetch_member(ctx.id)
        except: pass
        try:
            ugolokuser = await ugolok.fetch_member(ctx.id)
        except: pass
        
        guild = ctx.guild
        
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.member_update).flatten()
        logs = logs[0]
        
        if after.timed_out and (logs.user.id != self.Bot.user.id):
            duration = timedelta(days = 27)
            reason = f"Замьючен на сервере {guild} // got timeout on {guild}"
            ##################
            if guild == legionm:
                try:
                    await rsfuser.timeout_for(duration,  reason=reason)
                    await rsfnotifications.send(f'{after} был послан нахуй в таймаут на сервере {guild}')
                except: pass
                try:
                    await kashtanuser.timeout_for(duration, reason=reason)
                    await kashtannotifications.send(f'{after} был замьючен на сервере {guild}')
                except: pass
                try:
                    await ugolokuser.timeout_for(duration, reason=reason)
                    await ugoloknotifications.send(f'{after} был замьючен на сервере {guild}')
                except: pass
            #####################
            elif guild == rsf:
                try:
                    await legionmuser.timeout_for(duration, reason=reason)
                    await legionmnotifications.send(f'{after} был замьючен на сервере {guild} // {after} got timeout on {guild}')
                except: pass
                try:
                    await kashtanuser.timeout_for(duration, reason=reason)
                    await kashtannotifications.send(f'{after} был замьючен на сервере {guild}')
                except: pass
                try:
                    await ugolokuser.timeout_for(duration, reason=reason)
                    await ugoloknotifications.send(f'{after} был замьючен на сервере {guild}')
                except: pass
            ############################
            elif guild == kashtan:
                try:
                    await legionmuser.timeout_for(duration, reason=reason)
                    await legionmnotifications.send(f'{after} был замьючен на сервере {guild} // {after} got timeout on {guild}')
                except: pass
                try:
                    await rsfuser.timeout_for(duration, reason=reason)
                    await rsfnotifications.send(f'{after} был послан нахуй в таймаут на сервере {guild}')
                except: pass
                try:
                    await ugolokuser.timeout_for(duration, reason=reason)
                    await ugoloknotifications.send(f'{after} был замьючен на сервере {guild}')
                except: pass
            #############################
            elif guild == ugolok:
                try:
                    await legionmuser.timeout_for(duration, reason=reason)
                    await legionmnotifications.send(f'{after} был замьючен на сервере {guild} // {after} got timeout on {guild}')
                except: pass
                try:
                    await kashtanuser.timeout_for(duration, reason=reason)
                    await kashtannotifications.send(f'{after} был замьючен на сервере {guild}')
                except: pass
                try:
                    await rsfuser.timeout_for(duration, reason=reason)
                    await rsfnotifications.send(f'{after} был послан нахуй в таймаут на сервере {guild}')
                except: pass
        elif not(after.timed_out) and (logs.user.id != self.Bot.user.id):
            duration = None
            reason = f"Размьючен на сервере {guild} // got unmuted on {guild}"
            ##################
            if guild == legionm:
                try:
                    await rsfuser.timeout(duration,  reason=reason)
                    await rsfnotifications.send(f'{after} был снят с хуя в таймауте на сервере {guild}')
                except: pass
                try:
                    await kashtanuser.timeout(duration, reason=reason)
                    await kashtannotifications.send(f'{after} был размьючен на сервере {guild}')
                except: pass
                try:
                    await ugolokuser.timeout(duration, reason=reason)
                    await ugoloknotifications.send(f'{after} был размьючен на сервере {guild}')
                except: pass
            #####################
            elif guild == rsf:
                try:
                    await legionmuser.timeout(duration, reason=reason)
                    await legionmnotifications.send(f'{after} был размьючен на сервере {guild} // {after} got unmuted on {guild}')
                except: pass
                try:
                    await kashtanuser.timeout(duration, reason=reason)
                    await kashtannotifications.send(f'{after} был размьючен на сервере {guild}')
                except: pass
                try:
                    await ugolokuser.timeout(duration, reason=reason)
                    await ugoloknotifications.send(f'{after} был размьючен на сервере {guild}')
                except: pass
            ############################
            elif guild == kashtan:
                try:
                    await legionmuser.timeout(duration, reason=reason)
                    await legionmnotifications.send(f'{after} был размьючен на сервере {guild} // {after} got unmuted on {guild}')
                except: pass
                try:
                    await rsfuser.timeout(duration, reason=reason)
                    await rsfnotifications.send(f'{after} был снят с хуя в таймауте на сервере {guild}')
                except: pass
                try:
                    await ugolokuser.timeout(duration, reason=reason)
                    await ugoloknotifications.send(f'{after} был размьючен на сервере {guild}')
                except: pass
            #############################
            elif guild == ugolok:
                try:
                    await legionmuser.timeout(duration, reason=reason)
                    await legionmnotifications.send(f'{after} был размьючен на сервере {guild} // {after} got unmuted on {guild}')
                except: pass
                try:
                    await kashtanuser.timeout(duration, reason=reason)
                    await kashtannotifications.send(f'{after} был размьючен на сервере {guild}')
                except: pass
                try:
                    await rsfuser.timeout(duration, reason=reason)
                    await rsfnotifications.send(f'{after} был снят с хуя в таймауте на сервере {guild}')
                except: pass
            
def setup(bot):
    bot.add_cog(Bans(bot))