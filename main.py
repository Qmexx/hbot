#i shit the bed in the fourth grade
import discord, random, datetime, requests, math
from discord.ext import commands, tasks

TOKEN = open('token.txt', 'r').readlines()[0].strip()
TOOLS = open('tools.txt', 'r', encoding='utf-8').readlines()
VOWELS = open('name_vowels.txt', 'r').readlines()
NON_VOWELS = open('name_non_vowels.txt', 'r').readlines()
intents = discord.Intents().all()
prefixes = 'ö.', 'Ö.'
client = commands.Bot(command_prefix=prefixes, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('oh no'))
    print('BOT ONLINE')

@client.command()
async def jj(ctx):
    print('Jedes Jahr an deinem Geburtstag gehen deine Eltern in den Zoo und bewerfen den Storch mit Steinen') 
    await ctx.send('Jedes Jahr an deinem Geburtstag gehen deine Eltern in den Zoo und bewerfen den Storch mit Steinen')

@client.command()
async def DEsentence(ctx):
    print('Ich lebe in deinen Mauern von Son nenuntergang bis zur Dämmerung, aber tagsüber bin ich in deinem Schornstein')
    await ctx.send('Ich lebe in deinen Mauern von Son nenuntergang bis zur Dämmerung, aber tagsüber bin ich in deinem Schornstein')

@client.command()
async def RUsentence(ctx):
    print('Я не терплю, когда мои друзья мочатся в моем супе')
    await ctx.send('Я не терплю, когда мои друзья мочатся в моем супе')

@client.command()
async def JPtest(ctx):
    print('ハンバーガーチーズバーガーホットドッグハンバーガーチーズバーガーホットドッグ')
    await ctx.send ('ハンバーガーチーズバーガーホットドッグハンバーガーチーズバーガーホットドッグ')

@client.command()
async def ping(ctx):
    print('ping')
    await ctx.send(f'ping: {round(client.latency * 1000)}ms')

@client.command()
async def hhh(ctx):
    exhale = 'h' * random.randint(3,30)
    print(exhale)
    await ctx.send(exhale)

@client.command()
async def help(ctx):
    await ctx.send('ping, hhh, game, bonk, bagel, shake/handshake/respectfulhandshake, five/highfive, bite, deny, salami')  

@client.command()
async def nothing(ctx):
    await ctx.send('​')

@client.command()
async def zalgo(ctx, *args):
    rounds = 10
    text = args
    if args[0].isdigit():
        if 0 < int(args[0]) < 10:
            rounds = int(args[0])
        else:
            await ctx.send('Supply valid input between 1-10. Using default value of 10 instead')
        text = args[1:]

    rounds *= 10

    output_sentence = []
    for word in text:
        output_word = ''
        for ch in word:
            for _ in range(rounds):
                ch += random.randint(0x300,0x36f).to_bytes(2, 'big').decode('utf-16be')
            output_word += ch 
        output_sentence.append(output_word)
    await ctx.send(' '.join(output_sentence))

@client.command()
async def LEAN(ctx):
    print('Its literally just cola you piece of shit. Theres no cough syrup or anything. What the fuck is wrong with you. How fucking desperate are you to seem cool that you decide you want to force a "joke" about a child consuming drugs. Which would be funny except nothing in this scene implies that theyre doing drugs or a drug stand-in. You just saw a can of soda and the two neurons in your head fired for the first time in a week, and you jumped into the comments to screech lEAn and spam purple emojis like a clown bastard. You people are the reason art is dying. Fuck you')
    await ctx.send('Its literally just cola you piece of shit. Theres no cough syrup or anything. What the fuck is wrong with you. How fucking desperate are you to seem cool that you decide you want to force a "joke" about a child consuming drugs. Which would be funny except nothing in this scene implies that theyre doing drugs or a drug stand-in. You just saw a can of soda and the two neurons in your head fired for the first time in a week, and you jumped into the comments to screech lEAn and spam purple emojis like a clown bastard. You people are the reason art is dying. Fuck you')

@client.command()
async def NFT(ctx):
    print('Dude I own this NFT. Do you really think that you can get away with theft when youre showing what you stole from me directly to my face? My lawyer will make an easy job of this case. Prepare to say goodbye to your luscious life and start preparing for the streets. I will ruin you.')
    await ctx.send('Dude I own this NFT. Do you really think that you can get away with theft when youre showing what you stole from me directly to my face? My lawyer will make an easy job of this case. Prepare to say goodbye to your luscious life and start preparing for the streets. I will ruin you.')

