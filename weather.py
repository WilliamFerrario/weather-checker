import sys, requests, json, os

def main():
    #json file to keep track of favorites
    listFile = 'favs.json' 
    #api key
    key = 'b9f2337c6c95385e199b1a5e2710909e'
    
    if len(sys.argv) < 2:
        print("Command Examples:\npython weather.py [command] [city]")
        print("python weather.py add Lisbon")
        print("python weather.py remove Philadelphia")
        print("python weather.py list")
        print("python weather.py weather Scranton")
        sys.exit(1)

    command = sys.argv[1]
    
    #conditional statements for arguments below
    
    
    if command == "add" and len(sys.argv) == 3: #add
        addFavorite(listFile, sys.argv[2])
    elif command == "remove" and len(sys.argv) == 3: #remove
        removeFavorite(listFile, sys.argv[2])
    elif command == "list": #list
        listFavorites(listFile)
    elif command == "weather" and len(sys.argv) == 3: #weather
        city = sys.argv[2]
        weather = getWeather(city, key)
        if weather:
            temp = weather['main']['temp']
            description = weather['weather'][0]['description']
            print(f"The weather in{city}: {description}, Temperature: {temp} C")
        else:
            print("error getting weather data.")
    else:
        print("invalid argument")
        
#function to call api
def getWeather(city, key):
    #TODO -- may need to use lat and long paired with geocoder API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return 
    
#list favorite cities from 
def readFavorites(listFile):
    if os.path.exists(listFile):
        with open(listFile, 'rw') as file:
            return json.load(file)
    else:
        return []
        
def writeFavorites(listFile, favorites):
    with open(listFile, 'w') as file:
        json.dump(favorites, file, indent = 4)
        
def addFavorite(listFile, city):
    favorites = readFavorites(listFile)
    if city not in favorites:
        favorites.append(city)
        writeFavorites(listFile, favorites)
        print(f"{city} is now added to favorites.")
    else:
        print(f"{city} is already in favorites.")
        
def removeFavorite(listFile, city):
    favorites = readFavorites(listFile)
    if city in favorites:
        favorites.remove(city)
        writeFavorites(listFile, favorites)
        print(f"{city} has been removed from favorites.")
    else:
        print(f"{city} is not in favorites.")

def listFavorites(listFile):
    favorites = readFavorites(listFile)
    print("Favorite Cities:")
    for city in favorites:
        print(city)
        
        
if __name__ == "__main__":
    main()