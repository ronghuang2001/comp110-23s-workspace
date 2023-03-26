#create dictionary
icecream: dict[str,int]=dict()
icecrem: dict[str,int]= {"chocolate":5,"vanilla":6,"strawberry":7}
#add item to dictionary
icecrem["mint"]=5
icecrem["matcha"]=8
#remove item from dictionary
icecrem.pop("mint")
#modify
icecrem["matach"]=6
print(icecream)
print(icecrem)
#access
print(icecrem["matcha"])
print(f"number of vanilla icecream is {icecrem['vanilla']}")
#check
print("mint" in icecrem)
print("matach" in icecrem)
#create list
g_list: list[str]=list()
grocery_list: list[str]=["apple","egg"]
#add item to list
grocery_list.append("orange")
#remove item from list
grocery_list.pop(0)
#access
print(grocery_list[0])
#modify
grocery_list[0]="banana"
grocery_list.append("banana")
print(g_list)
print(grocery_list)
