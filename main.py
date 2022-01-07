import json
from os import listdir, mkdir
from os.path import isfile, join, exists
from shutil import rmtree

with open("config_generate.json","r") as file:
    data = json.load(file)

path_list = [
    data["folder"],
    "data",
    "immersiveengineering",
    "recipes",
    "cloche"
]
if exists(path_list[0]):
    resp = input("Do you want overwrite the directory "+ data["folder"] + "? (Y/N or Q) ").lower()
    while resp != "y" and resp != "n" and resp != "q":
        print("ERROR wrong answer")
        resp = input("Do you want overwrite this directory "+ data["folder"] + "? (Y/N or Q) ").lower()
    if resp == "q":
        input("Press Enter to quit...")
        exit()
    elif resp == "y":
        rmtree(path_list[0])
    elif resp == "n":
        input("Press Enter to quit (you can change name in config_generate.json)...")
        exit()
    
path_file = ""
for i in path_list:
    path_file+=i
    mkdir(path_file)
    path_file+="/"
    
mcmeta = {
    "pack":{
        "pack_format": 5,
        "description":"Immersive Engineering Integration with Mystical Agriculture"
        }
}
with open("datapack/pack.mcmeta", 'w') as outfile:
    json.dump(mcmeta,outfile)

normal_model = [f for f in listdir("base model") if isfile(join("base model", f))]

for i in data["normal"]:
    for j in normal_model:
        with open("base model/"+j) as file_normal:
            h = json.load(file_normal)
            h["results"][0]["item"] = h["results"][0]["item"].replace("xxxx",i)
            h["input"]["item"] = h["input"]["item"].replace("xxxx",i)
            h["render"]["block"] = h["render"]["block"].replace("xxxx",i)
            with open(path_file+i+"_"+j, 'w') as outfile:
                json.dump(h, outfile)

for i in data["custom"]:
    if "mod" in i:
        mod = i["mod"]
    else:
        mod = "minecraft"
    for j in normal_model:
        with open("base model/"+j) as file_normal:
            h = json.load(file_normal)
            h["results"][0]["item"] = mod+":"+i["results"]
            h["input"]["item"] = mod+":"+i["input"]
            h["render"]["block"] = mod+":"+i["name"]
            if "render" in i:
                h["render"]["type"] = i["render"]
            with open(path_file+i["name"]+"_"+j, 'w') as outfile:
                json.dump(h, outfile)

input("Finish ! Press Enter to quit...")