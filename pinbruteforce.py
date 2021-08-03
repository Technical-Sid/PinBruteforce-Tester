import random
import pyautogui
import os

chars = "0123456789"
chars_list = list(chars)

f = open("pin.txt",mode="w")

password = pyautogui.password("Enter a pin : ")

guess_pin = ""

while(guess_pin != password):
    guess_pin = random.choices(chars_list, k=len(password))

    print("<-----------------" + str(guess_pin) + "----------------->")

    if(guess_pin == list(password)):
        print("Your Pin is : " + "" .join(guess_pin))
        break
    
print(guess_pin , file=f)    
f.close()