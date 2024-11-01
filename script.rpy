# Define Characters with Colors and Styles
define walid = Character("Walid", color="#5DADE2")
define amal = Character("Amal", color="#F7DC6F")
define layla = Character("Layla", color="#A569BD")
define owner = Character("Baker", color="#318215")
define soldier = Character("Soldier", color= "#88100a")
define rami = Character("Rami", color= "#830d9d")
define man = Character("Man", color="#bbbbbb")
default avoid_alley = False
default fear_meter = 0
# Start of the Game Script
label start:
    scene bg_walid_home_morning
    with dissolve

    # Initial description of the scene
    "Layla, Walid and Amal's mother, hands them their school supplies. The atmosphere is tense, and she looks at her children with worry."

    # Dialogue
    layla "Remember to keep Amal close. And don’t talk to anyone at the checkpoints."

    walid "I will, Mama."

    layla "And if things get... difficult, remember that it’s okay to turn back. Your safety matters more."

    # Narrative action
    "She looks away, worry etched across her face."

    # Amal's gesture
    "Walid glances at Amal, who looks up, holding his hand tightly."

    layla "Please Walid, if things get bad… come back home. Amal’s still young. School isn’t worth your safety."

    walid "Yes, yes Mama, I know. You don't have to tell us every day."

    # Layla's response
    layla "I know I can be annoying, but I won't apologize. I love you, habibati. I hope you have a somewhat tranquil day."

    # Walid to Amal
    walid "We’ll make it to school, okay? I promise. Just stay close."

    # Walid's gesture and exit
    "Walid looks up and stiffens his upper lip, eyes sunken and heavy with responsibility. He puts on his best smile, looks towards his mother, and says:"

    walid "Bye Mama! Have a great day!"

    # Transition to the next scene
    "Walid opens the door, holding Amal's hand, ready to face whatever the day has for him."
    
    # Jump to the next scene
    jump walking_1

label walking_1:
    scene bg_west_bank_morning
    with dissolve

    # Description of the setting
    "Walid and Amal have left their house and are on their way to school. They come across a fork in the road."

    # Walid's internal monologue
    walid "(Hmm. I know we shouldn't waste time walking to school; it already takes us forever to get there.)"
    walid "(But I also know Amal hasn't had a full breakfast yet, and unlike me, she can't hold her hunger.)"

    # Choice for Walid
    menu:
        "Suggest getting a manouche":
            walid "What do you say, Ammoul? Feel like a manouche for our recess?"

            amal "Yes! I'll have half now and half later because I'm starving!"

            "Walid lets off a short breathy laugh, half amused by his sister and half relieved. He is also quite hungry."
            walid "Let's go then. *Yalla*, quickly, so we don't waste much time."

            # Transition to the next label
            jump man2ouche

        "Go directly to the checkpoint":
            amal "I know we don't have much time today, but I was kind of hoping to grab something to eat..."

            walid "Sorry, Ammoul. I know you're hungry, but the longer we take, the harder it'll be to get there. I'll get you two things from the store on the way back, I promise."

            amal "You know I'm holding you to that, right? And if you don't, I'm telling Mama and Baba that you liiiiiied!"

            # Nested choice after response
            menu:
                "Reassure her with a promise":
                    walid "I said I promised, didn't I?!"

                    amal "Okay okay, I believe you. You don't need to be so mean to me."

                    # Narrative action
                    "Amal lets go of Walid's hand in a show of independence. Walid lets her, but keeps a close eye on her."

                    # Transition to the checkpoint scene
                    jump chek_1

                "Change your mind and turn back toward the left":
                    walid "Ugh, fine, you win. Let's go now, but we need to be quick, Ammoul, okay?"

                    amal "YAY! Yes yes yes, super fast!"

                    # Transition to man2ouche
                    jump man2ouche

