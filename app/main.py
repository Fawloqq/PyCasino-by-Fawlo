import sys
from player_data_handler import PlayerHandler, Player

def main() -> None:
    print(80 * '=' + '\n' + 30 * ' ' + 'WELCOME TO PYCASINO\n' + 80 * '=')
    
    handler = PlayerHandler()
    current_user = None

    while current_user is None:
        try:
            print(80 * '=' + '\n' + 30 * ' ' + 'LOGIN SCREEN\n' + 80 * '=')
            print('1. Log in')
            print('2. Sign in')
            print('3. Exit')
            
            choice = input('\nWhat do you want to do?(1-3)\n>')
            
            database = handler._get_all_players_raw()

            match choice:
                case '1':
                    name = input('Enter your name\n>')
                    found_player = {}
                    for player in database:
                        if player['name'] == name:
                            found_player = player
                        else:
                            raise ValueError(f'Player with name {name} not found')
                    
                    if not found_player:
                        raise ValueError(f'Player with name "{name}" not found.')
                        
                    password = input('Enter your password\n>')
                    if found_player['password'] != password:
                        raise ValueError('Wrong password!')
                    
                    
                    current_user = Player(found_player['name'], found_player['balance'],
                                           found_player['games_played'], found_player['id'],
                                             found_player['password']) 
                    print(f'Logged in successfully! Welcome, {name}.')

                case '2':
                    name = input('Enter your name\n>').strip()
                    
                    
                    if any(p["name"] == name for p in database):
                        raise ValueError('Name already taken!')
                        
                    password = input('Create password\n>')
                    
                    player = Player.create_player(name, password)
                    handler.save_player(player)
                    
                    print('Account created successfully! You are now logged in.')
                    current_user = player 
                    
                case '3':
                    sys.exit('Goodbye!')
                case _:
                    print('Invalid option!')
                    
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"💥 Unexpected error: {e}")


    print(80 * '=' + '\n' + 20 * ' ' + f'You are coming to casino as {current_user.name}\n' + 80 * '=')

if __name__ == '__main__':
    main()