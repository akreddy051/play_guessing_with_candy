import sys
import text_to_speech as speech
from random import randint
answer=randint(1,10)
speech.speak('Hi! this is candy. your game assistant. I will guess a number between 1 and 10 . if you guess the number correctly, you will win','en')

while True:
    try:
        print(answer)
        speech.speak('enter your guess','en')
        guess = int(input('enter your guess: '))

        if 0 < guess < 11:
            if guess==answer:
                speech.speak('wow! your guess was correct. you won! congrats!', 'en')
                break
            else:
                speech.speak('sorry! your guess is wrong. try again', 'en')
                continue
        else:
            speech.speak('please enter a number between 1 and 10', 'en')
            continue
    except ValueError:
        speech.speak('please enter a number!  not text!', 'en')
