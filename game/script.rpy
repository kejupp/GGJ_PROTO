# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nao = Character("Naoki")
define jos = Character("Josie")
define unknown = Character("???")
define bad = Character("Kitarou")
define omi = Character("Naomi")
define cute = Character("Ichigo")

image Kitarou neutral = "images/Kitarou neutral.png"
image Naomi neutral = "images/Naomi neutral.png"
image Kitarou annoyed = "images/Kitarou annoyed.png"
image Naomi excited = "images/Naomi excited.png"

# The game starts here.

label start:
    play music "placeholder_music.wav"

    scene bg black

    "Regret and remorse. They can both come hand in hand as a pair, but that doesnt mean they should."
    "Coincidence and circumstance."
    "Appearing so sudden I swear that I can see flashes of a different life in each one."
    "{i}Pop.{i}"
    "Just like that."
    "Like a bad dream you once had, bursting into reality without your permission."
    "..."
    "...{w}Today is just another day once again.{w}"
    "Even walking the morning steps is just a reminder that I'm walking for someone who isn't here anymore."
    "It's heavy."
    "..."

    "... {w} Why do I hear footsteps?"
    
    "{i}Rapid thuds echo across the house, bringing along someone with rosy cheeks and bubbly attire.{/i}{w=4}{nw}"

    show Naomi excited at center with moveinleft
    omi "{b} Good Morning!!!{/b} How are you, honey?"

    scene bg kitchen

    "{i}Her petite stature peeks through the door frame.{i}"

    show Naomi excited with fade:
        yalign 1

    "Her skittery pace and piercing tone make me flinch in exasperation."
    
    unknown "Don't call me that."

    omi "Darllingg, dont be so harsh! Our names even rhyme. Naoki and Naomi! It's like we were meant to be!"

    nao "How'd you even get in? I'm pretty sure I locked the door last night."

    omi "Oh don't mind that, I just let myself in with the spare key you leave under the rock!"

    nao "Oh… I should change where I hide my spare key better next time."

    omi "So are you ready?"

    nao "...{w}Is Kitaro coming?"

    show Naomi neutral:
        yalign 1

    omi "Im not sure yet. I actually haven't seen him in a while!"

    nao "Well then. Shall we go?"

    show Naomi excited:
        yalign 1

    omi "Yep!"

    jump hospital

