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
    print("Awesome choice. They're great!")
elif college == "Carolina":
    print("Your choice is dumb.")
elif college == "Florida State":
    print("I hate those guys.")
else:
    print("Oh, that's interesting.")



running = True

print("Tell me something about yourself...")

while running:
    response = input()

    if "goodbye" in response:
        running = False
    elif "computer" in response:
        print("Very interesting. I really like computers.")
        print("Tell me something else about yourself.")
    elif "brother" in response:
        print("I'm a computer. My brother is a Game Boy. Tell me more about your family.")
    elif "pizza" in response:
        print("Mmmmmmm... You're making me hungry.")
    else:
        print("That's interesting. Tell me more.")

print("It was nice talking with you today.")











    

