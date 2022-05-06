import json
from pypresence import *
import requests
import time
import datetime
import random
import string
from pynotifier import Notification
from os import system
import discord
from colorama import Fore, init
from discord.ext import commands, tasks

system("title " + "SCREAMZ SELFBOT [github.com/screamz2k]")
banner1 = (Fore.BLUE + """
\t\t\t\t.|'''|                                              
\t\t\t\t||                                                  
\t\t\t\t`|'''|, .|'', '||''| .|''|,  '''|.  '||),,(|,  '''/
 \t\t\t\t.   || ||     ||    ||..|| .|''||   || || ||   //
 \t\t\t\t|...|' `|..' .||.   `|...  `|..||. .||    ||. /...""")
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
with open('config.json') as f:
    file = json.load(f)
    token = file["token"]
    prefix = file["prefix"]
    spam_msg = file["spam_msg"]
init()

# config
color = 1752220
log = []
avatar = "https://avatars.githubusercontent.com/u/78593516?v=4"

# Global vars
stop = True
nuker = False


def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def main():
    print(banner1)
    print(Fore.GREEN + "\t\t\t\t\t\t   Loading...")


RPC = Presence(923915111322746901)
RPC.connect()

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

cur_time = int(time.time())
RPC.update(
    large_image="screamz",
    large_text="SCREAMZ SELFBOT BETA",
    details="Feeling like a King.",
    start=cur_time,
    buttons=[{"label": "GET IT YOURSELF", "url": "https://github.com/screamz2k/SCREAMZ-SELFBOT"}])

