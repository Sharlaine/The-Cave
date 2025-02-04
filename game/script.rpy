# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#CHARACTERS
define e = Character("Eileen")
define b = Character("You")
define g = Character("Girl")

#IMAGES
image charlotte neutral = "charlotte neutral.png"

#TRANSFORMS
transform character_right:
    yalign 1
    xanchor 0.5
    xpos 0.85
    zoom 0.35

transform shake_bg_mid:
    linear 0.05 ypos 0.52
    linear 0.05 ypos 0.5
    repeat

transform bg_top:
    yalign 0

transform bg_topish:
    yalign 0.25

transform bg_mid:
    yalign 0.5

transform bg_bottomish:
    yalign 0.75

transform bg_bottom:
    yalign 1.0

#EFFECTS
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define hurt_flash = Fade(0.2, 0.0, 0.8, color='#f00')

#SCREENS
screen inventory_bar():
    frame:
        xalign 0 ypos 0

        has hbox spacing 20
        text "Inventory:":
            xalign 0
            yalign 0.5
        for i in bag:
            if i != "":
                use item(i)

screen item(item_pic):
    add item_pic.icon:
        xalign 0 
        zoom 0.05

#PYTHON
init python:
    class Item:
        def __init__(self, name, icon):
            self.name = name
            self.icon = icon
        
        def add_to_bag(self):
            renpy.hide_screen("inventory_bar")
            bag.append(self)
            renpy.show_screen("inventory_bar")
            renpy.notify("You have obtained " + self.name)

        def use(self):
            bag.remove(self)
            renpy.notify("You have used " + self.name)

#START
label start:

python:
    injuries_C = 0
    injuries_player = 0
    artifact_have = False
    bag = []
    
    #ITEMS
    lighter = Item("Lighter", "item lighter.png")
    firstaidkit = Item("First Aid Kit", "item firstaid.png")
    paracord = Item("Paracord (80m)", "item paracord.png")
    pocketknife = Item("Pocketknife", "item pocketknife.png")
    statue = Item("Half-Finished Wooden Statue", "item woodenstatue.png")
    flashlight = Item("Flashlight", "item flashlight.png")
    knocker = Item("Large Knocker Ring", "item knockerring")
    moss = Item("Healing Moss", "item moss.png")
    stoneidol = Item("Stone Idol", "item stoneidol.png")
    lifeidol = Item("Life Idol", "item totemwhite.png")

scene bg darkness

b "{i}Uugghhh my head..."
b "{i}Feels like I got hit by a semi..."
b "{i}Where am I? Why can't I see nothing?"
"{cps=15}*Rocks Shifting*"
b "{i}The hell was that?"
menu:
    "Call out":
        jump choice1_call

    "Throw Rock":
        jump choice1_throw

label choice1_call:
    b "Anybody there?"
    g "Oh thank God it's another person!"
    jump choice1_done

label choice1_throw:
    b "{i}If it's some kind of animal or creature, I'd better throw something far away to not draw attention to my position.{/i}"
    "*Throws*{p}*Clatters*"
    g "{size=+20}EEEEP{/size}"
    b "A girl?{p}Hello?{w} Sorry if I scared you, I didn't know you were a person."
    b "What's your name?"
    jump choice1_done

label choice1_done:

g "My name is Charlotte! I'm so glad I'm not alone! Unless you're a bad guy! Are you a bad guy? What's your name?"

define C = Character("Charlotte")

b "Whoa easy there, I'm not a bad guy haha"
b "You're real rapid-fire ain't ya?"

python:
    name = renpy.input("My name is:")

    name = name.strip() or "Adam"

define player = Character("[name]")

player "My name is [name]. Nice to meet you [C],{w} I'm sure you look lovely through all this darkness haha"

C "I hope you're not flirting with me."
player "Haha no sorry. I'm just relieved to not be the only one here and it's nice that we have two heads to work with and I just ramble nonsense to calm nerves. It happens, y'know?"
C "Hmmm{cps=2}...{/cps}{w=0.5} Alright then?"

C "So what do you make of this?"
player "Looks like some sort of cave?"
C "Looks? {w}Haha Mr. Funny Man."
player "Figure of speech! You know what I mean..."
C "{cps=4}Mhm...{/cps}{w=1} Anyways, how do we get out? {p}No use sitting here and waiting. Even if anyone knows we're missing I'm not even sure they can reach us wherever we are."
player "{i}What to do?{/i}"

