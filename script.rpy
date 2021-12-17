init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]

    $ timer_range = 0
    $ timer_jump = 0

# Amanda
image Amanda_Angry = "Amanda_Angry.png"
image Amanda_Annoyed = "Amanda_Annoyed.png"
image Amanda_Annoyed_2 = "Amanda_Annoyed_2.png"
image Amanda_Neutral = "Amanda_Neutral.png"
image Amanda_Neutral_2 = "Amanda_Neutral_2.png"
image Amanda_Neutral_3 = "Amanda_Neutral_3.png"
image Amanda_Sad = "Amanda_Sad.png"
image Amanda_Sad_2 = "Amanda_Sad_2.png"
image Amanda_Smiling = "Amanda_Smiling.png"
image Amanda_Smiling_2 = "Amanda_Smiling_2.png"
image Amanda_Pop_Art = "Amanda_Pop_Art.png"
image Amanda_Trippy = "Amanda_Trippy.png"
image Amanda_Close = "Amanda_close.png"

define a = Character("Amanda")

# Backgrounds
image School = "Old_School.png"
image Outdoor_Stairs = "Outdoor_Stairs.png"
image Old_KitchenB = "Old_KitchenB.png"
image Laundromat = "Laundromat.png"
image Laundromat_Trippy = "Laundromat_Trippy.png"
image Kitchen_Edit_1 = "Kitchen_Edit_1.png"
image Kitchen_Edit_2 = "Kitchen Edit_2.png"

# Banners
image Story_1_Banner ="story_1 banner.png"
# Music
define audio.deepblue = "bensound-deepblue.mp3"
define audio.extremeaction = "audio/bensound-extremeaction.mp3"
# Sound Effects
define audio.alarm = "Alarm.wav"
define audio.confirm = "audio/Confirm.ogg"

# Animations that will likely be a larger headache than they're worth
# But that's Hollywood baby.
image animated frames:
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2
    "Laundromat.png"
    pause 0.2
    "Laundromat_Trippy.png"
    pause 0.2

define fade = Fade(1.0, 0.0, 1.0)
define fade_Hard = Fade(0.5, 2.0, 0.5)



# The game starts here.
label start:

    $ Negative_Points = 0
    $ Positive_Points = 0
    $ Critical_Points = 0



transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

jump Chapter_1
