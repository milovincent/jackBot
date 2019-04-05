import sys, basebot, re

usersToTag = ['Doctor Number Four', 'liff', 'sxafo', 'D10', 'Vanna', 'Vannesa', 'The Tenth Doctor', 'FibonacciDaniel', 'Mala Lupa']

def tumble(match, meta):
    meta['self'].set_nickname('tumbleweed')
    meta['reply']('/me rolls by')
    meta['self'].set_nickname('jackBot')


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def greatScott(match, meta):
    meta['self'].set_nickname('DocBrown')
    meta['reply']('Great Scott, %s' % (meta['sender']))
    meta['self'].set_nickname('jackBot')

def alive(match, meta):
    meta['reply']('/me IS ALIVE!')
    meta['self'].set_nickname('Thunder')
    meta['reply']('/me crashes')
    meta['self'].set_nickname('jackBot')

def myThing(match, meta):
    meta['self'].set_nickname('DocBrown')
    meta['reply']('Hey, that\'s my thing!')
    meta['self'].set_nickname('jackBot')

def linkeru(match, meta):
    if meta['sender'] != 'RedditLinker':
        count = 0
        for i in re.findall('.*?\\b/?u/([\S]*)\\b', meta['msg'].content, flags=0):
            meta['self'].set_nickname('RedditLinker')
            meta['reply']('reddit.com/u/%s' % (re.findall('.*?\\b/?u/([\S]*)\\b', meta['msg'].content, flags=0)[count]))
            meta['self'].set_nickname('jackBot')
            count = count + 1
        count = 0
        for i in re.findall('.*?\\b/?r/([\S]*)\\b', meta['msg'].content, flags=0):
            meta['self'].set_nickname('RedditLinker')
            meta['reply']('reddit.com/r/%s' % (re.findall('.*?\\b/?r/([\S]*)\\b', meta['msg'].content, flags=0)[count]))
            meta['self'].set_nickname('jackBot')
            count = count + 1
def linker(match, meta):
    if meta['sender'] != 'RedditLinker':
        count = 0
        for i in re.findall('.*?\\b/?r/([\S]*)\\b', meta['msg'].content, flags=0):
            meta['self'].set_nickname('RedditLinker')
            meta['reply']('reddit.com/r/%s' % (re.findall('.*?\\b/?r/([\S]*)\\b', meta['msg'].content, flags=0)[count]))
            meta['self'].set_nickname('jackBot')
            count = count + 1
        count = 0
        for i in re.findall('.*?\\b/?u/([\S]*)\\b', meta['msg'].content, flags=0):
            meta['self'].set_nickname('RedditLinker')
            meta['reply']('reddit.com/u/%s' % (re.findall('.*?\\b/?u/([\S]*)\\b', meta['msg'].content, flags=0)[count]))
            meta['self'].set_nickname('jackBot')
            count = count + 1

def room(match, meta):
    if meta['sender'] != 'Heimdall':
        message = 'You\'re in &%s! Welcome! Say hi, guys!' % (meta['self'].roomname)
        for i in usersToTag:
            if meta['self'].users.for_name(i):
                message = message + ' @%s' % (i.replace(' ', ''))
        meta['reply'](message)


def kill(match, meta):
    meta['reply']('/me calls for a mate as a toad would')
    meta['self'].close()


def killall(match, meta):
    meta['self'].manager.shutdown()