menu:
    "Check your Pockets":
        jump choice2_pockets
    
    "Find the cave wall":
        jump choice2_wall

label choice2_pockets:
    $ pockets = True
    player "*pats pockets*{p}*rummages through waist pouch*"
    C "Watcha doin' there bud?"
    player "Checkin' if I got anythin' useful on me"
    C "Ah! Good call. {size=-18}Why didn't I think of that?{/size}"

    jump get_lighter

label choice2_wall:
    $ pockets = False
    "You decide to walk forward in hopes of bumping into something. The tip of your shoe manages to make contact with something rough and sturdy. You trail your hand across the surface."
    player "Hey, Charlotte!"
    C "Yeah?"
    player "I managed to find a wall. Follow my voice! Maybe we can follow this wall outta here."
    C "Are you serious? It's pitch black! My ears aren't that good y'know."
    player "You can stay there if you reaalllly want to." 
    player "*pretends to walk away*"
    extend "\n*step*{w=1}\n*step*{w=1}\n*step*"
    C "NO, wait for me!!" 
    "In a sudden panic, Charlotte blindly runs in the direction where she last heard [player]'s voice."
    
    $ injuries_C = injuries_C + 1

    "Charlotte, oblivious that her shoelace was undone the whole time, steps on the lace and lifts her other foot. She stumbles and lands on her knees, scraping them on the cold rugged ground. The impact of her fall echoes around the cave walls."
    "{size=+20} *THUD*"
    C "Owwww... That was stupid."
    player "Are you okay?? That didn't sound too good."
    C "*Whimpers* {p}I-it's fine. Just gotta shake it off. It's just a scrape."
    "Charlotte slowly rises and brushes the dust and dirt of her scout uniform."
    player "Are you feelin' up to it? We can rest up a bit first if you're not ready to be walkin' around."
    C "No no, I can do it. Plus, we can prob'ly find a place to wash my cuts. That'd be something to look forward to."
    jump get_lighter

label get_lighter:
    "Charlotte feels through her pockets and examines the contents of her pouch."

    if pockets:
        extend " She manages to pull out a lighter from the inner pocket of her pouch."
    else:
        player "What's all that rustlin'?"
        C "I'm seeing if I got anything useful before I start wanderin' in this pitch blackness again."
        player "{i}That's a bright idea{cps=4}...{/cps}{p}Good thing I didn't say that aloud."

    "*click*{p}*click*{p}*Fwo{nw}"

    scene bg cave1_warm at bg_bottomish
    show charlotte neutral at character_right with flashbulb:
    
    extend "osh*"

    $ lighter.add_to_bag()
    
    show charlotte shocked
    C "OH GOSH!"
    player "*Flinches* \n What!?! What happened?!"
    show charlotte worried
    C "O-oh no it's uh.. I just wasn't expecting to see you right away haha."
    player "Are{cps=4}...{/cps}{w=0.25} Are you callin' me ugly?"
    C "No no, not at all" 
    C "*Coughs*"
    show charlotte neutral
    C "Anyways, looks like this is all I have, everything else must've fallen out. You got anything useful?"
    "You rummage through your own pouch and pull out an item."

    $ pocketknife.add_to_bag()

    player "How's a pocket knife sound?"
    C "Better than nothing. At least it's a start."
    jump choice2_done

label choice2_done:
"Charlotte walks towards [player] with her lighter in hand. She moves it around the cave to light up some of the space around them."
C "Totally not creepy at all. Perfectly normal don't ya think?"
player "Yep. Perfectly normal considering we've been knocked out for who knows how long and didn't die from any random creatures lurkin' about. Oh shoot, I'm ramblin' again."
C "Pfft. No worries, makes sense. I'd be rambling too if I we didn't have this lighter."

"The two follow a dimly lit path. As they shuffle in the dark, they come across what they assumed to be a large cavern to their left. The lighter flickers and sways."
C "Airflow? {w=0.5}{nw}"

show charlotte happy

extend "Good news! We're not as deep as I thought we were then, eh?"
player "Sounds about right? So airflow means there's an exit somewhere or somethin' right?"

show charlotte neutral

C "I mean, it's possible. Not too sure tho- {w=0.5}{nw}"

