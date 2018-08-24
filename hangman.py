from turtle import *
def head():
    setheading(180)
    circle(10, 360)
def body():
    up()
    setheading(-90)
    fd(20)
    down()
    fd(50)
def leg1():
    setheading(290)
    fd(50)
    rt(180)
    fd(50)
def leg2():
    setheading(250)
    fd(50)
    rt(180)
    fd(50)
def arm1():
    up()
    setheading(90)
    fd(35)
    down()
    setheading(300)
    fd(30)
    rt(180)
    fd(30)
def arm2():
    setheading(240)
    fd(30)
    rt(180)
    fd(30)
draw = [head, body, leg1, leg2, arm1, arm2]
index = 0
array = []
print('welcome to hangman')
word = "secret"
while True:
    playerMode = input("How many players(1 or 2): ")
    try:
        playerMode = int(playerMode)
        if not(playerMode == 1 or playerMode == 2):
            print("Number is too big!")
        else:
            break
    except ValueError:
        print("not a number")
if playerMode == 2:
    word = input("Player One: Choose a word, Player Two: No Peeking!")
    print("\n" * 100)
up()
ht()
speed(0)
goto(-100, 0)
down()
lt(90)
fd(200)
rt(90)
fd(50)
rt(90)
fd(50)
lives = 6
correct = False
letters = 0
for x in word:
    print('_', end=" ")
while lives > 0:
    while True:
        guess = input("\nGuess a letter: ")
        correct = False
        if not len(guess) == 1:
            print("not a letter! ")
        else:
            break
    y = ''
    for x in word:
        for i in array:
            if i == x:
                y = i
                print(x, end=" ")
        if x == guess:
            print(x, end=" ")
            correct = True
            letters = letters + 1
        elif y != x:
            print('_', end=" ")
    if letters == len(word):
        print("You got the word!")
        break
    if correct:
        array.append(guess)
    if not correct:
        print("\nWRONG!")
        lives = lives-1
        draw[index]()
        index = index + 1
        if lives == 0:
            print("You Lose")
            print("The word was " + word)
            break
    print("\n" + str(lives) + " guesses left")