# Placeholder labels for next scenes
label man2ouche:
    # Code for the manouche scene goes here
    scene bg_bakery_morning
    with dissolve

    # Description of the setting
    "Walid and Amal reach the corner store bakery. The smell of fresh dough and thyme baking in the oven is overpowering, yet welcoming and comforting nonetheless. The store owner has his back turned to them, focused on the manakeesh baking."

    # Dialogue with the store owner
    walid "Sabah al kheir, Ammo. Can we get two?"

    "The owner quickly turns around to see who spoke. His face is sweaty and red, probably from being so close to the oven all day."

    owner "*Sabah al kheir* young ones! Would you like them with thyme, cheese, or both?"

    "Walid looks down towards Amal, who is already looking up at him, expecting him to know her choice."

    walid "We'll take one with thyme, and another..."

    # Decision point for choosing the second manouche
    menu:
        "With cheese":
            "Amal looks at you, confused."

            amal "I thought you said that cheese gives you an upset stomach? Maybe today isn't the day to risk it, but hey, it's your life."
            walid "Ah, maybe you're right. Make that two with thyme Ammo"
            owner "You got it."
            amal "Could I also get a juice?"
            menu:
                "Sure, can we get one juice as well, Uncle?":
                    owner "Of course. Here you go, 12 Shekels please."

                    "Walid hands him the money."

                    owner "May you go with peace!"

                    walid "Peace to you as well, uncle."

                "I don't really have enough, Ammoul, and Mama said I always need to keep some money on us in the case of an emergency.":
                    amal "Yeah, you're right. Anyway, maybe if we save enough, we can take a taxi back from school one day like we always say!"

            # Conclude transaction with two thyme
            "The owner presents a plastic white bag with two folded flatbreads inside, wrapped in paper."
            
            owner "I'll need 9 Shekels from you, sir."

            "Walid pulls out the money and bids the man farewell."

            owner "May you go with peace!"

            walid "Peace to you as well, uncle."


        "With both":
            "Amal looks at you, confused."

            amal "I'm assuming that one's yours, right? I don't like them mixed, Walid, you know that."
            walid "Um, sure."
            amal "Could I also get a juice?"
            menu:
                "Sure, can we get one juice as well, Uncle?":
                    owner "Of course. Here you go, 12 Shekels please."

                    "Walid hands him the money."

                    owner "May you go with peace!"

                    walid "Peace to you as well, uncle."

                "I don't really have enough, Ammoul, and Mama said I always need to keep some money on us in the case of an emergency.":
                    amal "Yeah, you're right. Anyway, maybe if we save enough, we can take a taxi back from school one day like we always say!"

            # Conclude transaction with two thyme
            "The owner presents a plastic white bag with two folded flatbreads inside, wrapped in paper."
            
            owner "I'll need 9 Shekels from you, sir."

            "Walid pulls out the money and bids the man farewell."

            owner "May you go with peace!"

            walid "Peace to you as well, uncle."

        "Two thyme":
            "Amal looks at you, excited and asks:"

            amal "Could I also get a juice?"

            # Decision point for getting juice
            menu:
                "Sure, can we get one juice as well, Uncle?":
                    owner "Of course. Here you go, 12 Shekels please."

                    "Walid hands him the money."

                    owner "May you go with peace!"

                    walid "Peace to you as well, uncle."

                "I don't really have enough, Ammoul, and Mama said I always need to keep some money on us in the case of an emergency.":
                    amal "Yeah, you're right. Anyway, maybe if we save enough, we can take a taxi back from school one day like we always say!"

            # Conclude transaction with two thyme
            "The owner presents a plastic white bag with two folded flatbreads inside, wrapped in paper."

            owner "I'll need 9 Shekels from you, sir."

            "Walid pulls out the money and bids the man farewell."

            owner "May you go with peace!"

            walid "Peace to you as well, uncle."

    # Move on to the next checkpoint
    jump chek_1
    

