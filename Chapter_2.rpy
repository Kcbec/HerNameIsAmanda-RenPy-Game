label Chapter_2:
scene Laundromat
show Amanda_Neutral
a "So, I'm going to ask you a few questions."
play sound confirm
hide Amanda_Neutral
scene animated frames
show Amanda_Close
a "Answer them truthfully %(player_name)s."
play sound confirm
scene Laundromat
hide Amanda_Close
show Amanda_Smiling_2
a "Okay, think of an open field."
play sound confirm
show Amanda_Smiling
a "How would you describe the field you're thinking of?"
label menu2:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu2_slow'
    show screen countdown
    menu:
        "Dry and Dead":
            hide screen countdown
            a "Gross."
            play sound confirm
            $ Negative_Points += 1
            jump menu2_end
        "Grassy and Healthy":
            hide screen countdown
            a "Hm."
            play sound confirm
            $ Positive_Points += 1
            jump menu2_end
        "Well-Trimmed":
            hide screen countdown
            $ Critical_Points += 1
            a "Sure."
            play sound confirm
            jump menu2_end

label menu2_slow:
    show Amanda_Annoyed
    $ responsive_points -=1
    a "Sorry, I didn't realize open fields analytics would stump you so easily. Lets move on"
    play sound confirm

label menu2_end:
    show Amanda_Smiling
    a "Great. Moving on"
    show Amanda_Smiling_2
    play sound confirm

show Amanda_Neutral
a "Think of a horse."
play sound confirm
show Amanda_Neutral_2
a "I can give you time to Google if you're unfamiliar with what a horse looks like."
play sound confirm
show Amanda_Smiling
a "Great. What color is the horse you're thinking of?"

label menu3:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu3_slow'
    show screen countdown
    menu:
        "Brown":
            hide screen countdown
            a "Another wrong answer."
            play sound confirm
            $ Positive_Points += 1
            jump menu3_end
        "Black":
            hide screen countdown
            show Amanda_Annoyed
            a "That is not one of the options."
            play sound confirm
            $ Negative_Points += 1
            jump menu3_end
        "White":
            hide screen countdown
            $ Critical_Points += 1
            hide Amanda_Smiling
            scene animated frames
            show Amanda_Close
            a "I told you to answer truthfully %(player_name)s."
            play sound confirm
            jump menu3_end

label menu3_slow:
    show Amanda_Annoyed
    a "I'm not explaining colors to you. Moving on."
    play sound confirm

label menu3_end:
    scene Laundromat
    show Amanda_Smiling
    a "Joking."
    play sound confirm


show Amanda_Neutral_2
$ player_goal = renpy.input("What do you hope to get out of this game?")

$ player_goal = player_goal.strip()

if player_goal == "Love":
    a "Love? From a video game?"
    play sound confirm
if player_goal == "love":
    a "Love? From a video game?"
    play sound confirm
if player_goal == "Sex":
    a "That's not happening, pervert."
    play sound confirm
if player_goal == "sex":
    a "That's not happening, pervert."
    play sound confirm
if player_goal == "Fuck you":
    a "What is wrong with you? I'm not real, you creep."
    play sound confirm
if player_goal == "fuck you":
    a "What is wrong with you? I'm not real, you creep."
    play sound confirm
if player_goal == "I want to fuck you":
    a "What is wrong with you? I'm not real, you creep."
    play sound confirm
if player_goal == "I wanna to fuck you":
    a "What is wrong with you? I'm not real, you creep."
    play sound confirm
else:
    a "Most of us cannot determine the difference between hopes and expectations."
    play sound confirm

a "Think of a storm"
play sound confirm
a "How far away is this storm. Is it close? Is it a big storm? Is it right above you?"
play sound confirm
a "Is it just passing through or is it here to stay?"
play sound confirm
label menu4:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu4_slow'
    show screen countdown
    menu:
        "It's right above me.":
            $ Negative_Points += 1
            hide screen countdown
            a "Then don't look up."
            play sound confirm
            jump menu4_end
        "It's nothing. It'll pass.":
            $ Positive_Points += 1
            hide screen countdown
            a "Fingers crossed."
            play sound confirm
            jump menu4_end
        "It's far away.":
            $ Positive_Points += 1
            hide screen countdown
            a "I'm sure it is."
            play sound confirm
            jump menu4_end
        "The storm is massive.":
            $ Critical_Points += 1
            hide screen countdown
            a "That it is."
            play sound confirm
            jump menu4_end

label menu4_slow:
    show Amanda_Annoyed
    $ Negative_Points -= 1
    a "If you cannot stop it, then why think about it?."
    play sound confirm

label menu4_end:
    show Amanda_Smiling
    a "All done."
    play sound confirm
    show Amanda_Smiling_2
    a "Now lets see..."
    play sound confirm

if Positive_Points > max(Negative_Points, Critical_Points):
    a "You have a good attitude."
    play sound confirm
    show Amanda_Smiling_2
    a "That makes me question your honesty."
    jump Chapter_3_a
elif Negative_Points > max(Positive_Points, Critical_Points):
    a "You're kind of downer, dude."
elif Critical_Points > max(Positive_Points, Negative_Points):
    a "You need to learn to relax."












return
