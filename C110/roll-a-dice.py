import random ;


response = "y"

while response == "y":

    no = random.randit(1,6)

    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[  00 ]")
        print("[     ]")
        print("[-----]")

   

    if no == 2:
        print("[  0  ]")
        print("[-----]")
        print("[ 000 ]")
        print("[     ]")
        print("[-----]")

    if no == 3:
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print("[-----]")

    if no == 4:
        print("[-----]")
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if no == 5:
        print("[-----]")
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[  0  ]") 

#Asking 
response = input("press y to roll a dice and n to exit-")
print("n")