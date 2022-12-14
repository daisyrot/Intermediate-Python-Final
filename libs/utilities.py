def pick(options):
    """Pick an option from a list of options."""
    for i, option in enumerate(options):
        print(str(i + 1) + ": " + option)
    choice = input("Pick an option: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(options):
            raise ValueError
    except ValueError:
        if choice in pick and choice != "":
            return choice
        else:
            print("Invalid choice.")
            return pick(options)
    else:
        return options[choice - 1]
