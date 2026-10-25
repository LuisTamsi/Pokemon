import requests
import random

POKEMON_NAMES = [
    "Bulbasaur", 
    "Charmander", 
    "Squirtle", 
    "Pikachu", 
    "Jigglypuff"]


POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_RETRIES = 3

def get_random_pokemon():
  try:
    print("Obtaining a random Pokemon.")
    pokemon_name = random.choice(POKEMON_NAMES).lower()
    response = requests.get(f"{POKEMON_API_URL}{pokemon_name}")
    
    if response.status_code != 200:
      print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
      return None
    
    data = response.json()
    
    return {
        "name": data["name"],
        "height": data["height"] / 10,  
        "weight": data["weight"] / 10,  
      }
    
  except Exception as e:
    print(f"An error occurred while fetching Pokemon data: {e}")
    return None

def main():
    pokemon = get_random_pokemon()
    
    if pokemon is None:
        print("Could not retrieve a Pokemon")
        return
      
    print(f"Height: {pokemon['height']} m")
    print(f"Weight: {pokemon['weight']} kg")
    
    print("Guess the Pokemon's name based on the height and weight provided.")
    print("You have 3 attempts to guess the Pokemon's name.")
    
    for attempt in range(MAX_RETRIES):
      choose = input("Guess the Pokemon's name: ").strip().lower()
      print(f"Attempt {attempt + 1} of {MAX_RETRIES}")
      
      if choose == pokemon["name"]:
          print(f"Congratulations! You guessed it right. The Pokemon is {pokemon['name'].capitalize()}.")
          break
      else:
          print("Incorrect guess.")
          if attempt < MAX_RETRIES - 1:
              print("Try again.")
          else:
              print(f"Sorry, you've used all your attempts. The correct answer was {pokemon['name'].capitalize()}.")
    
        
        
if __name__ == "__main__":
    main()