@client.command()
async def amogus(ctx):
    print('AMONG US Funny Moments! How to Free Robux and VBUCKS in SQUID GAME FORTNITE UPDATE! (NOT CLICKBAIT) MUKBANG ROBLOX GAMEPLAY TUTORIAL (GONE WRONG) Finger Family Learn Your ABCs at 3AM! Fortnite Impostor Potion! MrBeast free toys halal gameplay nae nae download حدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًا Super Idol的笑容都没你的甜八月正午的阳光都没你耀眼热爱 105 °C的你滴滴清纯的蒸馏水 amongla download Meme Compilation (POLICE CALLED) (GONE WRONG) (GONE SEXUAL) (NOT CLICKBAIT) Minecraft Series Lets Play Videos Number 481 - Poop Funny Hilarious Minecraft Roblox Fails for Fortnite - How to install halal minecraft cheats hacks 2021 still works (STILL WORKS 2018) Impostor Gameplay (Among Us) Zamn')
    await ctx.send('AMONG US Funny Moments! How to Free Robux and VBUCKS in SQUID GAME FORTNITE UPDATE! (NOT CLICKBAIT) MUKBANG ROBLOX GAMEPLAY TUTORIAL (GONE WRONG) Finger Family Learn Your ABCs at 3AM! Fortnite Impostor Potion! MrBeast free toys halal gameplay nae nae download حدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًا Super Idol的笑容都没你的甜八月正午的阳光都没你耀眼热爱 105 °C的你滴滴清纯的蒸馏水 amongla download Meme Compilation (POLICE CALLED) (GONE WRONG) (GONE SEXUAL) (NOT CLICKBAIT) Minecraft Series Lets Play Videos Number 481 - Poop Funny Hilarious Minecraft Roblox Fails for Fortnite - How to install halal minecraft cheats hacks 2021 still works (STILL WORKS 2018) Impostor Gameplay (Among Us) Zamn')

@client.command()
async def literally(ctx):
    print('"LiTeRaLlY nInEtEeN eIgHtY-fOuR" -George Orwell, 1948')
    await ctx.send('"LiTeRaLlY nInEtEeN eIgHtY-fOuR" -George Orwell, 1948')

@client.command()
async def fortnite(ctx):
    print('Hello, concerned father here. My son has recently got into the game called Fortnite? Ive spent well over $500 on this game and its becoming a problem. Apparently the game is down right now and its causing a lot distress for my child. He keeps taking my newspaper and tries to "full piece" me. I dont know what this means but Im starting to think its something associated with the devil. He wont come with us anywhere unless we take a "launch pad" to get there. Its starting to get worse by the hour and I dont know how much longer I can take this. His legs, arms, and hands are shaking violently yet he refuses to take any type of medicine unless its a "big pot" or "chuggies." Someone please help me.')
    await ctx.send('Hello, concerned father here. My son has recently got into the game called Fortnite? Ive spent well over $500 on this game and its becoming a problem. Apparently the game is down right now and its causing a lot distress for my child. He keeps taking my newspaper and tries to "full piece" me. I dont know what this means but Im starting to think its something associated with the devil. He wont come with us anywhere unless we take a "launch pad" to get there. Its starting to get worse by the hour and I dont know how much longer I can take this. His legs, arms, and hands are shaking violently yet he refuses to take any type of medicine unless its a "big pot" or "chuggies." Someone please help me.')

