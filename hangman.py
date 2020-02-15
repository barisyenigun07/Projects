words = ["ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra","cougar",
       "coyote","crow","deer","dog","donkey","duck","eagle","ferret","fox","frog","goat","goose","hawk",
       "lion","lizard","llama","mole","monkey","moose","mouse","mule","newt","otter","owl","panda",
       "parrot","pigeon","python","rabbit","ram","rat","raven","rhino","salmon","seal","shark","sheep"
       "skunk","sloth","snake","spider","stork","swan","tiger","toad","trout","turkey","turtle",
       "weasel","whale","wolf","wombat","zebra"]
letters = "abcdefghijklmnopqrstuvwxyz"
let = []
lives = 10
import random

def pickWord(words):
    word = random.choice(words)
    return word
def pickLetter(letters):
    letter = input("Enter a letter:")
    if letter not in letters:
        print("There is not a letter like that!")
    elif letter in let:
        print("You entered a letter like that!")
    else:
        let.append(letter)
        return letter
def checkLetter(letter,word):
    locs = []
    for i in range(len(word)):
        if letter == word[i]:
            locs.append(i)
    return locs
def parseGame(word):
    game = {}
    for i in range(len(word)):
        game[i] = "_"
    return game
def updateGame(lst,letter,game):
    if lst != []:
        for i in lst:
            game[i] = letter
        return game
    else:
        print("There is not a letter like that in the word!")
        return game
word = pickWord(words)
name = input("Enter your name:")
print("Hi {}! Welcome to Hangman Game!".format(name))
for i in parseGame(word).values():
    print(i,end=" ")
print()
print("You have {} lives {}!".format(lives,name))
letter = pickLetter(letters)
locs = checkLetter(letter,word)
if locs == []:
    lives -= 1
up_game = updateGame(locs,letter,parseGame(word))
for i in up_game.values():
    print(i,end=" ")
print()
print("You have {} lives!".format(lives))
while True:
    print()
    let1 = pickLetter(letters)
    locs1 = checkLetter(let1,word)
    if locs1 == []:
        lives -= 1
    up_game1 = updateGame(locs1,let1,up_game)
    for i in up_game1.values():
        print(i,end=" ")
    print()
    print("You have {} lives!".format(lives))
    if "_" not in up_game1.values():
        print()
        print("Congrats {}! You won!".format(name))
        break
    if lives == 0:
        print("Game over!")
        print("The word was",word)
        break
