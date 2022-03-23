import sys, string

while True:
    bad = ".?!'()*&!@#$%+-_={}|\;:,/~`"
    userInput = input("Enter a string to test for palindrome or 'exit': ")

    if userInput == "exit":
        sys.exit()

    userInput = userInput.lower()
    for char in bad:
        userInput = userInput.replace(char, "")

    userInput = list(userInput)

    if userInput == userInput[::-1]:
        print("Palindrome test: True")
    else:
        print("Palindrome test: False")