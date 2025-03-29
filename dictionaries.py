dict = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21 }
print(dict)
print(type(dict))
print(dict["age"])

dict["name"]= "Nida"
print(dict)

#nested
info = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21,
           "marks":{ "phy": 78,
                    "chem": 98,
                    "urdu": 67               
           } }
print(info)
print(info["marks"])

#Dictionary method

#return all keys
info = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21,
           "marks":{ "phy": 78,
                    "chem": 98,
                    "urdu": 67               
           } }
print(info.keys())
#return all values
dict = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21 }
print(dict.values())
#return all key,value in tuple
info = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21,
           "marks":{ "phy": 78,
                    "chem": 98,
                    "urdu": 67               
           } }
print(info.items())
#return key according to value
dict = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21 }
print(dict.get("name"))
#insert specified items//update
dict = { "name":"nida",
        "surname":"Hassan",
         "Degree" : "BS",
          "age" : 21 }
dict.update({"name":"Nidaa"})
print(dict)