label chek_1:
    # Code for the first checkpoint scene goes here
    scene bg_checkpoint_morning
    with dissolve

    # Description of the setting
    "Walid and Amal reach a long line of people at a checkpoint. Israeli soldiers stand, weapons slung over their shoulders, surveying the crowd. Every soul within a 500-meter radius is tense."

    # Dialogue with Amal
    amal "I really hope they don't make us wait too long today; there are already so many more people than usual."

    # Decision point to reassure Amal or change the subject
    menu:
        "Reassure Amal":
            walid "Look at me, do I seem worried?"

            amal "No, but you never do! So that doesn't count."

            "Walid smirks at Amal and ruffles her hair, trying to lighten the mood."

            walid "(When I was her age, that would've been comforting. Amal is smarter than I was, and more aware, especially ever since the situation in Gaza started more than a year ago.)"
        
        "Change the subject":
            walid "Are you excited for school today? I know you have science classes on Mondays."

            amal "Super excited! We're learning about different types of animals. Did you know that the mountain gazelle is our national animal? We don't see them in the city, apparently they mostly live somewhere in the south."

            walid "No, I actually didn't. That's pretty interesting. They must be pretty resilient to be able to live in such dry places."

            amal "Right?! I think the teacher called them Gazelle gazelle... or was it Gazella gazella? Gazello gazelli? Anyway, they also wake up at dawn, just like us! I bet *they* aren't forced to go through checkpoints to get to school..."

    # Soldier interrupts
    soldier "Next!"

    "Walid steps forward with Amal, holding her hand. A soldier approaches them, looking at them sternly."

    soldier "Papers."

    "Walid hands over the papers, trying not to look nervous. Amal clutches his arm."

    # Decision point to comply, ask how long, or lighten the mood
    menu:
        "Comply without speaking":
            "The soldier inspects their papers and then waves them through without incident."
            soldier "Go on. Next!"
            jump walking_2

        "Ask how long it will take":
            "The soldier narrows his eyes, visibly annoyed."
            soldier "It’ll take as long as I say. You got somewhere better to be?"
            "The soldier looks at Walid suspiciously, then lets them pass."
            jump walking_2

        "Try and lighten the mood":
            walid "Shalom aalaykum, officer. It's a nice day today, no?"

            "Amal tugs on Walid’s arm, looking uneasy. The soldier barks at them."

            soldier "You think this is a joke? Are you a funny guy? You think you're Bassem Youssef? Get back in line or don’t pass at all."

            walid "Sorry sir, I meant no disrespect, but it's our turn now. How far back do I need to go?"

            soldier "Does it look like I care?"
            $ fear_meter += 1  # Increase fear for this choice
            

            # Nested Decision: Try to find a new place in line or find an alley to slip through
            menu:
                "Try to find a new place in line":
                    "After carefully weighing his options, Walid decides to find another place in line farther back."
                    "He and Amal walk back parallel to the line they've been waiting in for almost an hour now, each step feeling like it’s destined to prolong their journey to school."
                    "Suddenly, an arm reaches out of the line and grabs him by the shoulder."

                    walid "Who's touching-"

                    "Walid looks up to see a familiar face in a sea of desperation."

                    amal "Ammo Rami!"

                    rami "Kiddos! It's great to see you. Where are you going? Don't tell me they didn’t let you pass again?!"

                    walid "No, not this time. I got us sent back to the end of the line."

                    amal "He was being a kiss-up, and now I'm going to miss my first class."

                    rami "Those... I better not say. Come, kids, take my place in line."

                    walid "Really, Ammo Rami? You’d do that for us? Don’t you need to get to work?"

                    rami "Don't worry about it! That’s what Ammos are for. Here, come stand in front of me."

                    "As they scoot in front of Rami, a man behind them shouts out:"

                    man "Hey! That’s not fair! I’ve been waiting here for almost an hour."

                    "Walid and Amal stay silent, feeling guiltly and embarrassed."

                    rami "Ah, shut up. They’re with me. Besides, can’t you see their backpacks? They’re just trying to get to school."

                    "The man mutters under his breath but concedes, perhaps not wanting to prevent children from reaching school."

                    "Rami turns back to the kids, softly."

                    rami "Don't mind him; he's probably trying to get to work, just like me."

                    "They continue conversing, and time seems to pass faster. Finally, they reach the checkpoint again."

                    soldier "Papers- Oh. It’s you two again. Finally made it back, I see?"

                    rami "Us three, actually. I'm crossing with them."

                    soldier "Ah. Well, in that case, you two, hand over your papers."

                    "Walid and Amal rummage through their backpacks for their crossing permits as the soldier signals to two other guards to come closer."

                    soldier "You two kids, go ahead and pass. Now."

                    walid "But Ammo Rami-"

                    rami "It’s alright, guys. Go on ahead and have a great day at school!"

                    "Walid and Amal move on as Rami continues to be harassed, the contents of his briefcase strewn across the filthy pavement."

                    jump walking_2

                "Find an alley to slip away through":
                    walid "I think we should try and go through that alley over there. It'll probably save us some time since we’d have to go back to the start of the line."

                    amal "If you think so. I've never been through there without Mama and Baba, so it’s up to you. Do you know the way?"

                    # Final Decision: Go forward or return to the line
                    menu:
                        "Go forward":
                            walid "I'm pretty sure. Come now, let's not waste more time."

                            $ fear_meter += 1  # Increase fear for this choice
                            

                            jump alley

                        "Return to the line":
                            $ avoid_alley = True  # Set variable to remember this choice
                            jump find_place_in_line  # Jump directly to the line scene

