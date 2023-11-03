Dict = {
    "name": "Dev",
     "class": "3-B",
     "roll-no": 220029000110,
        "age":18
}

print(Dict)

print(
    "Name:", Dict.get("name")
)

Dict2 = {
    "name": "sharma"
}

Dict["roll-no"] = Dict + Dict2

print(Dict["roll-no"] )