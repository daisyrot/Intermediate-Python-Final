import os

from dotenv import load_dotenv

load_dotenv()
region = "na1"
from riotwatcher import LolWatcher, ApiError

# Load the listings of champions and items
watcher = LolWatcher(os.getenv("API_TOKEN"))
champs = watcher.data_dragon.champions("10.24.1", "en_US")
items = watcher.data_dragon.items("10.24.1", "en_US")

def champById(id):
    for key in champs["data"].keys():
        if champs["data"][key]["key"] == str(id):
            return champs["data"][key]
    return None

def champByName(name):
    name = name.lower()
    name = name[0].upper() + name[1:]
    if name in champs["data"]:
        return champs["data"][name]
    else:
        return None

# API Routes #
def getSummoner(name):
    return watcher.summoner.by_name(region, name)

def getMasteries(eid):
    return watcher.champion_mastery.by_summoner(region, eid)

api = {
    getSummoner: getSummoner,
    getMasteries: getMasteries,
}