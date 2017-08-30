# This program says hello and greets a person by name.
#
# Your Name
# August 17, 2016


print("Hello.")
print("What is your name?")
name = input()
print("It is good to meet you, " + name + ".")

print("What is your favorite college?")
college = input()

if college == "Clemson":
    print(college + " is really cool!")
elif college == "Carolina":
    print("Boooooooooooooooo!")
elif college == "Florida State":
    print("I hate that team.")
else:
    print("Oh, that's interesting.")

running = True

while running:
    print("Tell me something about yourself.")
    something = input()

    if something == "goodbye":
        running = False
    elif "mother" in something:
        print("Ah, learning about your family is interesting.")
    elif "computer" in something:
        print("I'm interested in computers too.")
    else:
        print("That's interesting, tell me more.")

print("It was nice talking with you today. Goodbye.")





    
