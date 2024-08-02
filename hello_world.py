import sys

# Print name
program_name = sys.argv[1]
print(f"Hello, my name is {program_name}!")

# Asks your name
name = input("What is your name? > ")

# Print greeting with your name
print(f"Hello {name}")


# ----------------------------------

if name == "Bogdan":
    print("Cool!")
elif name == "Kolya":
    print("Need more stady")
else:
    print("OK")