label hospital:

    scene bg emergency with fade

    "The car ride on the way there could not have been longer."
    "I'm pretty sure if she had squealed a couple more times I wouldve crashed into the tree myself."
    "Time somehow felt longer as I had to bear with the mobile chatterbox."

    "We parked around the corner of the block and walked towards the entrance of the hospital."
    "We were warmly greeted by the swinging glass doors of the medical instituition."

    scene bg reception with fade

    "It's overwhelming."

    show Naomi neutral:
        yalign 1

    omi "...You look kinda lost."

    omi "Do you know what room she's in?"

    nao "No…"

    omi "Hey, Don’t worry about it! let's just go ask people who work here."

    nao "We just can't ask anyone."

    omi "Lets go find the receptionist then, 'kay?"

    nao "Yeah, ok."

    scene bg hospitalhall

    "{i}Me and Naomi ask the receptionist for the room number of our friend. {/i}"

    "{i}After a bit of back and forth we managed to finally come by the information. {/i}"

    "{i}As we walk down the hallway, we turn quiet for whats about to come.{/i}"

    show Naomi neutral:
        yalign 1

    omi "Nao, still remember the room number?"

    nao "Yeah. It was room number 401."

    nao "...{w}We're here."
    nao "...{w}Are you ok Naomi?"

    omi "Yeah, I'm ok."
    omi "...{w}Are you?"

    hide Naomi neutral

    "..."

    nao "Well, I'll have to be."

    scene bg josie with fade

    "{i}The door welcomes us into a windy room.{/i}" 
    "{i}The curtains by the open window danced around, like frenzied praying to some God for a miracle of some sorts.{/i}"

    "{i}There she was, in the center of the room, with large machines surrounding her.{/i}"

    "{i}She looked like a desecrated mummy wrapped up and held an expressionless gaze against the white wall in front of her.{/i}"
    "{i}Her eyes suddenly jolt from a thousand yard stare towards me and Naomi as we enter.{/i}"

    "..."

    "{i}She suddenly starts flailing with her limbless arms and starts screaming with incorrigible words.{/i}"

    "{i}Josie is disturbed. It's as if she saw a monster and lost all sense of humanity.{/i}"
    "{i}It was like watching a helpless animal begging for its life{/i}."

    "{i}The room is quickly filled with sounds of screaming and wails of pain that reminded me of Ichigo.{/i}"

    show Naomi neutral:
        yalign 1

    omi "Oh my."

    nao "Oh God..."

    hide Naomi neutral

    "{i}Gagging, I turned away. Each second I stood there made it hard to hold in my breakfast.{/i}"

    "{i}My knees felt weak and the world was spinning around violently.{/i}"

    "{i}The nurses rush in and comfort Josie.{/i}"

    "{i}One of them approaches us with eyes of concern. She tells us to come back tomorrow. {/i}"

    "{i}Me and Naomi leave the room in a mess with our backs turned against what was left of my friend.{/i}"

    scene bg hospitalhall

    show Naomi neutral at center with fade:
        yalign 1

    omi "Oh God... why her... What did we do to deserve this?"

    nao "It's... {w} It's all my fault. {w} If I'd never--"

    omi "Shhhh, it's not. Don’t worry about it too much..."

    omi "At least she's still alive."

    hide Naomi neutral

    "{i}I turn to her in anger, voice raised and fists clenched.{/i}"

    nao "AT LEAST?!" 

    nao "LOOK AT HER. SHE CAN'T WALK ANYMORE, LET ALONE TALK TO US."

    "{i}We both stare in silence at the door as the awkwardness creeps in enough for her to make senseless noise again.{/i}"

    show Naomi neutral at center:
        yalign 1

    omi "So, Kitaro didn’t show up huh? Who would've thought! {w} I guess the accident affected that loser more than you."

    nao "...{w}Sure."

    hide Naomi neutral

    "{i}Right then and there, we hear a voice round the corner of the hall. {/i}"

    show Kitarou neutral at left:
        yalign 1

    bad "Heard you two talking about me. What's up?"

    hide Kitarou neutral

    "{i}Speak of the Devil.{/i}"

    show Kitarou neutral at left:
        yalign 1

    bad "What were you saying about me again?"

    show Naomi excited at right:
        yalign 1

    omi "A-About how nice, sweet, and brave you are~ !"

    "{i}Veeeery subtle, Naomi. {/i}"

    bad "...Sure. {w} Anyways..."

    bad "Hey, since I was late and all, wanna get lunch at my place? We'll order food, it's my treat!"

    omi "Ohh, so sorry but I can't! I gotta go now! I have a spa treatment at 2pm!"

