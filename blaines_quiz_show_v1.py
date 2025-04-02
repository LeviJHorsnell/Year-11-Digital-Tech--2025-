import easygui
import random
answer1="No"
age=easygui.integerbox("Hello there! Welcome to Blaine's Quiz Show! Please enter your age")
if age <15:
    easygui.msgbox("You are too young to play in the quiz show")

if answer1 == "No":
    easygui.msgbox("Farewell!")
if age >15:
    easygui.msgbox("You are old enough to play in the quiz show")
    answer1=easygui.buttonbox("Would you like to continue?", choices=["Yes", "No"])
if age == 15:
    easygui.msgbox("You are old enough to play in the quiz show")
    answer1=easygui.buttonbox("Would you like to continue?", choices=["Yes", "No"])
if age >18:
    easygui.msgbox("You are too old to play in the quiz show")
while answer1 == "Yes":
    easygui.msgbox("You have to get 10 questions correct to win. Good luck!")
    question=[""]
    answer="Yes"