show charlotte happy

extend "Oh hey look over there!"
"Charlotte points to a crevice a few meters ahead of them."
C "It looks big enough for both of us to shimmy through! Maybe that's where the air current is coming from. Worth a shot right?"

menu:
    "Shimmy through the crevice":
        jump choice3_crevice

    "Explore the area":
        jump choice3_cavern

label choice3_crevice:
    player "Like you said, worth the shot so let's try it!"
    "The two of you walk up to the crevice and Charlotte gives you her lighter and gestures to the crevice"
    C "Lead the way~"
    "You begin to side step into the narrow entrance, arm outstretched for an optimal view of the path."
    
    scene bg crevice_edit at bg_mid
    
    player "Damn, this shimmy session is gonna be longer than I thought it'd be."
    
    show charlotte worried at character_right
    
    C "Wha?? You gotta be kidding me. I haven't even stepped in yet and I'm already exhausted from hearing you say that."
    player "You say that as if you're not gonna be in here soon haha."
    C "Ughhh."
    show charlotte neutral
    "Charlotte follows behind you while you wait for her to catch up."
    player "Never thought I'd be shimmyin' today. I shoulda stretched first haha."
    C "Honestly... same. I'm stiff as a rusty door."

    if injuries_C > 0:
        C "I'd be more limber if only SOMEONE didn't pretend to abandon me earlier."
        show charlotte annoyed
        C "*Glares*"
        player "*Whistles*\n*Avoids eye contact*"
        hide charlotte

    "You and Charlotte are almost out of the crevice and suddenly, you feel the world shake.{nw}"
    
    show bg at shake_bg_mid
    
    extend "{w=1} It wouldn't have been a big deal, until you hear crackles of stones and the walls behind Charlotte start to break down."
    player "{size=+20}LET'S HURRY AND MOVE IT. DON'T LOOK BACK."
    
    show charlotte worried at character_right

    C "Wha-{p}*looks back*{w=0.5}{nw}"
    
    show charlotte shocked

    extend "\nCrap, {size=+10}{w=0.25}crap, {size=+10}{w=0.25}CRAP {size=+20}{w=0.25}MOVEEE!!{/size}"
    "Both of you shimmy as quick as you can without blowing the lighter's flame out. You finally reach the crevice's exit. You take Charlotte's hand and pull her out before the rubble could get to her."
    
    show bg at bg_mid
    
    show charlotte worried
    C "*Huff*{w=0.8} *Huff*{w=1}\nYeah, let's not do that again. {w}No more crevices."
    player "*Huff*{w=0.8} *Huff*{w=1}\nI second that."
    C "Never thought I'd experience an earthquake like that."

    show charlotte neutral

    extend "\n*stretches*{w=1} \nWhere are we now?"
    player "*moves lighter around*{p}Another cavern I think."
    C "Hey [player], move the lighter to the right would ya? I think I saw something."
    "You move the lighter and see a lump on a large stone slab."
    player "No way."
    player "It's my bag! Now that's what I'm talkin' about!"
    C "Finally some good news. What's inside?"
    player "Lemme show ya."
    "You give the lighter back to Charlotte to hold and open the flap of your bag. In it are some snacks and a half empty water bottle. {w}Nothing too exciting until you pull out a bundle of paracord and your half-finished wooden statue.{w}{nw}"
    
    $ paracord.add_to_bag()
    extend "{w}{nw}"    
    $ statue.add_to_bag()
    extend "{w}"

    player "It don't look like much but hey, it's a good start."
    C "You carve things? Oh! That would explain your pocket knife huh?"
    player "Yeah, very perceptive of you."
    C "*Shrugs* I try."
    "You sling the bag onto your back and Charlotte returns the lighter to you."
    player "Let's keep goin'."

    jump choice3_done

