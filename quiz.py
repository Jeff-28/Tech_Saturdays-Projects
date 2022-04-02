print("Welcome to my quiz!")
print()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print()

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print()

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print()

answer = input("Who sings the hit song \"La Gasolina\"? ")
if answer.lower() == "daddy yankee":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print()

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
