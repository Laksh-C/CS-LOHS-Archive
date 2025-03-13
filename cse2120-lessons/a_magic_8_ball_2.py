# a_magic_8_ball_2.py
'''
title: Magic 8 Ball
author: Laksh Chopra
date-created: 2022/10/04
'''

import random

### --- VARIABLES --- ###
ANSWERS = (
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
)

### --- INTRO --- ###
print("Seek to find the answer in mind.")

### --- INPUTS --- ###
VALUE = input("Think your question and ENTER the 8Ball. (Press the ENTER key to shake the ball): ")

### --- PROCESSING --- ***
ANSWER = random.randrange(len(ANSWERS)) #any integer from 0 to length of ANSWERS (0-19)

### --- OUTPUTS --- ###
print(ANSWERS[ANSWER])