label choice3_cavern:
    "You scratch your chin, debating on which option would help you two the best."
    player "Let's check the cavern first. It'd be a waste to not investigate."
    
    if injuries_C > 0:
        player "And hey, maybe we can find something to treat your wounds right? Win-win for you~"
        C "Awww, are you worried about me? If you're worried you coulda just said so."
        player "Look who's flirting now."

    "Charlotte hands you her lighter and you walk into the open area. With no walls in arm's reach, you can only imagine the amount of space to tread in order to find something of use."
    C "Still not much to look at with just the a small lighter huh? It's better for us to stick together while we scan around."
    player "Agreed."
    "The two of you stand side by side, Charlotte scanning the right side of the cavern and you taking the left. You both move slowly and carefully."
    player "*squints*{p}I think I see something."
    C "Where?"
    "You point to a round shape on the ground, dimly lit but visible enough to see its distinct pattern against the coal-coloured ground."
    C "Is that what I think it is??"
    "Charlotte starts to move towards the object."
    player "Careful! Don't run off too far- {w=0.5}\nA bag?"
    C "Yeah, it's mine... {w}How'd it even get here?"
    player "Beats me. What do you have in there?"
    C "Let's see, hopefully nothing too important fell out."
    "Charlotte unzips the pockets of her backpack, uncovering essential snacks and water for for the scout's adventuring. You catch a glimpse of a small box in the front pocket of her bag."
    player "What's that?"
    C "*Pulls out a first aid kit*"

    $ firstaidkit.add_to_bag()

    extend  "\nKinda empty but we can still make do with it. Oh wait, there's more!"
    C "*Pulls out a flashlight*{p}This'll really brighten things up!"

    if injuries_C > 0:
        C "Wow, you weren't kidding when you said it was a win-win!" 
        player "I honestly didn't think that win-win moment would come now, but might as well get you patched up."
        "You use the newly acquired flashlight to help Charlotte assess her injuries."
        player "*chokes* I thought you said it was a scrape?! {w}That doesn't look like 'just a scrape' to me."
        C "Sure felt like a scrape. Can't change the past now."
        "You look away, feeling a bit queasy, while Charlotte focuses on disinfecting and wrapping her wounds."
        C "All good to go!"
        
        $ injuries_C = injuries_C - 1
        $ firstaidkit.use()

        player "*Trying not to gag* {p}Mhm *Thumbs up*"

    else:
        player "Keep that first aid kit close. Who knows if we'll need it down the line."
        C "No need to tell me twice. Also, don't jinx it! I really wouldn't want to be forced to use    it." 
        "Charlotte drops the first aid kit in her bag, zips it closed, and slings it on her back."

    "The two of you start to walk back towards the crevice. An unexpected rumble startles you both as you scramble to hug the walls for stability. Now that Charlotte has a flashlight, you can clearly see the stone ceiling above the crevice crumble and fall, sealing off your intended path."
    player "Well, uh, looks like that's not an option anymore?"
    C "*moves her flashlight around*{p}Haha, you know what they say. When one door closes, another opens and well, something did open."
    "You follow the direction of her flashlight and see a broken wall on the other side of the cavern. You walk towards and and see a path to who knows where. You look at each other."
    C "Any other options?"
    player "Nope."

    jump choice3_done

label choice3_done:

hide charlotte

"The path felt like a long one. No unexpected twists and turns, but seemed never ending."
"You two walked in silence, not because of the exhaustion of it all nor the fear of mundane conversation, but to recollect your thoughts and take the time to breathe."
"After what seemed like an hour, you finally reach a large open area. It's been a while since you've been in a well lit room and you finally get a glimpse of your surroundings."

scene bg largecavern1 at bg_bottomish

"This cavern is significantly larger than the one you passed earlier."
"The hole in the ceiling conveniently lights the majority of the cavern. In front of you is a pool of water with another area, unfortunately still shadowed in darkness, on the other side with what looks to be a possible exit."

show charlotte happy at character_right

C "Oh my gosh, light! {nw}"

if flashlight in bag:
    extend "*Turns off flashlight* {nw}"

extend "Nice to know we're at least near the surface. Maybe someone will be near by when we reach an exit."
player "That'd be a convenient coincidence now wouldn't it. *Puts the lighter away*" 
"Charlotte scans around the area and notices something up ahead."

show charlotte neutral

C "Speaking of people, I think I see something over there."
player  "{cps=200}*Jumps*{w=0.5}\nW-What!?!{w=0.5} Where?!{w=0.5} A person?!{/cps}"
C "Oh whoops! I meant these."
"Charlotte walks you to one of the cave walls and points to what looks to be a series of bronze objects protruding from the walls."
player "Charlotte, please be more specific. I almost had a heart attack thinking you saw some stranger. I welcome help but who knows what type we'll meet in the middle of a cave?"
player "No offense."
C "None taken."
C "But yeah sorry, these pitons are pretty clear evidence of people before us. Maybe longer ago than we thought though."
player "*Looks up*\nLook, there's a ledge with an opening up there too! Could be a way to an exit. Maybe we can use them to climb up!"
C "True, true. There's also that area past the water. We got some options on our hands." 

