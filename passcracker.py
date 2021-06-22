import random
import pyautogui
import string

chars = "1234567890"
chars_list = list(chars)
# print(chars)

password = pyautogui.password("Enter Your Brute Force Password:  ")

guess_password = ""
 
while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<=================" + str(guess_password)+ "=================>")

    if (guess_password == list(password)):
        print("Your Password Is:  " + "".join(guess_password))

        break