if __name__ == '__main__':
    basebot.run_minibot(botname='jackBot', nickname='jackBot', log_users=True,
                        regexes={
                            '(?i)([\s\S]*?)how([\s\S]*?)win([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': "I'm not gonna tell you how to cheat! Mostly because I don't know :/",
                            '(?i)([\s\S]*?)how([\s\S]*?)many (?!(people|players|participants))([\s\S]*?)jackbox': 'There are 25 games total that @DoctorNumberFour has, and 10 that =3 has. Most games require at least 3 players (though Guesspionage and Fibbage only require 2 (and several only require 1! ^^)) and can hold up to 8 players, though Bracketeering can hold up to 16 and a few have lower limits. In the future, please use !games for the number of games, and !players [game] for number of players.',
                            '(?i)([\s\S]*?)how([\s\S]*?)many([\s\S]*?)(people|players|participants)([\s\S]*?)(?!(need|have|must))([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': 'Most games require at least 3 players (though Guesspionage and Fibbage only require 2 (and several only require 1! ^^)) and can hold up to 8 players, though Bracketeering can hold up to 16.',
                            '(?i)([\s\S]*?)how([\s\S]*?)many([\s\S]*?)(people|players|participants)([\s\S]*?)(need|have|must)([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': 'Most games require at least 3 players (though Guesspionage and Fibbage only require 2 (and several only require 1! ^^)).',
                            '(?i)([\s\S]*?)(what|\\bwat\\b|how(?!(many|join|play|win))|why|tell([\s\S]*?)about)([\s\S]*?)(?!(quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp))([\s\S]*?)jackbox([\s\S]*?)(?!(quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp))': 'Jackbox games are a series of games that someone hosts (ask @DoctorNumberFour or =3) and everybody can play, by opening a stream (probably at grv.to/jackboxkcd (Doctor\'s stream) or maybe at mixer.com/niekie (=3\'s stream)) on a browser tab or somewhere else, where there is a 4-character code for the current game. Then they go to jackbox.tv in another browser tab or on their smartphone, and enter the code and a nickname there. Most games need 3 players or more.\nThere are euphoria themed games, as well as fast or slow-paced games, and trivia or drawing games as well. It\'s all lots of fun!',
                            '(?i)([\s\S]*?)where([\s\S]*?)(watch|stream)([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': 'There are three locations. Most often, @DoctorNumberFour streams at grv.to/jackboxkcd, or his youtube channel, https://www.youtube.com/c/MiloSzecket_says_the_fourth_doctor_is_the_best_one/live (yes he knows how stupid the url is), and sometimes =3 streams at mixer.com/niekie.',
                            '(?i)([\s\S]*?)(how|where)([\s\S]*?)(join|participate)([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': ' First, start watching a stream, and to play the games, go to jackbox.tv and type in the room code when it comes up (4 capital letters).',
                            '(?i)([\s\S]*?)where(?!(join|participate|watch|stream|not))([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': 'There are three locations. Most often, @DoctorNumberFour streams at grv.to/jackboxkcd, or his youtube channel, https://www.youtube.com/c/MiloSzecket_says_the_fourth_doctor_is_the_best_one/live (yes he knows how stupid the url is), and sometimes =3 streams at mixer.com/niekie. If you\'re asking what page to go to to play, that\'s jackbox.tv.',
                            '(?i)([\s\S]*?)when([\s\S]*?)(?!(jackbox.{0,2}(created|founded|made)|(created|founded|made).{0,2}jackbox))([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': 'Ask @DoctorNumberFour or =3! Probably right now! https://mixer.com/DoctorNumberFour or grv.to/jackboxkcd (Doctor\'s stream), https://www.youtube.com/c/MiloSzecket_says_the_fourth_doctor_is_the_best_one/live (Doctor\'s youtube) or mixer.com/niekie (=3\'s stream).',
                            '(?i)([\s\S]*?)who([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)': 'Normally it\'s either @DoctorNumberFour or =3, but I\'d ask @DoctorNumberFour first, he\'s usually more available. If it\'s Doctor #4 streaming, the stream site is probably https://mixer.com/DoctorNumberFour, but it could also be grv.to/jackboxkcd or his youtube:  https://www.youtube.com/c/MiloSzecket_says_the_fourth_doctor_is_the_best_one/live, and if it\'s =3 streaming, the site is mixer.com/niekie.',
                            '(?i)([\s\S]*?)when([\s\S]*?)(jackbox(created|founded|made)|(created|founded|made)jackbox)': 'Jackbox was founded in 2008.',
                            '(?i)^!(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room)\s?specifics': 'These are the games we could be playing, from most likely to least likely:  \n\nMad Verse City (3-8 players) - You and at least 2 friends (and Gene) play rap-battlin\' robots!\n\nYou Don\'t Know Jack (1-8 players) - A trivia game with a twist!\n\nPatently Stupid (3-8 players) - Create inventions to solve problems – and pit them against each other!\n\nSplit The Room (3-8 players) - Vote on hypothetical questions! The winner is whoever best – you guessed it – splits the room!\n\nBracketeering (3-16 players) - The deranged debate tournament! Place smart bets on what will win stupid arguments.\n\nCivic Doodle (3-8 players) - Compete to see who can make the best additions to a mural in your attempt to "beautify" the city.\n\nQuiplash XL/2 (3-8 players) - The laugh-a-minute battle of wits and wittiness, sometimes with Euph-flavored flair!\n\nTee K.O. (3-8 players) - Draw pictures, write slogans, then swap them around to create your own custom t-shirt warriors. You can even buy them at the end!  \n\nTrivia Murder Party (1-8 players) - Be the last to survive a serial killer\'s absurd trivia game show. But it\'s fun!  \n\nEarwax (3-8 players) - It\'s the sound effects game that\'ll have you up to your ears in laughter!  \n\nGuesspionage (2-8 players) - Guess the percentages of people that do things, based on internet surveys. And it\'s fun!  \n\nBidiots (3-6 players) - Outbid your opponents for absurd art – drawn by players themselves – and win this strangely competitive auction game! \n\nSurvive the Internet (3-8 players) - It\'s survival of the funniest as you playfully take your friends out of context across the World Wide Web.  \n\nFibbage 3 (2-8 players) - Fib your way through this all new version of the classic, which is the same, but more 70s-themed.\n\nFibbage: Enough About You (3-8 players) - Fibbage with facts about the players!\n\nFibbage 2 (3-8 players) - Lie to your friends, avoid their lies, and spot the truth.\n\nBomb Corp (1-4 players): You work in an office. With bombs. (NOTE: hard to play with any lag)\n\nZeeple Dome (1-6 players) - Fling yourself at evil aliens in order to get back home! NOTE: REALLY hard to play with any lag.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)quiplash': 'In Quiplash, you and your friends each answer two prompts, and the answers you each give are voted on by the other players! It\'s a lot of fun, and there\'s even an &xkcd themed game to play!\n3-8 players',
                            '^!players quiplash':'Quiplash is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(\\bmany))|why)([\s\S]*?)(tee.{0,2}k.{0,2}o|t.?\s?k.?\s?o)': 'In Tee K. O., you and your friends draw designs, write slogans, and mix-n-match them to create t-shirts, which are then pitted against one another in a sort of battle royale! It\'s tons of fun, and you can even buy the shirts afterwards!\n3-8 players',
                            '^!players (tee.{0,2}k.{0,2}o|t.?\s?k.?\s?o)':'Tee K.O. is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)(Trivia.{0,2}Murder.{0,2}Party|TMP)': 'This is a general trivia game, but with a unique serial killer twist! From finger removal to the Loser Wheel, much deadly fun is to be had playing Trivia Murder Party! \n1-8 players',
                            '^!players (Trivia.{0,2}Murder.{0,2}Party|TMP)':'Trivia Murder Party is played with 1-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)earwax': 'In Earwax, one player is chosen as a "judge." That player chooses a prompt, and everyone else gets a list of sounds and chooses the two sounds that best represent the prompt. The judge does their job (choosing the best sounds) and the winner gets a point! The first to 3 points wins.\n3-8 players',
                            '^!players earwax':'Earwax is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)guesspionage': 'Guess the percentage of people that did a thing, based on a Reddit survey conducted yearly! Everyone else guesses higher or lower. The closer you are, the more points you get.\n2-8 players',
                            '^!players guess?pionage':'Guesspionage is played with 2-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)bidiots': 'Bidiots is a fast-paced auction game, played using art made by you! Everyone gets a paddle and some possibly terrible advice in this light-speed game!\n3-6 players',
                            '^!players bidiots':'Bidiots is played with 2-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)fibbage/s?(?!(eay|enough about you))': 'In Fibbage, the players are given a ridiculous fact with one word or phrase missing. They must spot the truth, and provide a lie to catch others. In Enough About You mode, players do the same with questions they themselves have answered, showing how much you know about your friends!\n3-8 players',
                            '^!players fibbage/s?(?!(eay|enough about you))':'Fibbage is played with 2-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)fibbage(eay|enough about you)': 'In Fibbage, the players are given a ridiculous fact with one word or phrase missing. They must spot the truth, and provide a lie to catch others. In Enough About You mode, players do the same with questions they themselves have answered, showing how much you know about your friends!',
                            '^!players fibbage(eay|enough about you)':'Fibbage: Enough About You is played with 2-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)bracketeering': 'In Bracketeering, Everybody answers a strange question, like "Which vegetable should Benedict Cumberbatch play as in his next movie?" Then your answers face off in a showdown for the ages! (which you gamble on)\n3-16 players',
                            '^!players bracketeering':'Bracketeering is played with 3-16 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)civic.{0,2}doodle': 'In Civic Doodle, the mayor of Doodle city has commissioned you (all of you) to make art to put all around the city! Take turns adding to a communal drawing, then voting on which addition is best. Maybe you\'ll even get to paint a portrait to hang in Town Hall!\n3-8 players',
                            '^!players civic.{0,2}doodle':'Civic Doodle is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)bomb.{0,2}corp': 'In Bomb Corp, you try to beat the clock in daily office tasks such as filing and defusing bombs. NOTE: Hard to play with lag.\n1-4 players',
                            '^!players bomb.{0,2}corp':'Bomb Corp is played with 1-4 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)zeeple.{0,2}dome':'In Zeeple Dome, you play a sadistic alien flinging humans around what is basically jackbox\'s version of Running Man. A gauntlet of co-op, fast-flinging fun! Unless you have lag.\n1-6 players',
                            '^!players zeeple.{0,2}dome':'Zeeple Dome is played with 1-6 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)mad.{0,2}verse.{0,2}city':'In Mad Verse City, you play a robot taking part in the sickest rap battle of the century! Answer prompts for the last word of your first line, then shit yourself as you try in vain to come up with something clever to say in the second one!\n3-8 players',
                            '^!players mad.{0,2}verse.{0,2}city':'Mad Verse City is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)split.{0,2}the.{0,2}room':'In Split the Room, you are given (and expected to create) hypothetical what-if scenarios for the other players to vote on. Hosted by Schrödinger\'s cat itself!\n3-8 players',
                            '^!players split.{0,2}the.{0,2}room':'Split the Room is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)patently.{0,2}stupid':'In Patently Stupid, you are given a problem to solve, and must do so with nothing but a sub-par cocktail napkin, a pen, and some ingenuity! Players then vote on designs in order to fund them!\n3-8 players',
                            '^!players patently.{0,2}stupid':'Patently Stupid is played with 3-8 people.',
                            '(?i)([\s\S]*?)(what|wat|how(?!(many))|why)([\s\S]*?)(y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack)':'You Don\'t Know Jack is a trivia game with a twist! It\'s like a normal trivia game, but presided over by a large streaming corporation with little-to-no backstory known as Binjpipe. Just try and figure them out!\n1-8 players',
                            '^!players (y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack)':'You Don\'t Know Jack is played with 1-8 people.',
                            '(?i)([\s\S]*?)(jackbox|quiplash|bracketeering|earwax|trivia murder party|t.m.p.|tmp|tee K.O.|tko|civic doodle|fibbage|guesspionage|bidiots|survive the internet|bomb corp|zeeple dome|mad verse city|y.{0,2}d.{0,2}k.{0,2}j|you don\'?t know jack|patently stupid|split the room).{0,2}a.{0,2}game': 'Yes!',
                            '(?i)(what|wat|how(?!(many))|why)([\s\S]*?)survive.{0,2}the.{0,2}internet': 'In Survive the Internet, you do just that by using your evil brain to twist someone\'s innocent comment about how selfie sticks are an abomination into something a genocidal maniac would say! (all in good fun of course:smile:)\n3-8 players',
                            '(?i)(^!help\s*@?jackBot$|(what|who|why)([\s\S]*?)jack.{0,2}bot)': 'I tell you about Jackbox games! Just ask (using jackbox in your question)! Use:\n !jackboxspecifics for a list of games,\n !games <user> to see how many jackbox games a user has,\n !players to learn about player requirements,\n and more! I\'ve added some easter eggs as well!\nMade by @DoctorNumberFour.',
                            '(?i)([\s\S]*?)where.{0,2}am.{0,2}i': room,
                            '(?i)this.{0,2}town.{0,2}(ain\'t|aint|isn\'t|isnt|is not).{0,2}big.{0,2}enough.{0,2}for.{0,2}(the.{0,2}two.{0,2}of.{0,2}us|the both of us|us two|both of us)': tumble,
                            '(?i)gigawatt': greatScott,
                            '(?i)back.{0,2}to.{0,2}the.{0,2}future': greatScott,
                            '(?i)great.{0,2}scott': myThing, '(\s|^|\s/?)r/([a-zA-Z]*)\b': linker, '(\s|^|\s/?)u/([a-zA-Z]*)\b': linkeru,
                            '^!kill @jackbot$': kill,
                            '^!killall @jackbot$': killall,
                            '(?i)([\s\S]*?)where.{0,2}is(.{0,2}bot.{0,2}bot|([\s\S]*?)other.{0,2}bots)': 'BotBot is down right now, sorry! Ask =3 about it. It probably won\'t be up for some time, so you can run your own using one of the many bot libraries other people have made, such as yaboli (from @Garmy) and basebot (what jackBot uses, made by @Xyzzy). you do have to take care of server-side stuff though. :/',
                            '(?i)Point for user jackBot registered\.': 'Why thank you!',
                            '(?i)^!games (=3|niekie|@=3)$': '=3 has 10 of 25 Jackbox games.',
                            '(?i)^!games (dnf|doctornumberfour|dn4|@DoctorNumberFour)$': '@DoctorNumberFour has 25 of 30 Jackbox games.',
                            '(?i)^!games$': 'There are 25 games total that @DoctorNumberFour has, and 10 that =3 has. There are a total of 30 Jackbox games.',
                            '^!players$': 'Most games require at least 3 players (though Guesspionage and Fibbage only require 2 and several only require 1) and can hold up to 8 players (though Bracketeering can hold up to 16, Bidiots and Zeeple Dome hold 6, and Bomb Corp can only hold 4).',
                            '(?i)who([\s\S]*?)jack.{0,2}bot': 'I was made by @DoctorNumberFour!',
                            '(?i)(when|where)([\s\S]*?)jack.{0,2}bot': 'I am an eldritch abomination from a land outside of time. Do not ask me such trivial things.',
                            '(?i)([\s\S]*?)is.{0,2}this.{0,2}real.{0,2}life':'Yes',
                            'how([\s\S]*?)base.{0,2}bot':'Ask @Xyzzy.',
                            '/me spies an? @?jackBot':'/me spies you back',
                            '/me has resurrected @jackBot':alive,
                            '^!help$':'Just ask!'})