"""@tasks.loop(minutes=1)
async def up_time():
    with open("./stuff/infos.txt", "r") as f:
      up = int(f.read())
      up += 1
    with open("./stuff/infos.txt", "w") as f:
        f.write(up)
up_time.start()"""
@bot.event
async def on_ready():
    Notification(
        title='SCREAMZ SELFBOT',
        description=f'Logged in as: {bot.user}',
        duration=5,
        icon_path="./stuff/icon.ico",
        urgency='normal').send()
    system("cls ")
    print(banner1)
    print()
    print(Fore.RED + "\t\t\t\t\t  Started Selfbot as: " + str(bot.user))
    print(Fore.CYAN + "\t\t\t\t\t\tgithub.com/screamz2k")
    print(Fore.GREEN + f"\t\t\t\t\t\t Start with {prefix}help")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="SCREAMZ SELFBOT",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Fun", value=f"{prefix}fun", inline=True)
    embed.add_field(name="Utility", value=f"{prefix}utility", inline=True)
    embed.add_field(name="Admin", value=f"{prefix}admin", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# admin
@bot.command()
async def admin(ctx):
    embed = discord.Embed(title="Admin Commands",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Ban", value=f"{prefix}ban [user] [reason]", inline=True)
    embed.add_field(name="Kick", value=f"{prefix}kick [user] [reason]", inline=True)
    embed.add_field(name="Create Text Channel", value=f"{prefix}create_text_channel [name]",
                    inline=False)
    embed.add_field(name="Create Voice Channel", value=f"{prefix}create_voice_channel [name]",
                    inline=False)
    embed.add_field(name="Create Role", value=f"{prefix}create_role [name]", inline=True)
    embed.add_field(name="Give Role", value=f"{prefix}give_role [user] [role]", inline=True)
    embed.add_field(name="Change Nick", value=f"{prefix}nick [user] [name]", inline=True)
    embed.add_field(name="Delete a chosen amount of messages", value=f"{prefix}delete [amount]", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# ban
@bot.command()
async def ban(ctx, user: discord.Member = "", *, reason=None):
    if user == ctx.message.author:
        embed = discord.Embed(title="You cant ban urself dumbo!", colour=color)
        await ctx.send(embed=embed)
        return
    if user == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}ban @test smells bad", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.ban(user=user, reason=reason)
        embed = discord.Embed(title=f"Created {user} successfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# kick
@bot.command()
async def kick(ctx, user: discord.Member, *, reason=None):
    if user == ctx.message.author:
        embed = discord.Embed(title="You cant kick urself dumbo!", colour=color)
        await ctx.send(embed=embed)
        pass
    if user == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}kick @test smells bad", colour=color)
        await ctx.send(embed=embed)
        return
    else:
        try:
            await ctx.guild.kick(user=user, reason=reason)
            embed = discord.Embed(title=f"Kicked {user} successfully", color=color)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
            await ctx.send(embed=embed)


# Create Text Channel
@bot.command()
async def create_text_channel(ctx, name=""):
    if name == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}create_text_channel lounge", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.create_text_channel(name=name)
        embed = discord.Embed(title=f"Created {name} successfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Create Voice Channel
@bot.command()
async def create_voice_channel(ctx, name=""):
    if name == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}create_voice_channel lounge", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.create_voice_channel(name=name)
        embed = discord.Embed(title=f"Created {name} successfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Create role
@bot.command()
async def create_role(ctx, name=""):
    if name == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}create_role king", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.create_role(name=name)
        embed = discord.Embed(title=f"Created {name} successfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Give role
@bot.command()
async def give_role(ctx, user: discord.Member = "", role=""):
    if user == "" or role == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}give_role @screamz admin", colour=color)
        await ctx.send(embed=embed)
        return
    given_role = discord.utils.get(ctx.guild.roles, name=role)
    if given_role is None:
        discord.utils.get(ctx.guild.roles, name=role)
        embed = discord.Embed(title="Role doesnt exist", color=color)
        await ctx.send(embed=embed)
        return
    try:
        await user.add_roles(given_role)
        embed = discord.Embed(title=f"Gave {user} the role {role}", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Change nickname
@bot.command()
async def nick(ctx, user: discord.Member = None, *, name=""):
    if name == "" or user is None:
        embed = discord.Embed(title=f"Use command like this: {prefix}nick @screamz king", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await user.edit(nick=name)
        embed = discord.Embed(title=f"Changed name of {user} to {name}", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Delete
@bot.command()
async def delete(ctx, amount: int = 0):
    if amount == 0:
        embed = discord.Embed(title=f"Use command like this: {prefix}delete 50", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.channel.purge(limit=amount)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="Operation successfully!", description=f"Deleted {amount} successfully", color=color)
    await ctx.send(embed=embed)


# Utility
@bot.command()
async def utility(ctx):
    embed = discord.Embed(title="Utility",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Webhookspammer", value=f"{prefix}webspam [webhook] [count] [message]", inline=True)
    embed.add_field(name="Nuke:bomb:", value=f"{prefix}test (to hide the command)", inline=True)
    embed.add_field(name="Not Working Nitro Snipe", value=f"{prefix}snipe", inline=True)
    embed.add_field(name="Change activity", value=f"{prefix}activity [state]", inline=True)
    embed.add_field(name="Get userinfo", value=f"{prefix}userinfo ")
    embed.add_field(name="Create a random identity", value=f"{prefix}identity")
    embed.add_field(name="Send random Nitro Codes to a webhook", value=f"{prefix}gen [webhook] [amount]", inline=True)
    embed.add_field(name="Get the Geolocation of an IP", value=f"{prefix}geo [ip]")
    embed.add_field(name="General Bot Info", value=f"{prefix}info")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)
# bot info
@bot.command()
async def info(ctx):
    with open("./stuff/infos.txt") as f:
        up = f.read()
    embed = discord.Embed(title="Infos", colour=color)
    embed.add_field(name="Ping", value=bot.latency)
    embed.add_field(name="Use time", value=up)
    embed.add_field(name="Author", value="https://github.com/screamz2k")
    embed.set_thumbnail(url=avatar)
    await ctx.send(embed=embed)
# ip infos
@bot.command()
async def geo(ctx, ip=""):
    if ip == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}geo 1.1.1.1", colour=color)
        await ctx.send(embed=embed)
        return
    infos = requests.get(f"https://freegeoip.app/json/{ip}")
    embed = discord.Embed(title="IP Geolocation", colour=color)
    embed.add_field(name="Ip:", value=ip, inline=False)
    embed.add_field(name="Country", value=infos.json()["country_name"] + " " + infos.json()["country_code"], inline=False)
    embed.add_field(name="Region", value=infos.json()["region_name"], inline=False)
    embed.add_field(name="City", value=infos.json()["city"], inline=False)
    embed.add_field(name="Zip Code", value=infos.json()["zip_code"], inline=False)
    latitude = infos.json()["latitude"]
    longitude = infos.json()["longitude"]
    await ctx.send(embed=embed)
    await ctx.send("https://www.google.de/maps/place/" + str(latitude) + "," + str(longitude))

# create identity
@bot.command()
async def identity(ctx):
    data = requests.get("https://randomuser.me/api/")
    embed = discord.Embed(title="New Identity", colour=color)
    embed.add_field(name="Name:",
                    value=data.json()["results"][0]["name"]["title"] + " " + data.json()["results"][0]["name"][
                        "first"] + " " + data.json()["results"][0]["name"]["last"], inline=False)
    embed.add_field(name="Gender:", value=data.json()["results"][0]["gender"], inline=False)
    embed.add_field(name="Age:", value=data.json()["results"][0]["dob"]["age"], inline=False)
    embed.add_field(name="**User Details:**", value="ㅤ", inline=False)
    embed.add_field(name="Username", value=data.json()["results"][0]["login"]["username"], inline=False)
    embed.add_field(name="Email:", value=data.json()["results"][0]["email"], inline=False)
    embed.add_field(name="Password", value=data.json()["results"][0]["login"]["password"], inline=False)
    embed.add_field(name="**Location:**", value="ㅤ", inline=False)
    embed.add_field(name="Country", value=data.json()["results"][0]["location"]["country"], inline=False)
    embed.add_field(name="State & City",
                    value=data.json()["results"][0]["location"]["state"] + " " + data.json()["results"][0]["location"][
                        "city"], inline=False)
    embed.add_field(name="Postcode", value=data.json()["results"][0]["location"]["postcode"], inline=False)
    embed.add_field(name="Street", value=data.json()["results"][0]["location"]["street"]["name"] + " " + str(
        data.json()["results"][0]["location"]["street"]["number"]), inline=False)
    embed.set_image(url=data.json()["results"][0]["picture"]["large"])
    await ctx.send(embed=embed)


# userinfo
@bot.command()
async def userinfo(ctx):
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=bot.user,
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Full Username", value=bot.user, inline=False)
    embed.add_field(name="User ID", value=bot.user.id, inline=False)
    embed.add_field(name="Created at", value=bot.user.created_at.strftime(date_format), inline=False)
    friend_count = 0
    for friend in bot.user.friends:
        friend_count += 1
    embed.add_field(name="Number of Friends", value=friend_count, inline=False)
    blocked_count = 0
    for block in bot.user.blocked:
        blocked_count += 1
    embed.add_field(name="Number of Blocked", value=blocked_count, inline=False)
    if bot.user.premium:
        embed.add_field(name="Nitro", value=":white_check_mark:", inline=False)
    else:
        embed.add_field(name="Nitro", value=":x:", inline=False)
    embed.set_thumbnail(url=bot.user.avatar_url)
    await ctx.message.channel.send(embed=embed)


# WEBHOOK NITRO
@bot.command()
async def gen(ctx, webhook="", amount=0):
    await ctx.message.delete()
    if webhook == "" or amount == 0:
        embed = discord.Embed(title=f"Use command like this: {prefix}gen https://discord.com/api/webhooks 20",
                              colour=color)
        await ctx.send(embed=embed)
        return
    orig_embed = discord.Embed(description="Webhook Spammer", color=color)
    orig_embed.add_field(name="Messages sent:", value=f"{0}")
    info = await ctx.send(embed=orig_embed)
    success = True
    counter = 0

    def sent():
        global success
        success = True
        res = requests.post(webhook, data=data)
        new_embed = discord.Embed(description="Nitro Gen", color=color)
        new_embed.add_field(name="Codes sent:", value=f"{counter}")
        try:
            time.sleep(res.json()["retry_after"] / 1000)
        except:
            success = False
        return new_embed

    for i in range(amount):
        counter += 1
        code_gen = (random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16))
        code = ""
        for char in code_gen:
            code += char
        start = "https://discord.gift/" + code + "\n"

        data = {
            "content": start
        }
        embed = sent()
        await info.edit(embed=embed)
    last_embed = discord.Embed(description="Nitro Gen", color=color)
    last_embed.add_field(name="Finished", value=f"Sent {amount} codes")
    await info.edit(embed=last_embed)


# change activity
@bot.command()
async def activity(ctx, wanted):
    wanted = wanted.lower()
    if wanted == "idle" or wanted == wanted == "dnd" or wanted == "active" or wanted == "offline":
        pass
    else:
        pass


# WEBHOOK
@bot.command()
async def webspam(ctx, webhook="", count: int = 0, *, message):
    await ctx.message.delete()
    if webhook == "" or count == 0:
        embed = discord.Embed(title=f"Use command like this: {prefix}webspam https://discord.com/api/webhooks 20 msg",
                              colour=color)
        await ctx.send(embed=embed)
        return
    orig_embed = discord.Embed(description="Webhook Spammer", color=color)
    orig_embed.add_field(name="Messages sent:", value=f"{0}")
    info = await ctx.send(embed=orig_embed)
    data = {
        "content": message
    }
    success = True
    counter = 0

    def sent():
        global success
        success = True
        res = requests.post(webhook, data=data)
        new_embed = discord.Embed(description="Webhook Spammer", color=color)
        new_embed.add_field(name="Messages sent:", value=f"{counter}")
        try:
            time.sleep(res.json()["retry_after"] / 1000)
        except:
            success = False
        return new_embed

    for i in range(count):
        embed = sent()
        await info.edit(embed=embed)
        if success:
            counter += 1
    last_embed = discord.Embed(description="Webhook Spammer", color=color)
    last_embed.add_field(name="Finished", value=f"Sent {counter} messages")
    await info.edit(embed=last_embed)  #


# NUKE


blank = "\t\t\t\t\t"
blank1 = "\t\t\t\t    "


# Activate Nuke
@bot.command()
async def test(ctx):
    global nuker
    if not nuker:
        await ctx.message.delete()
        print("\n")
        print(Fore.GREEN + blank + "     Activated Nuke mode hehe")
        print(Fore.CYAN + blank + "\t    Commands:")
        print(Fore.MAGENTA + blank + "----------------------------------")
        print(blank + f"|nuke / spam / role_spam /clear  |")
        print(blank + "|ping_spam / mass_kick / mass_ban|")
        print(blank + "|stop                            |")
        print(blank + "----------------------------------")
        print(blank + "\t      Log:")
        print(Fore.BLUE + "\t\t\t\t" + "    -------------------------------------------")
        nuker = True
    else:
        await ctx.message.delete()


# Nuke:)
@bot.command()
async def nuke(ctx):
    global stop
    if nuker:
        print(Fore.BLUE + blank1 + f"[{update_time()}] Nuke attack started hehe")
        await ctx.message.delete()
        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except:
                pass
        for emoji in ctx.message.guild.emojis:
            try:
                await emoji.delete()
            except:
                pass
        print(Fore.BLUE + blank1 + f"[{update_time()}] Deleted all emojis!")
        print(Fore.BLUE + blank1 + f"[{update_time()}] Deleted all roles!")
        for member in ctx.message.guild.members:
            try:
                await member.edit(nick="nuked lmao")
            except:
                pass
        await ctx.message.guild.edit(name="nuked by 1takeluca on tt")
        for channel in ctx.message.guild.voice_channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        for channel in ctx.message.guild.text_channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        print(Fore.BLUE + blank1 + f"[{update_time()}] Deleted all channels")
        print(Fore.BLUE + blank1 + f"[{update_time()}] Creating channels")
        while True and stop:
            await ctx.message.guild.create_text_channel("nuked by github.com/screamz2k")
            await ctx.message.guild.create_voice_channel("discord.gg/toolstown")
        else:
            stop = True
    else:
        await ctx.message.delete()
        print(Fore.RED + blank + f"You need to type {prefix}test first")


# Delete all channels
@bot.command()
async def clear(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        for channel in ctx.message.guild.channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        ch = await ctx.message.guild.create_text_channel("finished")
        await ch.send("Cleared successfully")
        print(Fore.BLUE + blank1 + f"[{update_time()}] Cleared successfully")


# Spam every channel
@bot.command()
async def spam(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + blank1 + f"[{update_time()}] Started spamming!")
        for channel in ctx.message.guild.text_channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("got nuked lmao @everyone")
                await channel.send(spam_msg)
        print(Fore.BLUE + blank1 + f"[{update_time()}] Restarting Spam!")
        for channel in ctx.message.guild.text_channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("got nuked lmao @everyone")
                await channel.send(spam_msg)
        print(Fore.BLUE + blank1 + f"[{update_time()}] Stopped spamming!")


# Spam pings
@bot.command()
async def ping_spam(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + blank1 + f"[{update_time()}] Started pinging!")
        for channel in ctx.message.guild.channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("@everyone @here")
        for channel in ctx.message.guild.channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("@everyone @here")
        print(Fore.BLUE + blank1 + f"[{update_time()}] Stopped pinging!")


# Spam roles
@bot.command()
async def role_spam(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + blank1 + f"[{update_time()}] Started mass creating roles")
        while True and stop:
            await ctx.message.guild.create_role(name="screamz2k", colour=discord.Colour.blue())
        else:
            stop = True


# Ban all members
@bot.command()
async def mass_ban(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + blank1 + f"[{update_time()}] Started mass banning!")
        count = 0
        for user in ctx.message.guild.members:
            if user == ctx.message.author:
                continue
            try:
                await user.ban(reason="Got nuked lmao", delete_message_days=7)
                count += 1
            except PermissionError:
                continue
            if not stop:
                stop = True
                break
        print(Fore.BLUE + blank1 + f"[{update_time()}] Successfully banned {count} members")


# Kick all members
@bot.command()
async def mass_kick(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + blank1 + f"[{update_time()}] Started mass kicking!")
        count = 0
        for user in ctx.message.guild.members:
            if user == ctx.message.author:
                continue
            try:
                await user.kick(reason="Got nuked lmao")
                count += 1
            except:
                pass
            if not stop:
                stop = True
                break
        print(Fore.BLUE + blank1 + f"[{update_time()}] Successfully kicked {count} members")


@bot.command()
async def stop(ctx):
    global stop
    await ctx.message.delete()
    stop = False
    print(Fore.BLUE + blank1 + f"[{update_time()}] Stopped current operation")


# Fun
@bot.command()
async def fun(ctx):
    embed = discord.Embed(title="Fun",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Flip a Coin :coin:", value=f"{prefix}flip [head/tails]", inline=True)
    embed.add_field(name="Roll a Dice :1234:", value=f"{prefix}dice", inline=True)
    embed.add_field(name="Anime", value=f"{prefix}anime", inline=True)
    embed.add_field(name="Cat :cat:", value=f"{prefix}cat", inline=True)
    embed.add_field(name="Dog :dog:", value=f"{prefix}dog", inline=True)
    embed.add_field(name="Duck :duck:", value=f"{prefix}duck", inline=True)
    embed.add_field(name="Fox :fox:", value=f"{prefix}fox", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# flip a coin
@bot.command()
async def flip(ctx, choice=""):
    if choice.lower() == "head" or choice.lower() == "tails":
        embed = discord.Embed(description=f"You choose {choice}", color=color)
        sign = await ctx.send(embed=embed)
        flipped = random.choice(["Head", "Tails"])
        load = ""
        for i in range(3):
            time.sleep(1)
            load += "."
            processing = discord.Embed(description=f"You choose {choice}", color=color)
            processing.add_field(name="Flipping", value=load)
            await sign.edit(embed=processing)
        if choice == "head" and flipped == "Head":
            end = discord.Embed(description="You win! :grin:", color=color)
            end.add_field(name="Coin landed on Head", value=f"You choose {choice}")
        elif choice == "tails" and flipped == "Tails":
            end = discord.Embed(description="You win! :grin:", color=color)
            end.add_field(name="Coin landed on Tails", value=f"You choose {choice}")
        else:
            end = discord.Embed(description="You loose!:sob:", color=color)
            end.add_field(name=f"Coin landed on {flipped}", value=f"You choose {choice}")
        await sign.edit(embed=end)
        return
    else:
        embed = discord.Embed(title=f"Use command like this: {prefix}flip head/tails", colour=color)
        await ctx.send(embed=embed)


# roll a dice
@bot.command()
async def dice(ctx):
    roll = random.randint(0, 5)
    numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    embed = discord.Embed(description=f"Rolling the dice:1234:", color=color)
    sign = await ctx.send(embed=embed)
    load = ""
    for i in range(3):
        time.sleep(1)
        load += "."
        processing = discord.Embed(description=f"Rolling the dice:1234:", color=color)
        processing.add_field(name="Rolling", value=load)
        await sign.edit(embed=processing)
    end = discord.Embed(description=f"Dice rolled on: {numbers[roll]}", color=color)
    await sign.edit(embed=end)


# anime
@bot.command()
async def anime(ctx):
    embed = discord.Embed(title="Anime",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="sfw", value=f"{prefix}sfw [category]", inline=False)
    embed.add_field(name="sfw category", value=f"""
waifu, neko ,shinobu
megumin, bully, cuddle
cry, hug, awoo
kiss, lick, pat
smug, bonk, yeet
blush, smile, wave
highfive, handhold, nom
bite, glomp, slap
kill, kick, happy
wink, poke, dance
cringe""", inline=False)
    embed.add_field(name="nsfw", value=f"{prefix}nsfw [category]", inline=False)
    embed.add_field(name="nsfw category", value="""waifu
neko, trap, blowjob""", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


@bot.command()
async def sfw(ctx, category, amount=0):
    if amount == 0:
        picture = requests.get("https://api.waifu.pics/sfw/" + category)
        embed = discord.Embed(description="Here you go!", colour=color)
        embed.set_image(url=picture.json()["url"])
        await ctx.send(embed=embed)
    elif amount <= 5:
        for i in range(amount):
            picture = requests.get("https://api.waifu.pics/sfw/" + category)
            embed = discord.Embed(colour=color)
            embed.set_image(url=picture.json()["url"])
            embed.set_footer(text=f"Requested by {ctx.message.author.name}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Max amount is 5!", colour=discord.Colour.red())
        embed.set_footer(text=f"Requested by {ctx.message.author.name}")
        await ctx.send(embed=embed)


@bot.command()
async def nsfw(ctx, category, amount=0):
    if amount == 0:
        picture = requests.get("https://api.waifu.pics/nsfw/" + category)
        embed = discord.Embed(description="Here you go!", colour=color)
        embed.set_image(url=picture.json()["url"])
        await ctx.send(embed=embed)
    elif amount <= 5:
        for i in range(amount):
            picture = requests.get("https://api.waifu.pics/nsfw/" + category)
            embed = discord.Embed(colour=color)
            embed.set_image(url=picture.json()["url"])
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Max amount is 5!", colour=discord.Colour.red())
        await ctx.send(embed=embed)


# cat
@bot.command()
async def cat(ctx):
    picture = requests.get("https://thatcopy.pw/catapi/rest/")
    embed = discord.Embed(description=":cat:", colour=color)
    embed.set_image(url=picture.json()["url"])
    await ctx.send(embed=embed)


# duck
@bot.command()
async def duck(ctx):
    await ctx.message.delete()
    picture = requests.get("https://random-d.uk/api/random")
    embed = discord.Embed(description=":duck:", colour=color)
    embed.set_image(url=picture.json()["url"])
    await ctx.send(embed=embed)


# dog
@bot.command()
async def dog(ctx):
    picture = requests.get("https://random.dog/woof.json")
    embed = discord.Embed(description=":dog:", colour=color)
    embed.set_image(url=picture.json()["url"])
    await ctx.send(embed=embed)


# fox
@bot.command()
async def fox(ctx):
    picture = requests.get("https://randomfox.ca/floof/")
    embed = discord.Embed(description=":fox:", colour=color)
    embed.set_image(url=picture.json()["image"])
    await ctx.send(embed=embed)
@bot.command()
async def rickroll(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173")


"""@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Error",
            description=f"**Command does not exist.**",
            color=discord.Colour.red())
        await ctx.send(embed=embed)
"""
if token == "paste bot token here" or token == "":
    print(Fore.RED + blank1 + "You need to paste your token into the config file!!!")
    input()
    exit()

main()
try:
    bot.run(token, bot=False)
except:
    print(Fore.RED + "\t\t\t\t\t     Token is invalid!")
    input()
