import easygui
import random
answer1="No"
score=(0)
list_q=["Pikachu?", "Digglet?", "Ho-oh?", "Emboar?", "Beedrill?", "Vileplume?", "Happiny?", "Arceus?", "Hawlucha?", "Porygon?"]
list_a=["Volt tackle", "Fissure", "Sacred fire", "Heat crash", "Twineedle", "Petal dance", "Soft-Boiled", "Judgement", "Flying press", "Conversion"]
name=easygui.enterbox("Hello there! Welcome to Blaine's Quiz Show! Please enter your name")
age=easygui.integerbox(name + "... what a fantastic name! Please enter your age")
if age <15:
    easygui.msgbox("You are too young to play in the quiz show")
    easygui.msgbox("Farewell!")
if age == 15:
    easygui.msgbox("You are old enough to play in the quiz show")
    answer1=easygui.buttonbox("Would you like to continue?", choices=["Yes", "No"])
    if answer1 == "No":
        easygui.msgbox("Farewell!")
if age == 16:
    easygui.msgbox("You are old enough to play in the quiz show")
    answer1=easygui.buttonbox("Would you like to continue?", choices=["Yes", "No"])
    if answer1 == "No":
        easygui.msgbox("Farewell!")
if age == 17:
    easygui.msgbox("You are old enough to play in the quiz show")
    answer1=easygui.buttonbox("Would you like to continue?", choices=["Yes", "No"])
    if answer1 == "No":
        easygui.msgbox("Farewell!")
if age == 18:
    easygui.msgbox("You are old enough to play in the quiz show")
    answer1=easygui.buttonbox("Would you like to continue?", choices=["Yes", "No"])
    if answer1 == "No":
        easygui.msgbox("Farewell!")
if age >18:
    easygui.msgbox("You are too old to play in the quiz show")
    easygui.msgbox("Farewell!")
if answer1 == "Yes":
    easygui.msgbox("You have 10 questions to answer. Every correct answer will give you one point, while every wrong answer will deduct a point. Good luck " + name + "!")
    easygui.msgbox("Question 1")
    answer=easygui.buttonbox("Which of these moves is exclusive to " + list_q[0], choices=["Electrify", "Zing zap", list_a[0], "Techno blast"])
    if answer == list_a[0]:
        if name == "kp":
            score += 2
        else:
            score +=1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 2")
    answer2=easygui.buttonbox("Which of these moves is exclusive to " + list_q[1], choices=["Dig", list_a[1], "Rock slide", "Rock tomb"])
    if answer2 == list_a[1]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 3")
    answer3=easygui.buttonbox("Which of these moves is exclusive to " + list_q[2], choices=[list_a[2], "Fire blast", "Incinerate", "Heat wave"])
    if answer3 == list_a[2]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 4")
    answer4=easygui.buttonbox("Which of these moves is exclusive to " + list_q[3], choices=["Flamethrower", list_a[3], "Fire lash", "Searing shot"])
    if answer4 == list_a[3]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 5")
    answer5=easygui.buttonbox("Which of these moves is exclusive to " + list_q[4], choices=["Fell stinger", "Infestation", "Savage spin-out", list_a[4]])
    if answer5 == list_a[4]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 6")
    answer6=easygui.buttonbox("Which of these moves is exclusive to " + list_q[5], choices=["Flower trick", list_a[5], "Grassy terrain", "Worry seed"])
    if answer6 == list_a[5]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 7")
    answer7=easygui.buttonbox("Which of these moves is exclusive to " + list_q[6], choices=["Minimize", "Pulverizing pancake", list_a[6], "Me first"])
    if answer7 == list_a[6]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 8")
    answer8=easygui.buttonbox("Which of these moves is exclusive to " + list_q[7], choices=["Mirror shot", "Sunsteel strike", "Doom desire", list_a[7]])
    if answer8 == list_a[7]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 9")
    answer9=easygui.buttonbox("Which of these moves is exclusive to " + list_q[8], choices=[list_a[8], "Quick guard", "Max knuckle", "Brave bird"])
    if answer9 == list_a[8]:
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("Question 10")
    answer10=easygui.buttonbox("Which of these moves is exclusive to " + list_q[9], choices=["Signal beam", list_a[9], "Conversion 2", "Magnet rise"])
    if answer10 == list_a[9] or "Conversion 2":
        if name == "kp":
            score += 2
        else:
            score += 1
        easygui.msgbox(f"Correct! Your score is now {score}")
    else:
        score -= 1
        if score <0:
            score=0
        easygui.msgbox(f"Incorrect! Your score is now {score}")
    easygui.msgbox("There you go! That's all 10 questions! Let's see how well you did!")
if score == 0 or 1 or 2 or 3:
    easygui.msgbox("You need to back to Pokemon School bud! Your score was " + str(score))
if score == 4 or 5 or 6:
    easygui.msgbox("You did well " + name + "! Your score was " + str(score))
if score == 7 or 8 or 9:
    easygui.msgbox(name + ", you did very well on this test! Your score was " + (score))
