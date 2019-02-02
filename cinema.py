# creating some kind of data structure using a dictionary that has list as values
# zero index is age and first index is # of tickets
films = {
    "Incredibles 2": [3, 5],
    "Black Panther": [13, 5],
    "A Quiet Place": [13, 5],
    "A Star Is Born": [18, 5]
}
# using a while loop
while True:
    print(list(films.keys()))
    # title converts answer to title case
    choice = input("What film would you like to see?:").strip().title()

    if choice in films:  # pass key word tells python to move on
        # coverting input to an interger
        age = int(input("How old are you?:").strip())

        # Check user age

        if age >= films[choice][0]:
            total_tickets = int(input("How many tickets do you want?:"))
            # check enough seats
            if films[choice][1] > 0 and total_tickets <= films[choice][1]:
                print("Enjoy the film!")
                remaining = films[choice][1] = films[choice][1] - total_tickets
                print("Remaining tickets", remaining)
            elif films[choice][1] > 0 and total_tickets > films[choice][1]:
                print(
                    "That number of tickets is not available. Total tickets available:", films[choice][1])
            else:
                print("Sorry we are sold out!")
        else:
            print("You are too young to see that film!")

    else:
        print("We don't  have that film...Please see list and/or check spelling")
