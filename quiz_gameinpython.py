print("welcome to my computer quiz!!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("ok lets play! :)")
score=0
answer = input("what does cpu stand for ").lower()
 

if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!!")

answer = input("what is the full form of IDE  ").lower()

if answer.lower() == "integrated development environment":
    print("correct!")
    score += 1
else:
    print("incorrect!!")

answer = input("who is father of computer programming ").lower()

if answer.lower() == "charles babbage":
    print("correct!")
    score += 1
else:
    print("incorrect!!")

answer = input("who is often considered the father of modern computer programming ").lower()

if answer == "dennis ritchie":
    print("correct!")
    score += 1
else:
    print("incorrect!!")
print("you got " + str(score) +" questions correct")
print("you got" + str((score/4)*100) +"%")