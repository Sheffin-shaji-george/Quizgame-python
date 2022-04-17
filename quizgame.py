print("welcome to my computer quiz")

playing=input("Do you want to play?").lower()

if playing !="yes":
    quit()

print("Okey,Let's Play!")
score = 0

answer = input("What does CPU stands for?").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for?").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does ROM stands for?").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stands for?").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU stands for?").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print("You got " +str(score) + " correct answers")
print("You got " + str((score/5)*100)+"%")


