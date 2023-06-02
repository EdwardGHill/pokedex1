import csv
import random



class Pokemon:
    def __init__(self, id, name, type1, type2, generation, legendary, total):
        self.id = id
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.generation = generation
        self.legendary = bool(legendary)
        self.total = total

class Pokedex:
    def __init__(self, csv_file_path):
        self.pokemon_list = []
        self.load_data(csv_file_path)

    def load_data(self, csv_file_path):
        with open(csv_file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                legendary = True if row['Legendary'] == "True" else False
                pokemon = Pokemon(
                    id=row['#'],
                    name=row['Name'],
                    type1=row['Type 1'],
                    type2=row['Type 2'],
                    generation=int(row['Generation']),
                    legendary=legendary,
                    total=int(row['Total'])
                )
                self.pokemon_list.append(pokemon)

    def get_all_pokemon(self):
        return self.pokemon_list

    def get_pokemon_by_name(self, name):
        for pokemon in self.pokemon_list:
            if pokemon.name.lower() == name.lower():
                return pokemon
        return None
    
    def get_pokemon_by_search(self, name: str):
        if len(name) < 3:
            return []
        
        matching_pokemon = [pokemon for pokemon in self.pokemon_list if name.lower() in pokemon.name.lower()]
        return matching_pokemon

    def get_pokemon_by_id(self, id):
        id = str(id)
        for pokemon in self.pokemon_list:
            if str(pokemon.id) == id:
                return pokemon
        return None
    
    def get_pokemon_by_type1(self, type1):
        matching_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon.type1.lower() == type1.lower():
                matching_pokemon.append(pokemon)
        return matching_pokemon
    
    # Could use list comprehension instead
    # def get_pokemon_by_type1(self, type1):
    # return [pokemon for pokemon in self.pokemon_list if pokemon.type1.lower() == type1.lower()]
    
    def get_pokemon_by_type2(self, type2):
        matching_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon.type2.lower() == type2.lower():
                matching_pokemon.append(pokemon)
        return matching_pokemon
    
    def get_pokemon_by_type(self, type):
        matching_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon.type1.lower() == type.lower() or pokemon.type2.lower() == type.lower():
                matching_pokemon.append(pokemon)
        return matching_pokemon
    
    def get_pokemon_by_generation(self, generation):
        matching_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon.generation == generation:
                matching_pokemon.append(pokemon)
        return matching_pokemon
    
    def get_pokemon_by_legendary(self):
        legendary_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon.legendary:  
                legendary_pokemon.append(pokemon)
        return legendary_pokemon
    
    def get_random_team(self):
        team_size = 6
        random_team = random.sample(self.pokemon_list, team_size)
        return random_team
    
    def get_strong_team(self):
        team_size = 6

    # Calculate the total stats for all Pokémon
        total_stats = [pokemon.total for pokemon in self.pokemon_list]

    # Determine the cutoff for the top 20% of total stats
        cutoff = int(len(total_stats) * 0.2)
        top_pokemon_indices = sorted(range(len(total_stats)), key=lambda i: total_stats[i], reverse=True)[:cutoff]

    # Sort the top indices again and select random Pokémon from the top 20%
        sorted_top_pokemon_indices = sorted(top_pokemon_indices)
        strong_team = random.sample([self.pokemon_list[i] for i in sorted_top_pokemon_indices], k=team_size)
        return strong_team
    
    def get_weak_team(self):
        team_size = 6

    # Calculate the total stats for all Pokémon
        total_stats = [pokemon.total for pokemon in self.pokemon_list]

    # Determine the cutoff for the lowest 20% of total stats
        cutoff = int(len(total_stats) * 0.2)
        lowest_pokemon_indices = sorted(range(len(total_stats)), key=lambda i: total_stats[i])[:cutoff]

    # Sort the lowest indices again and select unique Pokémon from the lowest 20%
        sorted_lowest_pokemon_indices = sorted(lowest_pokemon_indices)
        weak_team_indices = random.sample(sorted_lowest_pokemon_indices, k=team_size)
        weak_team = [self.pokemon_list[i] for i in weak_team_indices]
        return weak_team
    
    def get_legendary_team(self):
        team_size = 6

    # Get all legendary Pokémon
        legendary_pokemon = [pokemon for pokemon in self.pokemon_list if pokemon.legendary]

    # Select random legendary Pokémon for the team
        team = random.sample(legendary_pokemon, k=team_size)
        return team
    
    def get_rainbow_team(self):
        team = []

    # Random Fire type 1
        fire_pokemon = random.choice(self.get_pokemon_by_type1("Fire"))
        team.append(fire_pokemon)

    # Random Fighting or Ground type 1
        fighting_ground_pokemon = random.choice(self.get_pokemon_by_type1("Fighting") + self.get_pokemon_by_type1("Ground"))
        team.append(fighting_ground_pokemon)

    # Random Electric type 1
        electric_pokemon = random.choice(self.get_pokemon_by_type1("Electric"))
        team.append(electric_pokemon)

    # Random Grass type 1
        grass_pokemon = random.choice(self.get_pokemon_by_type1("Grass"))
        team.append(grass_pokemon)

    # Random Water type 1
        water_pokemon = random.choice(self.get_pokemon_by_type1("Water"))
        team.append(water_pokemon)

    # Random Poison or Ghost type 1
        poison_ghost_pokemon = random.choice(self.get_pokemon_by_type1("Poison") + self.get_pokemon_by_type1("Ghost"))
        team.append(poison_ghost_pokemon)

        return team





