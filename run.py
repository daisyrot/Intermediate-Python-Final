import os;
from dotenv import load_dotenv
import libs.apis as apis
import libs.utilities as utils
import time

load_dotenv()
def lookup():
    # Get the user's name
    name = input("Enter a username or champion name: ")

    if apis.champByName(name) != None:
        champLookup(name)
    else:
        # Get the user's data
        resp = apis.getSummoner(name)
        # print == 10 times
        print("=" * len(resp["id"]))
        print("Summoner name: " + resp["name"])
        print("Summoner level: " + str(resp["summonerLevel"]))
        print("Summoner ID: " + str(resp["id"]))
        print("=" * len(resp["id"]))

def champLookup(name):
    # Capitalize the first letter
    name = name[0].upper() + name[1:]

    # Get the champion data
    champ = apis.champByName(name)

    if not champ:
        print("No username or champion found.")
        return main()

    # Pretty print the champ object
    def champLoop():
        # Get the choice
        choice = utils.pick((
            "Info", "Abilities", "Back"
        ))

        if choice == "Info":
            print("=" * len(champ["name"]))
            print("Champion name: " + champ["name"] + ", " + champ["title"])
            print(" ^ " + champ["blurb"])
            print("Skin Count: " + str(len(champ["skins"])))

            print("=" * len(champ["name"]))
        elif choice == "Abilities":
            print(" === Abilities: === ")
            for ability in champ["spells"]:
                print(ability["name"])
                print(" ^ " + ability["description"])
                print(" ^ Cooldown: " + str(ability["cooldownBurn"]))
                print(" ^ Cost: " + str(ability["costBurn"]))
            print("===================")
        elif choice == "Back":
            return main()
        else:
            print("=" * 20)
            return champLoop()
        champLoop()

    champLoop()

def masteries():
    # Get the user's name (for id)
    name = input("Enter a username: ")
    # Get the user's data
    resp = apis.getSummoner(name)

    if not resp["id"]:
        print("Invalid name ;(")
        main()
    else:
        resp = apis.getMasteries(resp["id"])
        # Filter by the field 'championPoints'
        resp = sorted(resp, key=lambda k: k['championPoints'], reverse=True)
        # Print the top 5 champions
        print(" === Top 5 Champions: === ")
        for i in range(5):
            champ = apis.champById(resp[i]["championId"])
            print(champ["name"])
            print(" ^ Mastery Level: " + str(resp[i]["championLevel"]))
            print(" ^ Mastery Points: " + str(resp[i]["championPoints"]))
            print(" ^ Last Played: " + time.strftime('%Y-%m-%d', time.localtime(resp[i]["lastPlayTime"] / 1000)))


def gameInfo():
    # Get the user's name (for id)
    name = input("Enter a username: ")
    # Get the user's data
    resp = apis.getSummoner(name)

    if not resp["id"]:
        print("Invalid name ;(")
        main()
    else:
        resp = apis.getMasteries(resp["id"])
        print(resp)

def challenges():
    resp = apis.challenges()

    print(resp)

def main():
    # Get the choice
    choice = utils.pick((
        "Search", "Mastery", "Exit"
    ))

    if choice == "Search":
        lookup()
    elif choice == "Exit":
        print("Goodbye!")
        exit()
    elif choice == "Mastery":
        masteries()
    elif choice == "Challenges":
        challenges()
    else:
        print("Invalid choice.")
        main()
    main()

# Main
if __name__ == "__main__":
    main()