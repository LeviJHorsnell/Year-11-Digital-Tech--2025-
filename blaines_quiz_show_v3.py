import easygui
import random
answer1="No"
score=0
age=easygui.integerbox("Hello there! Welcome to Blaine's Quiz Show! Please enter your age")
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
    easygui.msgbox("You have 10 questions to answer. Every correct answer will give you one point, while every wrong answer will deduct a point. Good luck!")
list_q=["Pikachu", "Digglet", "Ho-oh", "Emboar", "Beedrill", "Vileplume", "Happiny", "Arceus", "Hawlucha", "Porygon"]
list_a=["Volt tackle", "Fissure", "Sacred fire", "Heat crash", "Twineedle", "Petal dance", "Soft-Boiled", "Judgement", "Flying press", "Conversion"]

