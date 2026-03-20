Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... 
... number_to_guess = random.randint(1, 100)
... attempts = 0
... 
... print("I'm thinking of a number between 1 and 100. Can you guess it?")
... 
... while True:
...     guess = int(input("Enter your guess: "))
...     attempts += 1
...     
...     if guess < number_to_guess:
...         print("Too low! Try again.")
...     elif guess > number_to_guess:
...         print("Too high! Try again.")
...     else:
...         print(f"Congratulations! You guessed it in {attempts} attempts.")
