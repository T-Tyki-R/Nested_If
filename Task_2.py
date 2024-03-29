# Quick Decisions: The Event Planner

attendees = int(input("Enter the numbers of attendees: "))
print("Large Hall" if attendees > 100 else "Conference Room" if attendees <= 75 and attendees >= 30 else "Audio room")


foodRecommendation = input("Are you a vegan? ")
print("Veggie Delight Caterers" if foodRecommendation == "yes" else "Gourmet Meals Caterers") # <--- was this suppose to be it's own line of code?