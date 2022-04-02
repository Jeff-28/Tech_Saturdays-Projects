name = input("Type your name: ")
print("Good morning {}! Remember that every action you make has consecuences. I hope you have a great day.".format(name))

print()
answer = input(
    "You are leaving your house running late and now you are heading to your job. You can either go through the shortest route\
 or the fastest route. Which route would you like to go? (shortest/fastest)? ").lower()

if answer == "shortest":
    print()
    answer = input(
        "The shortest route has many traffic lights. You see that the Krispy Kreme ahead is advertising their dozen of any doughnuts\
 at half the price. The fact of getting some doughnuts sounds very enticing, specially beacuse you skipped breakfast during\
 the morning rush. Will you go to the drive-through to get something to eat in the way, or will you skip the treat and endure\
 your hunger in the traffic? (shop/skip)? ")
    print()

    if answer == "shop":
        print("You went to the drive-through and after a moment you notice the ridiculous long line, but now you can't get out cause\
 there are cars blocking your back. You end up arriving late and got fired!")

    elif answer == "skip":
        print("You stayed on the road hoping that the traffic will loosen up ahead, but you noticed the road is being repaired and the\
 traffic is just getting worse. You end up arriving late and got fired!")

    else:
        print('Not a valid option. You lose.')

elif answer == "fastest":
    print()
    answer = input(
        "You took the highway, but now you are feeling a great urge to pee. Will you continue the route even if pee in your clothes,\
 or will you stop in the nearest emergency lane available to make a quick flush? (continue/stop)? ")
    print()

    if answer == "continue":
        print("You got on time to your job, but now you have a huge stain in your pants and a terrible stink.\
 The walk of embarrassment is awaiting...")

    elif answer == "stop":
        answer = input(
            "You stopped the car and now you are getting ready to do #1. Suddenly, you noticed that a snake is around a bush in the greens.\
 Will you just ignore it cause you can't hold the urge anymore, or will you try to scare it away? (ignore/scare)? ")
        print()

        if answer == "ignore":
            print("The snake reaches your leg and bites you. You end up dying poisoned.")
        elif answer == "scare":
            print("You managed to scare the snake away and finally let the fluids out of your body. Unfortunately, that awful\
 encounter took you longer than expected, so you ended up arriving late and got fired.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for participating {}!".format(name))