menu:
    "Climb the Wall":
        jump choice4_climb

    "Wade through the Water":
        jump choice4_water

label choice4_climb:
    player "How do you feel about climbing? I mean, if there were people that used those to climb, that seems like a good sign, dontcha think?"
    C "I don't want to toot my own horn or anything but I'm pretty good at free solo haha."
    player "At what?"
    C "Climbing without equipment."

    if paracord in bag:
        player "*Pulls out paracord from bag*\nAlright muscles, you think you can climb all the way up there and then send this down for me?"
        C "*Stretches*\nI got this."

        if injuries_C > 0:
            C "Of course, I'd feel more confident if my legs were in better shape but it's not like I have that luxury." 
            player "*Stares* {p}You're really just gonna guilt trip me now, are you?"
            C "Relax, it's just a joke with a seed of truth in it."
            "Charlotte places her hand on your shoulder as if to reassure you."

        "You give Charlotte the paracord and she walks up to the wall, assessing her route. She mimes out her actions and you couldn't help but join in too. With surprising strength and patience, Charlotte scales the wall as if it's second nature. She manages to reach the top ledge."
        C "Lemme find something to tie this cord to- Oh what's this?"
        player "Hey, don't leave me here!"
        C "Don't worry. *Throws paracord down* Just went to secure it to something while you climb up. Also! I found something!"
        "You start to climb the paracord."
        player "{i}I should start working out after this... I'm sweatin' up a storm."
        "You reach the top and Charlotte lends you a hand and pulls you up."
        C "Nice to see ya!"
        player "Likewise~ So what were you saying earlier? You found something?"
        C "Yeah, I walked a bit a head while waiting for you and snagged this"
        "She holds out her other hand."

        jump choice4a_getknocker

    else:
        player "I gotta say, I'm not as confident as you are. This body is not meant for climbing."
        "You wiggle your arms like noodles."
        C "Pfft, I wasn't gonna point it out but now that you mentioned it, you do have noodle arms. Say what you will but, maybe I have faith that you can pull it off." 
        player "I don't know if I should feel offended or encouraged."
        C "As long as you follow exactly what I do, you should be fine."
        "Both of you stretch and loosen up a bit before Charlotte takes the lead. She mimes out her visual route and starts to climb, with you tagging behind. As she climbs and grabs onto a pattern of protrusions and pitons, Charlotte details her movements for you to follow suit. You start to feel your strength wither away, arms and legs both shaking. You grab onto a piton and it snaps, your hand slips and ends up wedged into a crack in the wall. You screech as the pain shoots from your wrist and up into your shoulders."
        C "[player]!"
        "Charlotte shoots up onto the ledge and reaches her arm out."
        C "I'm here! I got you!"
        "You take the risk and with all the strength you can muster in your legs. You jump and grab Charlotte's arm to hoist you up. You curl up holding your wrist with your other hand."
        
        $ injuries_player = injuries_player + 1

        if firstaidkit in bag:
            C "H-Hold on! \n*Takes her bag off and pulls out the first aid kit*" 
            C "*Looks around for a stick* \nDid you feel it break? Or is it a sprain or something."
            player "Uhhhh... \n*Dazed*"
            C "It's fine. Let's just do this for now just in case."
            "Charlotte takes your hand, places the firm stick on your forearm and wraps your arm with the leftover gauze in the first aid kit."

            firstaidkit.use()
            $ injuries_player = injuries_player - 1

            "..."
            C "How're you feeling?"
            player "Better than before I suppose."
            C "Yeah...You kinda passed out? I wasn't sure what to do so I just waited here. Sorry, I kinda ate a good amount of our snacks, but the water's still available haha."
            player "*Looks at wrist*\nThanks for your help. I owe ya."
            C "You owe me double! 'Cause look what I found."
            "She holds out her hand."

            jump choice4a_getknocker

        else:
            C "*Helps you hold your wrist in place*\nIs it broken or do you think its a sprain?? Scale of 1 to 10 how painful?? 10 is the highest."
            player "Uhhh... 7?"
            C "Oh good. Maybe it's not serious. Uh, maybe try to move your wrist around slowly once you feel the pain ease up."
            player "Sure thing boss. *Flashes a thumbs up and winces*"
            C "Wait here, I'll scout out the path ahead if there's anything we can use."
            player "Hey, don't go too far. We can go together."
            C "*Sighs* Alright, Alright. I'll walk in your field of vision."
            "..."
            player "Found anything?"
            "She holds out her hand."

            jump choice4a_getknocker

    label choice4a_getknocker:
        player "A giant ring?"
        C "Yup. But doesn't it look like one of those fancy door knocker things? Y'know, the ones that make you feel spiffy when you use it to knock instead of your knuckles."
        player "Now that you mention it, yes, it does. It could come in use so let's bring it. Who knows, maybe we'll find a door to knock on."
        C "Haha alright. {nw}"
        
        $ knockerring.add_to_bag()
        
        extend "\n*Loops it through her belt and buckles her belt up again.*"
    
    jump choice4_done