# i am disliking kitarou LMAOOO
# "where's my hug" type guy cndsnfsnva

    "{i} His brows furrow at her excuse to absolutely not hang out with him (I don't blame her) and it thoroughly annoys me. {/i}"

    bad "Oh wow okay, So I guess it's like that then."

    nao "Yes, it IS like that, dummy! You certainly look like you could use the spa too though, those legs need waxing!"

    show Naomi excited at right:
        yalign 1

    "{i} Naomi whips around, looking at me without remorse as she leaves me with HIM. {/i}"

    omi "OMG Ok ok so Bye-bye Naoki, see you tomorrow!! {w} MWAH MWAH HUGS AND KISSES XOXOXOOO"

    hide Naomi excited

    "{i} And just like that, she's off to talk someone else's ears off. {/i}"

    bad "I guess it's just you and me then."

    "{i} {w=3}Sh*t. {/i}"

    nao "...{w}Guess so"

    bad "So..."

    "{i} He turns to me expectantly, with a mug only a really specific mother would love. {/i}"

    bad "You free to come over? I'm gonna grab some takeaway steak."

    nao "...Fine"

    scene bg kitchen with fade

    "{i} We take the car to his place and order a steak dinner from Pete's steakhouse on the way. {/i}"

    "{i} Kitaro bragged about everything he bought or flaunted to anyone who was unfortunate enough to listen during the entire car ride. {/i}"

    "{i} I guess I'm now one of those victims. Again.{/i}"

    "{i}We get out of the sports car that he praises so much and into the walkway of his \"two-floor bungalow\". His words, not mine.  {/i}"

    show Kitarou neutral at center:
        yalign 1

    bad "Make yourself at home!"

    nao "...Okay."

    hide Kitarou neutral

    "{i} As I take off my shoes and leave them by the door, Kitaro tries small talk to lighten the mood. {/i}"
    "{i} We continue to catch up as he sets up the table for lunch. {/i}"

    show Kitarou neutral at center:
        yalign 1

    bad "So what have you been up to this past month?"

    nao "I've just been sleeping in from time to time. {w} Trying to... uh, wrap my head around everything."

    bad "Well, just to remind you, I lost my boat during \" everything \", remember? The one with the new paint job?"

    hide Kitarou neutral

    "{i} The boat. {/i}"

    show Kitarou neutral at center:
        yalign 1

    bad "Damn. I still can't believe that Ichigo is gone now. It was so sudden."

    hide Kitarou neutral

    "{i} Ichigo. {/i}"
    "{i} Just hearing her name was enough. {/i}"
    "{i} It sends me spiraling into memories I tried to bury... {w} memories I'd hope to forget along with the pain. {/i}"

    scene bg black

    show Ichigo excited at center

    cute "Hi, Naoki!"

    nao "Ichigo…."

    cute "Do you miss me already?"

    "{i} This... this isn't real... {/i}"

    nao "Why did you leave me…"

    cute "... That ... {w} wasn't my choice to make, dear. "

    "{i} I'm chasing after a breeze, a slight wind that knocked me off my feet whenever she entered the room. It's agony.{/i}"

    nao "BUT-- I'M NOT READY TO LET YOU GO!"

    cute "...Do you think you'll ever be ready?"

    "{i} Her question catches me off guard. It's too soon. Far, far too soon for me to miss her this much.{/i}"

    nao "I-- {w} I don't know."

    cute "When you are, I'll see you in our favorite place, 'kay?"

    hide Ichigo excited

    "{i} Her ghost leaves me in this temporal state of pain, like I'm not even real. She fades away and I'm alone.{/i}"

    "{i} It's like... {w} only I lost something that day.{/i}"

    "{i}I snap back into reality. {/i}"

    scene bg kitchen with fade

    show Kitarou neutral at center:
        yalign 1

    bad "Hey! Earth to Naoki! You still with me buddy?"

    "{i} A few seconds later, I'm back at the dining table facing Kitaro.{/i}"

    show Kitarou annoyed at center:
        yalign 1

    bad "Are you even listening to me? I can't believe I let you into my home, even after the whole damn boat thing!"
    bad "I pay hundreds in insurance, and THIS is how you treat ME?"

    nao "...I'm sorry."

    bad "Yeah, you sure as hell should be."

    bad "If it weren't for you, none of this would've happened. I would have been cruising the TROPICS by now."

    nao "…"

    bad "Let's not forget how boring everything got after."
    bad "I mean look, Naomi tries so hard to put up a front, even with all her stupid appointments!"
    bad "And Josie? Let's be real, she's alive 'cuz her mom owns the hospital."
    bad "I couldn't imagine not being able to drive my car looking like that. Yeesh"
    bad "What's worse, my boat's gone and your chick died on my property! What a load of--"

    "{i} I gripped my fork and knife pointed upward. {w} What the hell? Who the hell says these kinds of things? {/i}"
    "{i} I grit my teeth and glare at him. Enough is enough. {/i}"

    "{i} He stands up from the other end of the table as he sees my anger. {/i}"

    bad "Oh, so now you wanna fight me? In MY own home?"

    hide Kitarou annoyed

    "{i} He chuckles, then says something I couldn't believe. {/i}"

    show Kitarou annoyed at center:
        yalign 1

    bad "Do you know how EASY it was to stage a murder and blame it on some dumbass like you?"


    nao "What {w=3}{nw}the {w=3}{w}hell?"

    hide Kitarou annoyed

    "{i} He drops his grin and replaces it with a sadistic smile. {/i}"

    show Kitarou annoyed at center:
        yalign 1

    bad "I'm glad I killed that whore. I never understood why she would ever pick you over me."

    "{i} I'm going to kill him. {w} I swear, I'll --{/i}"

    bad "So what? What are you gonna do about it now?"
    bad "YOU KNOW WHAT, YOU BOTH SHOULD HAVE DIED THAT DAY, BUT YOU MAKE IT OUT WITH BARELY A SCRATCH LIKE IT'S NOTHING."

    hide Kitarou annoyed

    "{i} I grip the knife that I was just cutting steak with, my knuckles hot-white. {w=4} I lunge at him. {i}"
    "{i} I pounce over the table knocking everything off of it, from the centerpiece to the food we just took a bite of, now in shattered plates on the floor. {/i}"

    "{i} He resists and strikes me in the liver with his fist.{i} Dammit, I forgot he used to do Martial arts. {w} Whatever. I'm armed."

    "{i} I plunge the steak knife deep into the side of his neck with his smug grin as it fades into an annoyed yet sly smirk. {/i}" 

    "{i}Driving my hand repeatedly to do something that feels unjust and unnatural, blood sputters out instead of the screams that would've been. {/i}"

    bad "{b} Gurgled Laughing {/b}"

    "{i} The static ringing from the adrenaline and blinding rage numbs the weight of my actions. {/i}"

    "{i} A flurry of stabs missing the mark of his mouth to keep him from uttering anymore words and plenty to his heart to keep his vile body from doing anymore harm to anyone else. {/i}"

    "{i} It was like my hand was guided to his throat to stop him from sputtering anymore vile things. {/i}"

    "...{w} {i} and I kept going. {/i}"

    "Over. {w}And over. {w}And over. {w}And over. {w}And over. {w}And over. {w}And over. {w}And over. {w}And over. {w}And over."

    "It feels like time stopped."

    "Everything has frozen in place except the blood gurgling from his throat."

    "I got up from the ocean of blood that littered the dining room floor and staggered towards the kitchen sink."

    "I wash my hands of the guilt I have. {w=4} ... {w=4} It won't come off."

    "I just keep washing with soap, with the sponge and with the steel wool. It just won't come off."
    "The blood is gone."
    "But my hands still feel slimy."
    "Its like I'm wearing hands that aren't mine. It feels so sickening, So unnerving."
    "No matter how much I keep scrubbing it wont come off."
    "My skin starts to peel as soon as I start using the steel sponge to clean my hands."

    "I leave."

    "I go home like nothing happened. But I can't sleep. My sins became physical and my moral center fractured."

    "...I still need to talk to Naomi tomorrow." 
    
    "I hope she gets better soon."

    "A sleepless night passes. All that crosses my thoughts are what I'd done. "
    
    "Its all my fault... Why am I still alive?"

    "I hear a knocking on the door this time. It's naomi. Her face looks morose."
    
    "Its like she hasnt gotten any sleep either. Her eyes are puffy and nose riddled with snot bubbles."
    
    show Naomi neutral at center:
        yalign 1

    omi "Naoki..."

    "Her tone seems more sullen than her usual bubbly demeanor."

    nao "Whats wrong?"

    omi "I--It's Kitaro, naoki... He's... he's dead..!"

    omi "WHY... WHY WOULD SOMEONE DO SOMETHING SO HORRIBLE! KITARO WOULDN'T EVEN HURT A FLY!!!"

    "She takes a break from wailing and continues."

    omi "The police said he was riddled with holes... I can't even imagine it without gagging...!"

    "{i} I stare at her blankly. {/i}"

    omi "What's wrong... Why aren't you saying anything?! Kitaro was our friend, and now he's been killed!"
    omi "Come on... Say something please! Please.... All you guys ever do is make me worry.... This is terrible..."

    "{i} She cries and collapses on her knees at the doorstep. {/i}"

    jump ending

#    menu:
#        "Anyways, what do you choose?"
#
#        "Good end!":
#            window hide
#            call minigame from _call_minigame
#
#        "Bad end!":
#            "!! WATCH OUT!"
#            window hide
#            pause 1.0
#            call screen2show
#            jump good_road-

# label good_road:
#     scene bg black
#     "You made the right choice!"
#     return

# label bad_road:
#     scene bg black

#     "You feel yourself losing consciousness... {w=3.0}{nw}"
#     jump ending


