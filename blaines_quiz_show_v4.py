import easygui
import random
answer1="No"
back="OK"
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
    while back == "OK":
        answer=easygui.buttonbox("Which of these moves is exclusive to " + list_q[0], choices=["Electrify", "Zing zap", list_a[0], "Techno blast"])
        if answer == list_a[0]:
            score =+ 1
            easygui.msgbox(f"Correct! Your score is now {score}")
        else:
            score =- 1
            if score <0:
                score=0
            back=easygui.buttonbox(f"Incorrect! Try again. Your score is now {score}", choices=["OK"])
        answer2=easygui.buttonbox("Which of these moves is exclusive to " + list_q[1], choices=["Dig", list_a[1], "Rock slide", "Rock tomb"])
        if answer2 == list_a[1]:
            score =+ 1
            easygui.msgbox(f"Correct! Your score is now {score}")
        else:
            score =- 1
            if score <0:
                score=0
            back=easygui.buttonbox(f"Incorrect! Try again. Your score is now {score}", choices=["OK"])   