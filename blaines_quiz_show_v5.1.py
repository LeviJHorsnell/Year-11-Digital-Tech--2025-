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
    