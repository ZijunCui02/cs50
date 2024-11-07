name = input("What is your name? ").title()

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case "Luna":
#         print("Ravenclaw")
#     case _:
#         print("Who")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco" | "Crabbe" | "Goyle":
        print("Slytherin")
    case _:
        print("Who?")
