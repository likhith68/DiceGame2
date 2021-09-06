import random

n="y"

while n.lower()!="n":
    k = random.randint(1, 6)
    if k==1:
        print("-----------")
        print("-----------")
        print("-----0-----")
        print("-----------")
        print("-----------")
    elif k==2:
        print("-----------")
        print("-----------")
        print("---0---0---")
        print("-----------")
        print("-----------")
    elif k==3:
        print("-----------")
        print("--0--------")
        print("-----0-----")
        print("--------0--")
        print("-----------")
    elif k==4:
        print("-----------")
        print("---0---0---")
        print("-----------")
        print("---0---0---")
        print("-----------")
    elif k==5:
        print("-----------")
        print("--0-----0--")
        print("-----0-----")
        print("--0-----0--")
        print("-----------")
    elif k==6:
        print("-----------")
        print("---0---0---")
        print("---0---0---")
        print("---0---0---")
        print("-----------")
    n=input("Do you want roll the dice again???(y/n):")