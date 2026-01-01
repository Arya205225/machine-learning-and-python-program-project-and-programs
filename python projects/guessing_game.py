import random
eassy_word=["cat","dog","apple","book","car","house","train","tree","phone","table","tiger"]

    

medium_word=[ "elephant","guitar","notebook","umbrella","airplane","building"]

hard_word=["xylophone","quizzical","juxtapose","mnemonic","zephyr","yacht"]

print("welcome to gessing game")
print("you have 3 level  ( eassy , medium , hard )")

level=input("choose your level : ").lower()
if level=="eassy":
    secret=random.choice(eassy_word)
elif level=="medium":
    secret=random.choice(medium_word)
elif level=="hard":
    secret=random.choice(hard_word)
else:
    print("invalide level")
    exit()

attempts=0
print("\n given the secret password")

while True:
    guess= input("enter your guess:").lower()
    attempts+=1
    if guess==secret:
        print(f"congratulation! you guessed the word {secret} in {attempts} attempts.")
        break
    
    
    hint=" "
    
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("hint:",hint)

print("game over")