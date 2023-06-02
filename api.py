from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Pokedex
import random

app = FastAPI()
pokedex = Pokedex('Data/pokemon_data.csv')

origins = ["http://127.0.0.1:5500"]  # Replace with the actual URL of your front-end

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/pokemon")
def get_all_pokemon():
    return pokedex.get_all_pokemon()

@app.get("/pokemon/name/{name}")
def get_pokemon_by_name(name: str):
    return pokedex.get_pokemon_by_name(name)

@app.get("/pokemon/search/{name}")
def get_pokemon_by_search(name: str):
    return pokedex.get_pokemon_by_search(name)

@app.get("/pokemon/id/{id}")
def get_pokemon_by_id(id: str):
    return pokedex.get_pokemon_by_id(id)

@app.get("/pokemon/type1/{type1}")
def get_pokemon_by_type1(type1: str):
    return pokedex.get_pokemon_by_type1(type1)

@app.get("/pokemon/type2/{type2}")
def get_pokemon_by_type2(type2: str):
    return pokedex.get_pokemon_by_type2(type2)

@app.get("/pokemon/type/{type}")
def get_pokemon_by_type(type: str):
    return pokedex.get_pokemon_by_type(type)

@app.get("/pokemon/generation/{generation}")
def get_pokemon_by_generation(generation: int):
    return pokedex.get_pokemon_by_generation(generation)

@app.get("/pokemon/legendary")
def get_pokemon_by_legendary():
    return pokedex.get_pokemon_by_legendary()

@app.get("/pokemon/random")
def get_random_pokemon():
    random_pokemon = random.choice(pokedex.get_all_pokemon())
    return random_pokemon
    
@app.get("/pokemon/random_team")
def get_random_team():
    return pokedex.get_random_team()

@app.get("/pokemon/strong_team")
def get_strong_team():
    return pokedex.get_strong_team()

@app.get("/pokemon/weak_team")
def get_weak_team():
    return pokedex.get_weak_team()

@app.get("/pokemon/legendary_team")
def get_legendary_team():
    return pokedex.get_legendary_team()

@app.get("/pokemon/rainbow_team")
def get_rainbow_team():
    return pokedex.get_rainbow_team()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)