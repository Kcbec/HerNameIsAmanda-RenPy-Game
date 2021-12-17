label Chapter_1:



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/bensound-extremeaction.mp3" fadein 1.0
    scene Old_KitchenB with fade_Hard

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show Amanda_Neutral_3 at right
    a "Hey there."
    play sound confirm
    show Amanda_Neutral at right
    a "I'm Amanda."
    play sound confirm
    show Amanda_Neutral_2 at right
    $ player_name = renpy.input("What do you want me to call you?")
    play sound confirm

    $ player_name = player_name.strip()

    if player_name == "":
        $player_name = "Asshat"
        a "If you're going to ignore me then I'll just call you Asshat."
        play sound confirm

    show Amanda_Neutral at right
    a "Alright %(player_name)s, what is 1,440 divided by 6?"
    play sound confirm

    $ u = player_name


label menu1:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'
    show screen countdown
    menu:
        "320":
            hide screen countdown
            a "Wrong."
            play sound confirm
            jump menu1_end
        "240":
            hide screen countdown
            a "That was an easy one."
            play sound confirm
            jump menu1_end
        "280":
            hide screen countdown

            a "Wrong."
            play sound confirm
label menu1_slow:
    show Amanda_Annoyed at right

    a "It's not that hard...."
    play sound confirm
label menu1_end:
    show Amanda_Smiling at right
    a "I'm just trying to get an idea of what I'm working with here."
    show Amanda_Smiling_2 at right


default menuset = set()

menu chapter_1_places:
    set menuset
    a "You ready start?"

    "Yes":
        jump Chapter_2
        play sound confirm
    "No":
        jump Chapter_2
        play sound confirm
