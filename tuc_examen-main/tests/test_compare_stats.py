# test_main.py
import sys
import os
from fastapi import HTTPException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app


client = TestClient(app)

@patch("app.utils.pokeapi.battle_pokemon")
@patch("app.utils.pokeapi.get_pokemon_name")
def test_compare_pokemon_stats_winner(mock_get_pokemon_name, mock_battle_pokemon):
    # Mock the response from the battle_pokemon function
    mock_battle_pokemon.return_value = ('Charizard', [{'base_stat': 60}] * 6, 'Bulbasaur', [{'base_stat': 50}] * 6)
    mock_get_pokemon_name.side_effect = ['Charizard', 'Bulbasaur']

    response = client.get("/compare-stats/1/2")
    assert response.status_code == 200
    assert response.json() == {
        'result': 'Charizard is the winner!',
        'stat_difference': {'hp': 15, 'attack': 13, 'defense': 14, 'speed': 15, 'special-attack': 15, 'special-defense': 15},
    }
@patch("app.utils.pokeapi.battle_pokemon")
@patch("app.utils.pokeapi.get_pokemon_name")
def test_compare_pokemon_stats_draw(mock_get_pokemon_name, mock_battle_pokemon):
    # Mock the response from the battle_pokemon function for a draw
    mock_battle_pokemon.return_value = ('draw', [{'base_stat': 60}] * 6, 'Squirtle', [{'base_stat': 60}] * 6)
    mock_get_pokemon_name.side_effect = ['Charmander', 'Squirtle']

    response = client.get("/compare-stats/1/1")
    assert response.status_code == 200
    assert response.json() == {'result': 'draw'}

@patch("app.utils.pokeapi.battle_pokemon")
@patch("app.utils.pokeapi.get_pokemon_name")
def test_compare_pokemon_stats_pokemon_not_found(mock_get_pokemon_name, mock_battle_pokemon):
    # Mock the response from the battle_pokemon function for Pokemon not found
    mock_battle_pokemon.side_effect = HTTPException(status_code=404, detail="One or both Pokemon not found")
    mock_get_pokemon_name.return_value = 'InvalidPokemon'

    response = client.get("/compare-pokemon-stats/100000/123")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