@client.command()
async def walter(ctx):
    print('My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If youre watching this tape, Im probably dead– murdered by my brother-in-law, Hank Schrader. Hank has been building a meth empire for over a year now, and using me as his chemist. Shortly after my 50th birthday, he asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using connections that he made through his career with the DEA. I was... astounded. I... I always thought Hank was a very moral man, and I was particularly vulnerable at the time – something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me in on a ride-along and showed me just how much money even a small meth operation could make. And I was weak. I didnt want my family to go into financial ruin, so I agreed. Hank had a partner, a businessman named Gustavo Fring. Hank sold me into servitude to this man. And when I tried to quit, Fring threatened my family. I didnt know where to turn. Eventually, Hank and Fring had a falling-out. Things escalated. Fring was able to arrange – uh, I guess... I guess you call it a "hit" – on Hank, and failed, but Hank was seriously injured. And I wound up paying his medical bills, which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge. Working with a man named Hector Salamanca, he plotted to kill Fring. The bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but Im a coward. I wanted to go to the police, but I was frightened. Hank had risen to become the head of the Albuquerque DEA. To keep me in line, he took my children. For three months, he kept them. My wife had no idea of my criminal activities, and was horrified to learn what I had done. I was in hell. I hated myself for what I had brought upon my family. Recently, I tried once again to quit, and in response, he gave me this.')
    await ctx.send('My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If youre watching this tape, Im probably dead– murdered by my brother-in-law, Hank Schrader. Hank has been building a meth empire for over a year now, and using me as his chemist. Shortly after my 50th birthday, he asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using connections that he made through his career with the DEA. I was... astounded. I... I always thought Hank was a very moral man, and I was particularly vulnerable at the time – something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me in on a ride-along and showed me just how much money even a small meth operation could make. And I was weak. I didnt want my family to go into financial ruin, so I agreed. Hank had a partner, a businessman named Gustavo Fring. Hank sold me into servitude to this man. And when I tried to quit, Fring threatened my family. I didnt know where to turn. Eventually, Hank and Fring had a falling-out. Things escalated. Fring was able to arrange – uh, I guess... I guess you call it a "hit" – on Hank, and failed, but Hank was seriously injured. And I wound up paying his medical bills, which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge. Working with a man named Hector Salamanca, he plotted to kill Fring. The bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but Im a coward. I wanted to go to the police, but I was frightened. Hank had risen to become the head of the Albuquerque DEA. To keep me in line, he took my children. For three months, he kept them. My wife had no idea of my criminal activities, and was horrified to learn what I had done. I was in hell. I hated myself for what I had brought upon my family. Recently, I tried once again to quit, and in response, he gave me this.')
    
@client.command()
async def me(ctx):
    await ctx.send(random.choice(TOOLS))

@client.command()
async def avatar(ctx):
    sender = ctx.message.author
    receiver = ctx.message.mentions
    if receiver:
        await ctx.send(receiver[0].avatar_url)
    else:
        await ctx.send(sender.avatar_url)

def generate_name():
    name = ''
    for i in range(random.randint(2,4)):
        if i % 2:
            name += random.choice(VOWELS).strip()
        else:
            name += random.choice(NON_VOWELS).strip()

    return name.title()

@client.command()
async def cryptid(ctx):
    embed = discord.Embed(
        title=generate_name(),
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Test Embed', value='Test Embed',
                    inline=False)
    await ctx.send(embed=embed)

######################################
#                                    #
#    [sender] [action] [receiver]    #
#                                    #
######################################

sender = None
receiver = None

@client.command()
async def game(ctx):
    global sender
    global receiver
    sender = ctx.message.author.name
    receiver = ctx.message.mentions[0].name
    options = [f'**{sender}** just made **{receiver}** lose the game!!!',
            f'**{sender}** pulled a sneaky and made **{receiver}** lose the game! What a trickster. What a jester.',
            f'**{sender}** made **{receiver}** lose the game. haha get fucked **{receiver}**. bozo']
    
    await ctx.send(random.choice(options))

@client.command()
async def bonk(ctx):
    global sender
    global receiver
    sender = ctx.message.author.name
    receiver = ctx.message.mentions[0].name
    options = [f'BONK!!!! **{sender}** bonks the everloving shit out of **{receiver}**',
            f'**{sender}** RIPS a traffic sign out of the ground and bonks **{receiver}** on the noggin. Estimated recovery time: {random.randint(1,24)} months',
            f'**{sender}** bonks **{receiver}** on the head, making a loud and obnoxious cartoon sound effect. \"And I live to bonk again...\" says **{sender}**. they stare off into the sunset.',
            f'**{sender}** bonks **{receiver}** with a baseball bat, killing them instantly']
    
    await ctx.send(random.choice(options))

