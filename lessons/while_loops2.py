"""Demonstrates while loops by finding low value in string"""
cards: str = "5235"
card_idx: int = 0
lowest_card: int = int(cards[0])
while card_idx < 4:
    current_card: int = int(cards[card_idx])
    if current_card<lowest_card:
        lowest_card = current_card
    card_idx = card_idx + 1
print(lowest_card)
print("Hello\tworld\t!")
print("the computer said,\"hello\"")
print("\\a")
print("hi")
print(f"hi")
name: str = "Jessie"
age_turning: int = 21
print("Hello " + name + ", you are almost " + str(age_turning))
print(f"Hello {name}, you are almost {age_turning}")