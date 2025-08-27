import random
import os

hangman=["""
+---+
  |   |
  O   |
      |
      |
      |
=========
""","""
+---+
  |   |
  O   |
  |   |
      |
      |
=========
""","""
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
""","""
+---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""","""
+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""","""
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""]


words=["book","door","fish","milk","apple","water","window","school","table","ball","football","notebook"]
random_woard=random.choice(words)
display=["_"]*len(random_woard)

lifes=6
i_hangman=0

print("""
+---+
  |   |
      |
      |
      |
      |
=========
""")

while "_" in display and lifes > 0:
    
    print("\n")
    print(display)
    print("\n")
    print("LIFES: ",lifes)
    print("\n")
    guessed=input("Guess a letter: ").lower()

    if guessed in random_woard:
        os.system("cls")
        if i_hangman != 0 :
            print(hangman[i_hangman-1])
        print("\ncorrect!!\n")
        for i in range(len(display)):
            if random_woard[i]==guessed:
                display[i]=guessed
    else:
        os.system("cls")
        
        print(hangman[i_hangman])
        print("\nincorrect!!\n")
        lifes -=1
        i_hangman +=1 

if "_" in display:
    print("YOU LOSE!!!")
    print("\nthe correct answer is : ",random_woard)
    print("\n")
    
else:
    print("""
***********
YOU WIN
***********\n                    
""")
    print(" ".join(display)) 
    print("\n")