from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon
from .forms import PokemonForm


from django.core.paginator import Paginator

def pokemon_list(request):
    pokemons = Pokemon.objects.all()  
    paginator = Paginator(pokemons, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pokemon/list.html', {'pokemons': page_obj})



def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon})


def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'pokemon/form.html', {'form': form})


def pokemon_edit(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon/form.html', {'form': form})


def pokemon_confirm_delete(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('pokemon_list')
    return render(request, 'pokemon/confirm_delete.html', {'pokemon': pokemon})