label choice4_water:
    player "Let's go across the water, I'm not too confident in my arm strength."
    C "With noodles like those I ain't too surprised."
    "You both approach the water"

    if flashlight in bag:
        player "Could you do me a favor and shine up the water for me? I wanna see how deep it is."
        "Charlotte lights up the water."
        C "Hey look, there's an underwater ledge! I think it goes all the way across? *Whistle*\nIt's wide enough to walk normal."
        player "Whew, I thought we were gonna have to wade over. Glad only our little piggies need to take the plunge."
        "You both cross the water with only slightly damp feet."

    else:
        "[player] sticks his leg into the water all the way and it still doesn't reach the bottom."
        player "Well, {w}wish me luck."
        "[player] plunges into the water"
        player "{size=+20}CO- {size=-5}*Gurgle*"
        C "[player]! What happened!?"
        "Charlotte reaches into the water and grabs [player]'s arm to pull him up but she notices some oddly warm water on the arm she grabbed"
        player "*surfaces*\n Ah tits, be more gentle will ya!"
        "[player] clambers back onto land, cursing in ways Charlotte never heard before"
        Charlotte "What happened? Why's your arm covered in blood!?"
        player "^%#$%$ rock happened that's what! Gashed me bloomin' arm!"
        C "A rock? Where?"
        player "'Towards the left wall, the sneaky bugger, thinks the darkness means it can surprise folk like that, @%#$ piece of @%#$&# in a pile of *#^$%&. I hope you crumble to dust."
        C "Ummmm... so do you want the good news first or the bad news?"
        player "Tear that bandage right off, what's our latrine being filled with?"
        C "You didn't need to get wet. The good news is that the rock seems to be a ledge and I think I can barely see it going all the way over."
        "[player] begins to curse for several minutes."
        "You both cross the water as you curse up another storm about how blood loss and hypothermia are having a race to see who can kill him first"
        "By the time you get to the other side, you've calmed down significantly and even your accent seems to have retreated."
        C "So British huh?"
        player "Sort of, grew up all over Europe but yeah I was born in Britain. Ma and Pa loved road trips before the triplets. Hopefully when the triplets grow up, Ma and Pa find the energy to go on road trips again. "

        $ injuries_player = injuries_player + 1

    "As you reach the end of the pool, you notice the ground getting{cps=4}...{/cps}{w=0.3} fuzzy"
    player "Great, another slippin' hazard. {w}At least this one's hard to miss."
    C "Wait...{w} Is this what I think it is?"
    player "I just see some fuzzy patches of asininity waiting to get our arses bruised."
    C "First off, this species of moss is mostly under whatever surface it's on and the parts in open air are usually bone dry and therefore not slippery."
    C "Secondly, this moss is super rare and in high demand since it has very strong healing and antibacterial properties."
    player "So that means we don't gotta worry about any more injuries! At least in the long term."
    C "THIRDLY, a side effect of how it grows means that the surface part, the only part we can even gather right now, is mostly air. So we're gonna need basically everything we see just for a poultice big enough"
    
    if pockets = False:
        extend " for this knee."
    
    else:
        if injuries_player > 0:
            extend " for yer arm."

        else:
            extend " for anything larger than a scraped knee."
    
    C "Regardless, it's a nice thing to have even if we've barely got one use of it."
    "You and Charlotte grab all the moss you see, the armload you both got really compacting down to the size of both of your fists"
    $ moss.add_to_bag()
    C "Wait till you add water to apply it, it'll shrink to like half that."        

    if injuries_C > 0 and injuries_player > 0:
        player "So you wanna use it? Your gash looks way uncomfortable to walk on."
        C "Eh, I got used to it. I got used to getting scratched up and powering through when I got these babies. \n*Points at the badges on her sleeves*"

    menu:
        "Heal Charlotte":
            jump choice4a_C

        "Heal yourself":
            jump choice4a_player

    label choice4a_C:
        player "I insist, you must've powered through more than enough injuries to be as nonplussed as you are about your knee. I think I should take a page from your book and \"build some character\" myself"
        "You mix the moss with water and it shrinks even more, barely enough to cover the gash on her knee"
        
        $ moss.use()
        $ injuries_C = injuries_C - 1
        
        "You both decide to get back to getting out of here"

        jump choice4a_done

    label choice4a_player:
        player "Yeah I guess you do seem to be doin' fine with that leg."
        player "Me on the other hand.{w} I feel like I'd faint if so much as a breeze touches me arm."
        "You mix the moss with water and it shrinks even more, barely enough to cover the gash on your arm"
        
        $ moss.use()
        $ injuries_player = injuries_player - 1
        
        "You both decide to get back to getting out of here"
        
        jump choice4a_done

    label choice4a_done:
    C "Sure do hope this tunnel ain't a dead end."
    player "Only one way to find out."
    jump choice4_done


