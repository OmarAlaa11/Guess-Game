import random as random


L=["ronaldo","messi","neymar","mbabe","muller","haland"]
R=random.choice(L)
letters=list(R)
letters=",".join(letters)

display=[]
for i in (letters):
    display.append("-")

n=len(R)
name=input("Please Enter your name \n")
print(f"Hello {name},Welcome to the Game.\n")
print(f"Guess a word in {n} letters \n {display} \n")
while "-" in display:
    Guess=input("Guess a letter : ").lower()
    if Guess in letters:
        for position in range(n):
            letter=letters[position]
            if letter ==  Guess:
                display[position]=Guess
    print(f"\n{display}")
    if Guess not in letters:
        print("Wrong,Please Try again!")
    if "-" not in display:
        print("\n Congratulations You Win!!!!")
        display.clear()
        break