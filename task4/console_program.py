import random, keyboard

print("\nWelcome to the Fun Console Program!")

def wait_for_user():
    input("\nPress any key to return to the menu...")
    keyboard.read_event()

def random_message(messages):
    print(random.choice(messages))
    wait_for_user()

def dad_joke_generator():
    return [
        "\nWhy don't skeletons fight each other? Because they don't have the guts!",
        "\nI was wondering why the baseball was getting bigger. Then it hit me.",
        "\nI'm reading a book about anti-gravity. I can't put it down.",
        "\nMy dolphin puns are terrible on porpoise.",
        "\nOrion’s Belt is a huge waist of space."
    ]
    
def fortune_cookie():
    return [
        "\nBe at peace with yourself.",
        "\nYour home will be filled with peace and harmony.",
        "\nDon't hesitate to tackle a difficult problem.",
        "\nGet ready for a life-changing event!",
        "\nWork with your destiny. Stop trying to outrun it."
    ]
    
def magic_ball():
    return [
        "\nIt is certain",
        "\nIt is decidedly so",
        "\nWithout a doubt",
        "\nYes definitely",
        "\nYou may rely on it",
        "\nAs I see it, yes",
        "\nMost likely",
        "\nOutlook good",
        "\nYes",
        "\nSigns point to yes",
        "\nReply hazy, try again",
        "\nAsk again later",
        "\nBetter not tell you now",
        "\nCannot predict now",
        "\nConcentrate and ask again",
        "\nDon't count on it",
        "\nMy reply is no",
        "\nMy sources say no",
        "\nOutlook not so good",
        "\nVery doubtful"
    ]
    
def cli():
    while True:
        print("\nPlease choose an option:\n")
        print("1. Dad Joke Generator")
        print("2. Fortune Cookie")
        print("3. Magic 8-Ball")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            random_message(dad_joke_generator())
        elif choice == "2":
            random_message(fortune_cookie())
        elif choice == "3":
            input("\nAsk a yes/no question: \n")
            random_message(magic_ball())
        elif choice == "4":
            print("\nGoodbuy! Thank you!\n")
            break
        else:
            print("\nInvalid choice, please select again.")

if __name__ == "__main__":
    cli()
