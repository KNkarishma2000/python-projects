print("Welcome to My Computer Quiz!")


playing = input("Do You Want to Play? ")
 
if playing.lower() != "yes":
    quit()
print("Okay! Let's Play :) ")

score = 0
answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
answer = input("What does GPU Stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
answer = input("What does PSU Stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
    
    
print("you got " + str(score) + "Questions Correct!")

print("you got " + str((score/4) * 100) + "%")