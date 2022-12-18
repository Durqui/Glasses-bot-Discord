import hikari

#Token to connect bot to discord
bot = hikari.GatewayBot(token='toekn',intents=hikari.Intents.ALL)

#Copypasta broke up into parts
Pt1 = "Glasses are really versatile. First, you can have glasses-wearing girls take them off and suddenly become beautiful, or have girls wearing glasses flashing those cute grins, or have girls stealing the protagonist's glasses and putting them on like, Haha, got your glasses!"
Pt2 = " That's just way too cute! Also, boys with glasses! I really like when their glasses have that suspicious looking gleam, and it's amazing how it can look really cool or just be a joke. I really like how it can fulfill all those abstract needs. Being able to switch up the styles and colors of glasses based on your mood is a lot of fun too!"
Pt3 = " It's actually so much fun! You have those half rim glasses, or the thick frame glasses, everything! It's like you're enjoying all these kinds of glasses at a buffet."
Pt4 = " I really want Luna to try some on or Marine to try some on to replace her eyepatch. We really need glasses to become a thing in hololive and start selling them for HoloComi. Don't. You. Think. We. Really. Need. To. Officially. Give. Everyone. Glasses?"
Copypasta = Pt1 + Pt2 + Pt3 + Pt4
triggers = ["glasses", "Glasses"]

#Bot reads messages to see if it's trigger word comes up
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    if event.is_human:
        msg = event.content.split()
        thislist = list(msg)
        #Cross references the words in the triggers list with word in the message
        for j in triggers:
            for i in thislist:
                if i == j:
                    await event.message.respond(Copypasta)
                    break
                else:
                    print("Check fail")
                    pass


#Fun start up message in command prompt
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Hi friends!')


bot.run()