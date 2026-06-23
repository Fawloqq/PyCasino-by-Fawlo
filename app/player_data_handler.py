import json, os
from dataclasses import dataclass
from typing import Self

@dataclass
class Player:
    name: str = ''
    balance: int = 1000
    games_played: int = 0
    id: int = 0
    password: str = '0000'

    @staticmethod
    def player_from_dict(dict: dict[str, int]) -> Self:
        return Player(name=dict['name'], balance=dict['balance'], games_played=dict['games_played'], id=dict['id'], password=dict['password'])

    @staticmethod
    def create_player(name: str, password: int) -> Self:
        id = PlayerHandler().get_max_id() + 1
        return Player(name, 1000, 0, id, password)

    def load_balance(self, amount: int) -> None:
        self.balance += amount


class PlayerHandler:
    def __init__(self) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(base_dir, "users-data.json")
        
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)
        
    def _save_all_players_raw(self, players: list[dict[str, str | int]]) -> None:
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(players, file, indent=4, ensure_ascii=False)

    def _get_all_players_raw(self) -> list[dict[str, int | str]]:
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def load_player(self, player_id: int) -> Player:
        with open(self.path, 'r', encoding='utf-8') as file:
            players_list = json.load(file)
            for player in players_list:
                if player["id"] == player_id:
                    return Player.player_from_dict(player)
            raise ValueError(f'Player with id {player_id} not found')

    def get_max_id(self) -> int:
        if not os.path.getsize(self.path):
                return 0
        with open(self.path, 'r', encoding='utf-8') as file:
            max_id = 0
            for player in json.load(file):
                if player['id'] > max_id:
                    max_id = player['id']
            return max_id

            
    
    def save_player(self, player: Player) -> None:
        players_list = self._get_all_players_raw()

        player_dict = {
            "name": player.name,
            "balance": player.balance,
            "games_played": player.games_played,
            "id": player.id,
            "password": player.password
        }

        found = False
        for i, p in enumerate(players_list):
            if p["id"] == player.id:
                players_list[i] = player_dict
                found = True
                break
        
        if not found:
            players_list.append(player_dict)
        
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(players_list, file, indent=4, ensure_ascii=False)
    
    def delete_account(self, player_id: int) -> None:
        confirmed = input('Confirm account deletion? (y/n): ').lower().strip()

        if confirmed == 'n':
            print('Coming back to menu')
            return 

        if confirmed != 'y':
            print('❌ Wrong option! Enter "y" or "n".')
            return

        all_players = self._get_all_players_raw()

        player_exists = any(player['id'] == player_id for player in all_players)
        
        if not player_exists:
            raise ValueError('Player not found')
        
        updated_players = [player for player in all_players if player['id'] != player_id]
        self._save_all_players_raw(updated_players)
    
    def change_password(self, player_id: int, new_password: int) -> None:
        confirmed = input('Confirm password change (y/n): ').lower().strip()

        if confirmed == 'n':
            print('Coming back to menu')
            return 

        if confirmed != 'y':
            print('❌ Wrong option! Enter "y" or "n".')
            return
    
        all_players = self._get_all_players_raw()


        player_exists = any(player['id'] == player_id for player in all_players)
        
        if not player_exists:
            raise ValueError('Player not found')
        
        for player in all_players:
            if player['id'] == player_id:
                player['password'] = new_password
        
        self._save_all_players_raw(all_players)