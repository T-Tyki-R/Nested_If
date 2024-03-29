# Nested Decisions: The Adventure Game 


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    print("You found a bird's nest" if action == "tree" else "You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    print("SHHHH!!! You found a sleeping dragon!" if action == "torch" else "Oops... you bumped into an angry dragon!")
else:
    pass