label choice4_done:

"You two continue down the path."
C "Don't you think it's strange?"
player "What's strange?"
C "These tunnels are pretty clear. Like sure, there's rubble and such, but for the most part, we haven't really had any issues walking around this place. How big do you think this cave even is?"
player "Who knows. Maybe it was once a home for a small community or somethin'. I wouldn't be surprised."
C "True... I could see that, if we weren't stuck here I mean."
player "We're not gonna be here for long. We're gettin' outta here together."
C "Haha, got that right! Let's go to a buffet after all this is done n' over."
player "Aww you're gonna pay for me? Thanks, I accept your invitation~"
C "Wait, what?!"

"You and Charlotte sit in an open section of the path you've been walking, the light from outside giving you a bit of warmth and hope. Drinking the last drops of water and remaining snacks you get up from your spot and dust off your uniform."
C "Almost feels like we're in the homestretch huh? I gotta say, we just met not too long ago, but it's a nice feeling not having to shoulder the burden of life and death alone."
player "You gettin' poetic on me?"
C "Nah, *scratches neck* just feels like the best time to say it."
player "That ain't ominous at all."
C "Ughhh, you know what I mean. Anyway, the moment's gone now so you lost your chance to be sentimental."
"Charlotte skips ahead and you can't help but chuckle at your new friend."
C "Hey [player], check this out!"
"You follow the sound of Charlotte's voice and find her looking up at a section of the ceiling where a piece of rock juts out to form some sort of shelf. You squint and notice something relatively large balancing laying on it. The object looks as if it could be pulled off with some effort."
player "Think it's worth it?"
C "Anything's worth it if it helps us out. Of course if we don't injure ourselves in the process."

if paracord and knocker in bag:
    "You look at Charlotte's belt, at the large knocker ring you found recently."
    player "I got an idea, it involves that ring of yours."
    "You pull out your paracord and Charlotte removes the ring from her belt and hands it to you. Tying a secure knot around the ring, you do some test throws with it to ensure the ring doesn't go rogue."
    C "How nifty. Nice to know the gears are still turning in there after who knows how long."
    player "Haha, ye. You're lucky I still got some brain battery left over."
    "Swinging the paracord, you take your aim. It takes a few attempts but you finally managed to slot the cylindrical object into the ring and yank it down. Charlotte catches the item in her arms."
    player "What a catch! What fish did we reel in?"
    C "Uhhhh. *Shows you a stone idol* {nw}"
    
    stoneidol.add_to_bag()

    extend "This?"
    player "A stone idol huh? I wonder what it was used for."
    C "Well, now that we have it, we can find out maybe?"
    player "Yup. I'm sure the opportunity will present itself."
    "Charlotte places it in your bag. Due to its height, it now comically pokes its head out."
