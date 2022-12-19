import re

day = "19"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

blueprints = []

with open(file, "r") as file:
    for line in file:
        blueprint = {}
        line = line.split(".")
        blueprint["id"] = (re.sub(r'[^0-9 ]', '', line[0])).strip().split("     ")[0]
        blueprint["ore"] = (re.sub(r'[^0-9 ]', '', line[0])).strip().split("     ")[1]
        blueprint["clay"] = (re.sub(r'[^0-9]', '', line[1])).strip()
        blueprint["obsidian"] = (re.sub(r'[^0-9 ]', '', line[2])).strip().split("   ")
        blueprint["geode"] = (re.sub(r'[^0-9 ]', '', line[3])).strip().split("   ")
        blueprints.append(blueprint)
