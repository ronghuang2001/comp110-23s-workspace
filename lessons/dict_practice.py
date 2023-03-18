"""Practice with disctionaries."""

ice_cream: dict[str,int] = dict()  # empty one
ice_crem: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}   
ice_creamm: dict[str,int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}   # can actually use single quote
# Adding
ice_crem["mint"] = 3
print("After adding mint:")
print(ice_crem)

#Removing
ice_crem.pop("mint")
print("After removing mint:")
print(ice_crem)

#Accessing
print(ice_crem["vanilla"])
print(f"Number of vanilla orders: {ice_crem['vanilla']}") #single quote in[]

# updating a value
ice_crem["vanilla"] += 1
print("After adding 1 vanilla")
print(ice_crem)
print(f"Number of vanilla orders: {ice_crem['vanilla']}")

#checking if in dictionary
print("mint" in ice_crem)
print("chocolate" in ice_crem)

ice_crem["apple"]