else:
    if injuries_C < 1 and injuries_player < 1:
        player "Wanna try an old fashioned boost?"
        C "Gladly!"
        "You give Charlotte a boost. Unfortunately she comes up short."
        player "Lemme have a go."

        jump boost_C

    if injuries_C > 0:
        player "Wanna try an old fashion boost?"
        C "Yeah...maybe not, my knees are takin' their toll."
        player "*Looks at Charlotte's relatively fresh skid marks on her knees* Ah shoot, sorry, I completely forgot."
        C "No biggie."
        player "Sorry about that by the way... Dumb move on my part."
        C "Hey, don't worry about it. We're past that now. Anywho, let's just move on. Doesn't look like we'll get to uncover that treasure."

    if injuries_player > 0:
        player "I'd boost ya, but my whole arm is outta commission."
        C "I can try to boost you."
        player "Aight. Let's do this."

        jump boost_C
  
    label boost_C:
        "Charlotte boosts you and her arms immediately start shaking."
        C "Dude, are you made of lead or something!?! Why are you so heavy!"
        player "Hey! Has anyone told you not to mention a man's weight! *reaching out*"
        "You jump back to the ground."
        player "Mission failed on this one."
        player "At least we can say we tried."
        C "Yeah... It's prob'ly not important anyway. At least, that's what I'm gonna tell myself."
        player "I concur. Let's save our energy while we still have some."

"A fork in the tunnel presents itself."
C "Oh wow, we got a choice on our hands! Been a while hasn't it."
player "Left or Right huh?"
C "Yup! Better be careful which one you choose."
player "Why do I gotta choose."

show charlotte happy

C "'Cause I don't wanna be responsible if something bad happens~"
"You groan while Charlotte's cackle bounces around the cave walls."

menu:
    "Go Left":
        jump choice5_left
    
    "Go Right":
        jump choice5_right

label choice5_left:
    player "Left it is."
    "You and Charlotte go into the tunnel on the left."
    "A few minutes later."
    player "Is it just me or is the cave looking{cps=4}...{/cps} cleaner?"
    C "What do you mean?"
    player "It feels like the cave is traveling straighter, like it's more intentional now. I don't know, I could just be imaginin' things."
    C "I don't think you're imagining it..."
    "You and Charlotte stop in your tracks"
    player "Is that a brazier?"
    C "Either that or a real fancy stalagmite."
    "You start walking towards the brazier. It felt as if it was calling you. Surprisingly, there are hot coals inside it, hot enough to light something on fire."

    if pocketknife and statue in bag:
        player "Ah!"
        "You reach into your bag and grab the wooden statue you were working on and whip the pocket knife out of your pouch. Charlotte watches you and you shave off bits of wood from your carving.The wood shavings start to burn and flames bloom to life."
        C "Whoa [player], there's something emerging from the coal!"
        "Staring into the flames, you noticed a stone pedestal"

    else:
        C "What are you doing? It's not like we can do anything with it. There's nothing in it for us to use either. Unless you wanna throw coal at each other."
        player "I guess you're right. But I can't shake this feeling' like we could've done somethin' here."
        "You walk away, look back at the brazier, then head back to retrace your steps and check out the other path."
        jump choice5_right

label choice5_right:
    player "Right it is."
    "You and Charlotte go into the tunnel on the right."
    "After walking for several minutes, Charlotte notices something."
    C "I hear birds.{p} I think we-{nw}"
    player "Hup. {w=0.5}Zip it. Don't jinx it."
    C "Fine, then I guess those are bats and we accidentally made our way deeper.\nNyeh *Sticks out Tongue*"
    player "Better."
    "You stop in your tracks as you stare at the sight before your eyes. You and Charlotte look down at the bottomless gap before you. It's just large enough that you would need to jump to even start climbing. Thankfully, the ledge is just short enough that if one of you gives the other a boost, they should be able to reach the ledge. You can only hope that there's something on the other side that you can use to help the other one across."
    C "Looks like we can boost each other. One of us is sure to make it."
    player "Heh. You must be a mind reader 'cause I was thinkin' the same thing."
    C "Well, you were making a face. Like you were staring into the void...well technically you were but y'know what I mean."



return

# The game starts here.

# label start:

#     # Show a background. This uses a placeholder by right, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room with Pause(3)

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return
