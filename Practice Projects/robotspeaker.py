import os

print("Hello  welcome to Robo Speaker. \n Made by Tahsin Ahmad")


while True:
        x = input("What you went to say: ")
        if x == "OK" :
            break
        command = f"Say {x}"
        os.system(command)