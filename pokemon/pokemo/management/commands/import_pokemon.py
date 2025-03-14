import requests
from django.core.management.base import BaseCommand
from pokemo.models import Pokemon

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        url = 'https://pokeapi.co/api/v2/pokemon?limit=200'  
        response = requests.get(url)
        data = response.json()

        
        for pokemon in data['results']:
            
            pokemon_data = requests.get(pokemon['url']).json()
            name = pokemon_data['name']
            image = pokemon_data['sprites']['front_default']
            abilities = ', '.join([ability['ability']['name'] for ability in pokemon_data['abilities']])

           
            Pokemon.objects.update_or_create(
                name=name,
                defaults={'image': image, 'abilities': abilities},
            )

        self.stdout.write(self.style.SUCCESS('Pokémon importados exitosamente'))
