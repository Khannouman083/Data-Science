name="Nouman Khan"

nameUpper=name.upper() #converts to uppercase
nameLower=name.lower() #converts to lowercase
nameNew=name.replace("Nouman", "Nomii") #replace the string
nameFind= name.find("Khan") #return index if found
nameNotFound=name.find("Nomii") #return -1 if not found
findIN= "N" in name #use the in keyword (Either return true or false)


print(nameUpper)
print(nameLower)
print(nameNew)
print(nameFind)
print(nameNotFound)
print(findIN)