label find_place_in_line:
    if avoid_alley:
        "Walid decides to avoid the alley and looks for a place in line with Amal by his side."
    else:
        "They return to the line and look for a new place to wait."

    # Continue the scene with Ammo Rami
    "He and Amal walk back parallel to the line they've been waiting in for almost an hour now, each step feeling like it’s destined to prolong their journey to school."
    "Suddenly, an arm reaches out of the line and grabs him by the shoulder."

    walid "Who's touching-"

    "Walid looks up to see a familiar face in a sea of desperation."

    amal "Ammo Rami!"

    rami "Kiddos! It's great to see you. Where are you going? Don't tell me they didn’t let you pass again?!"

    walid "No, not this time. I got us sent back to the end of the line."

    amal "He was being a kiss-up, and now I'm going to miss my first class."

    rami "Those... I better not say. Come, kids, take my place in line."

    walid "Really, Ammo Rami? You’d do that for us? Don’t you need to get to work?"

    rami "Don't worry about it! That’s what Ammos are for. Here, come stand in front of me."

    "As they scoot in front of Rami, a man behind them shouts out:"

    man "Hey! That’s not fair! I’ve been waiting here for almost an hour."

    "Walid and Amal stay silent, feeling both guilty and embarrassed."

    rami "Ah, shut up. They’re with me. Besides, can’t you see their backpacks? They’re just trying to get to school."

    "The man mutters under his breath but concedes, perhaps not wanting to prevent children from reaching school."

    "Rami turns back to the kids, softly."

    rami "Don't mind him; he's probably trying to get to work, just like me."

    "They continue conversing, and time seems to pass faster. Finally, they reach the checkpoint again."

    soldier "Papers- Oh. It’s you two again. Finally made it back, I see?"

    rami "Us three, actually. I'm crossing with them."

    soldier "Ah. Well, in that case, you two, hand over your papers."

    "Walid and Amal rummage through their backpacks for their crossing permits as the soldier signals to two other guards to come closer."

    soldier "You two kids, go ahead and pass. Now."

    walid "But Ammo Rami-"

    rami "It’s alright, guys. Go on ahead and have a great day at school!"

    "Walid and Amal move on as Rami continues to be harassed, the contents of his briefcase strewn across the filthy pavement."
    
    $ fear_meter += 1  # Increase fear for this choice
    

    jump walking_2