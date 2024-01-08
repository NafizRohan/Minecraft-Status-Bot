from mcstatus import JavaServer
import config
import discord
from discord import app_commands as ac
from discord import Colour as c
import time
#Timestamp
time_ = time.localtime()
timestamp = f"[{time_.tm_hour}:{time_.tm_min}:{time_.tm_sec}]  "

#Client Setup
client = discord.Client(intents = discord.Intents.all())
bot = ac.CommandTree(client = client)

##_________________________________##
##__________CILENT EVENT__________##
@client.event
async def on_ready():
    print(f"{timestamp}{client.user.name} is activated.")
    while True:
        time__ = time.localtime()
        channel =  await client.fetch_channel(config.channel_id)
        message = await channel.fetch_message(config.message_id)
        try:
            server = JavaServer.lookup(config.server_address)
        except Exception as e:
            print("Wrong IP:PORT")
        else:
            try:
                status = server.status()
            except ConnectionRefusedError:
                Embed = discord.Embed(title=f"SMP Status", color= c.red())
                Embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1099343453609005167/1193104151316541480/g.png?ex=65ab7fd4&is=65990ad4&hm=5afd5a1a340795a75e88d06697b10cd3a4ea42b56689a581214fc14e66c53530&")
                Embed.add_field(name= "> Status", value= "```\n🔴 Offline!\n```")
                Embed.add_field(name= "> Players", value=f"```\n👥 0/0\n```")
                Embed.add_field(name= "> Ping", value=f"```\n📶 0 ms\n```")
                Embed.add_field(name= "> IP Address", value=f"```\n🌐 {config.server_address}\n```", inline= False)
                Embed.set_footer(icon_url= "https://cdn.discordapp.com/attachments/1099343453609005167/1193104151316541480/g.png?ex=65ab7fd4&is=65990ad4&hm=5afd5a1a340795a75e88d06697b10cd3a4ea42b56689a581214fc14e66c53530&",
                                text=f"SMP Status ・ Updated every minute ・Today at {time__.tm_hour}:{(time__.tm_min) + 1}")
                channel =  await client.fetch_channel(1192134661225316406)
                await message.edit(content=" ",embed= Embed)
            else:
                Embed = discord.Embed(title=f"{status.raw['version']['name']} {status.raw['description']['text']}", color= c.green())
                Embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1099343453609005167/1193104151316541480/g.png?ex=65ab7fd4&is=65990ad4&hm=5afd5a1a340795a75e88d06697b10cd3a4ea42b56689a581214fc14e66c53530&")
                Embed.add_field(name= "> Status", value= "```\n🟢 Online!\n```")
                Embed.add_field(name= "> Players", value=f"```\n👥 {status.players.online}/{status.players.max}\n```")
                Embed.add_field(name= "> Ping", value=f"```\n📶 {int(status.latency)} ms\n```")
                Embed.add_field(name= "> IP Address", value=f"```\n🌐 {config.server_address}\n```", inline= False)
                Embed.set_footer(icon_url= "https://cdn.discordapp.com/attachments/1099343453609005167/1193104151316541480/g.png?ex=65ab7fd4&is=65990ad4&hm=5afd5a1a340795a75e88d06697b10cd3a4ea42b56689a581214fc14e66c53530&",
                                text=f"SMP Status ・ Updated every minute ・Today at {time__.tm_hour}:{(time__.tm_min) + 1}")
                await message.edit(content=" ",embed= Embed)
                
        time.sleep(60)


client.run(config.Token)