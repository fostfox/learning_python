import random

DAD_JOKES_LIST = [
        "Why don't skeletons fight each other? Because they don't have the guts!",
        "I was wondering why the baseball was getting bigger. Then it hit me.",
        "I'm reading a book about anti-gravity. I can't put it down.",
        "My dolphin puns are terrible on porpoise.",
        "Orion's Belt is a huge waist of space."
    ]

FORTUNE_COOKIES = [
        "Be at peace with yourself.",
        "Your home will be filled with peace and harmony.",
        "Don't hesitate to tackle a difficult problem.",
        "Get ready for a life-changing event!",
        "Work with your destiny. Stop trying to outrun it."
    ]

MAGIC_BALL = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

def wait_for_user() -> None:
    input("\nPress ENTER to return to the menu...")

def random_message(messages: list) -> None:
    print("\n", random.choice(messages), end="\n\n")
    wait_for_user()

def cli() -> None:
    try:
        print("\nWelcome to the Fun Console Program!")
        while True:
            print("\nPlease choose an option:\n")
            print("1. Dad Joke Generator")
            print("2. Fortune Cookie")
            print("3. Magic 8-Ball")
            print("4. Exit\n")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                random_message(DAD_JOKES_LIST)
            elif choice == "2":
                random_message(FORTUNE_COOKIES)
            elif choice == "3":
                input("\nAsk a yes/no question: \n")
                random_message(MAGIC_BALL)
            elif choice == "4":
                break
            else:
                print("\nInvalid choice, please select again.")
    except KeyboardInterrupt:
        print("\n\nThe program was terminated by the user (Ctrl+C).\n")
    finally:
        print("Goodbuy! Thank you!")
        

if __name__ == "__main__":
    cli()
