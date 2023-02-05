light: str = input("what color is the light? ").lower()
if (light=="green"):
    print("Go")
else:
    if (light!="red"):
        if (light=="yellow"):
            print("slow")
        else:
            print("report")
    else:
        print("stop")
print("don't look at your phone")

number_string: str= "123"
number_odd: int=0
if(int(number_string[0]) % 2==1):
    print("odd")
    number_odd= number_odd+1
if(int(number_string[1]) % 2==1):
    print("odd")
    number_odd= number_odd+1
if(int(number_string[2]) % 2==1):
    print("odd")
    number_odd= number_odd+1
print("You have "+ str(number_odd) + " odds")