@client.command()
async def bagel(ctx):
    global sender
    global receiver
    sender = ctx.message.author.name
    receiver = ctx.message.mentions[0].name
    options = [f'**{sender}** gives a bagel to **{receiver}**. \"It\'s pronounced *b-ay-gel*\", they say. **{receiver}** keels over and dies. \"Impossible...\"',
            f'**{sender}** gives a bagel to **{receiver}**. \"It\'s pronounced *b-ah-gel*\", they say. **{receiver}** keels over and dies. \"Impossible...\"',
            f'**{sender}** gives a bagel to **{receiver}**. \"It\'s pronounced *b-ä-gel*\", they say. **{receiver}** keels over and dies. \"Impossible...\"',
            f'**{sender}** gives a bagel to **{receiver}**. \"It\'s pronounced *b-æ̃-gel*\", they say. **{receiver}** keels over and dies. \"Impossible...\"']
    
    await ctx.send(random.choice(options))

@client.command(aliases=['respectfulhandshake', 'handshake'])
async def shake(ctx):
    global sender
    global receiver
    sender = ctx.message.author.name
    receiver = ctx.message.mentions[0].name
    options = [f'**{sender}** gives **{receiver}** a firm yet kind handshake. \"You\'re a real one, homeslice\"',
            f'**{sender}** gives **{receiver}** a respectable handshake. \"Godspeed, my eternal compadre\"',
            f'**{sender}** gives **{receiver}** a classic **{sender}** handshake. \"Keep on rocking, skater-bitch (positive)\"']
    
    await ctx.send(random.choice(options))

@client.command(aliases=['five'])
async def highfive(ctx):
    global sender
    global receiver
    sender = ctx.message.author.name
    receiver = ctx.message.mentions[0].name
    options = [f'**{sender}** does the WORLD\'S SWAGGIEST HIGH FIVE with **{receiver}**. The resulting shockwave kills {random.randint(3000,10000)} and injures millions more',
            f'**{sender}** high-fives **{receiver}**. holy shit they are so cool. holy fuck',
            f'**{sender}** gives **{receiver}** a high five. In the distance, a jazz solo plays. **{sender}** puts on a pair of sunglasses over the pair of sunglasses they are already wearing. Obama is there']
    
    await ctx.send(random.choice(options))

@client.command()
async def bite(ctx):
    global sender
    global receiver
    sender = ctx.message.author.name
    receiver = ctx.message.mentions[0].name
    options = [f'**{sender}** bites down hard on **{receiver}**\'s arm. ${random.randint(10000,50000)} hospital fee. (America)',
            f'**{sender}** bites on **{receiver}**\'s ear, creating several ear piercings for free! What a bargain',
            f'**{sender}** bites **{receiver}**\'s entire hand off. There is no joke here. **{receiver}** is in extreme pain']
    
    await ctx.send(random.choice(options))

@client.command()
async def deny(ctx):
    global sender
    global receiver
    new_sender = ctx.message.author.name
    new_receiver = ctx.message.mentions[0].name
    
    if receiver == new_sender and sender == new_receiver:
    
        sender = new_sender
        receiver = new_receiver

        options = [f'DENIED!!!!! **{sender}** dodges and lands a critical blow to **{receiver}**\'s jugalar',
                f'DENIED!!!!! **{sender}** does a cool backflip and boards the nearest flight to Bolivia, never to be seen again. The Boeing 787 Dreamliner {sender} is on sucks up **{receiver}** into its engine. rip bozo',
                f'DENIED!!!!! **{sender}** pulls an entire katana out of their ass (ancient samurai technique). **{receiver}** is sliced into fun celebratory confetti. YIPEEE',
                f'DENIED!!!!! **{sender}** activates their Special Move and pushes **{receiver}** down the stairs and then drags them up the stairs and then pushes them down the stairs and then',
                f'DENIED!!!!! **{sender}** does an Evasive Cartwheel and Exits the Situation. \"You Have No Bitches! Bitchless!!!\" **{sender}** shouts as they leave. **{receiver}**\'s body collapses out of pure shame',
                f'DENIED!!!!! **{sender}** does a silly dance, destroying **{receiver}**\'s body beyond recognition',
                f'DENIED!!!!! **{sender}** enters Angry Mode. \"Now Prepare You\'r\'m\'self For Utter Destrctuiioun!!\". {random.randint(3,10)} dead, {random.randint(10,20)} injured. **{receiver}**\'s corpse was never recovered']

        await ctx.send(random.choice(options))
    else:
        await ctx.send('There is no action to deny')
         
client.run(TOKEN)
