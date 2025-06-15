import random

first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().capitalize()
style = input("Preferred style (short/fun/formal/random): ").strip().lower()

def generate_nicknames(first, last, style="random"):
    nicknames = []
    f3, l3 = first[:3], last[-3:]
    f2, l2 = first[:2], last[:2]
    
    base = [
        f3 + l3,
        f2 + l2,
        first + last,
        last + first,
        first[0] + last,
        first + last[0],
        first[:1] + "_" + last[-1:]
    ]
    
    if style == "short":
        nicknames.extend([
            f3, f2 + last[0], first[0] + l3,
            first[:2] + last[-1],
        ])
    elif style == "fun":
        emojis = ['😊', '🔥', '💥', '🌟']
        nicknames.extend([
            f"{f3}{l3}{random.choice(emojis)}",
            f"{first}ie_{random.randint(1, 99)}",
            f"{first}the{last}",
        ])
    elif style == "formal":
        nicknames.extend([
            f"{first}.{last}",
            f"{first}_{last}",
            f"{first}{last[0].upper()}",
        ])
    else:  # random or undefined style
        symbols = ['_', '.', '-', 'X']
        nicknames.extend([
            f"{f3}{random.choice(symbols)}{l3}",
            f"{first}{random.randint(10,99)}",
            f"{random.choice(symbols)}{last}{first[0]}",
        ])
    
    # Remove duplicates and shuffle
    nicknames = list(set(nicknames))
    random.shuffle(nicknames)
    return nicknames

nicknames = generate_nicknames(first_name, last_name, style)

print("\nHere are your generated nicknames:")
for i, name in enumerate(nicknames, 1):
    print(f"{i}. {name}")


save = input("\nWould you like to save these nicknames to a file? (yes/no): ").strip().lower()
if save == "yes":
    with open("nicknames.txt", "w") as f:
        f.write(f"Nicknames for {first_name} {last_name}:\n")
        for name in nicknames:
            f.write(name + "\n")
    print("Nicknames saved to nicknames.txt!")