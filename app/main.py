import sys
from player_data_handler import PlayerHandler, Player
from games import Roulette, SlotMachine, BlackJack
from password_handler import PasswordHandler

def main() -> None:
    print(80 * '=' + '\n' + 30 * ' ' + 'WELCOME TO PYCASINO\n' + 80 * '=')
    
    slot_machine = SlotMachine()
    roulette = Roulette()
    blackjack = BlackJack()
    handler = PlayerHandler()
    current_user = None
    while True:
        try:
            

            while current_user is None:
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
                                break
        
                        
                        if not found_player:
                            raise ValueError(f'Player with name "{name}" not found.')
                        
                        password = input('Enter your password\n>')
                        if not PasswordHandler.verify_password(password, found_player['password']):
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
                        hashed_password = PasswordHandler.hash_password(password)
                        
                        player = Player.create_player(name, hashed_password)
                        handler.save_player(player)
                        
                        print('Account created successfully! You are now logged in.')
                        current_user = player 
                        
                    case '3':
                        sys.exit('Goodbye!')
                    case _:
                        print('Invalid option!')
            print(80 * '=' + '\n' + 20 * ' ' + f'You are coming to casino as {current_user.name}\n' + 80 * '=')
            while True:
                print(f'Your balance: {current_user.balance}$')
                print(f'Games played: {current_user.games_played}')

                print('\nWhat do you want to do(1-5)')
                print('1. Play Roulette🔴⚫️🟢')
                print('2. Play Slot machine🎰')
                print('3. Play BlackJack🃏')
                print('4. Open account manager👤')
                print('5. Exit🔙')

                choice = input('>')

                match choice:
                    case '1':
                        print('What type of roulette do you wanna play(1-5)')
                        print('1. bet on Colour🔴⚫️')
                        print('2. bet on Even/Odd🔢')
                        print('3. bet on dozen📊')
                        print('4. bet on specific number🎯')
                        print('5. Exit to menu🔙')
                        type_of_roulette = input('>')
                        match type_of_roulette:
                            case '1':
                                print(f'Your balance {current_user.balance}$')
                                bet = int(input('How much do you wanna bet\n>'))
                                won_prize = roulette.bet_on_colour(bet)
                                current_user.balance += won_prize
                                current_user.games_played += 1
                                handler.save_player(current_user)
                            case '2':
                                print(f'Your balance {current_user.balance}$')
                                bet = int(input('How much do you wanna bet\n>'))
                                won_prize = roulette.bet_on_even_odd(bet)
                                current_user.balance += won_prize
                                current_user.games_played += 1
                                handler.save_player(current_user)
                            case '3':
                                print(f'Your balance {current_user.balance}$')
                                bet = int(input('How much do you wanna bet\n>'))
                                won_prize = roulette.bet_on_dozen(bet)
                                current_user.balance += won_prize
                                current_user.games_played += 1
                                handler.save_player(current_user)
                            case '4':
                                print(f'Your balance {current_user.balance}$')
                                bet = int(input('How much do you wanna bet\n>'))
                                won_prize = roulette.bet_on_number(bet)
                                current_user.balance += won_prize
                                current_user.games_played += 1
                                handler.save_player(current_user)
                            case '5':
                                print('Coming back to menu')
                            case _:
                                raise ValueError('Wrong option')
                    case '2':
                        print(f'Your balance {current_user.balance}$')
                        bet = int(input('How much do you wanna bet\n>'))
                        won_prize = slot_machine.play(bet)
                        current_user.balance += won_prize
                        current_user.games_played += 1
                        handler.save_player(current_user)
                    case '3':
                        print(f'Your balance {current_user.balance}$')
                        bet = int(input('How much do you wanna bet\n>'))
                        won_prize = blackjack.play(bet)
                        current_user.balance += won_prize
                        current_user.games_played += 1
                        handler.save_player(current_user)
                    case '4':
                        print('What do you want do to with your account(1-5)')
                        print('1. Load balance💸')
                        print('2. Log out↩️')
                        print('3. Delete account❌')
                        print('4. Change password🔐')
                        print('5. Exit to menu🔙')
                        option = input('>')

                        match option:
                            case '1':
                                amount = int(input('How many do you want to load\n>'))
                                current_user.load_balance(amount)
                                handler.save_player(current_user)
                            
                            case '2':
                                print('Logging out')
                                current_user = None
                                break
                            case '3':
                                handler.delete_account(current_user.id)
                                print('Account deleted succesfully')
                                current_user = None
                                break
                            case '4':
                                new_password = input('Write new password\n>')
                                handler.change_password(current_user.id, new_password)
                                print('Password changed succesfully!')
                                current_user = None
                                break
                            case '5':
                                print('Coming back to menu')
                            case _:
                                raise ValueError('Wrong option')  
                    case '5':
                        sys.exit('Goodbye!')
                    case _:
                        raise ValueError('Wrong option')
        except ValueError as e:
                    print(f"❌ Error: {e}")
        except Exception as e:
            print(f"💥 Unexpected error: {e}")

        

if __name__ == '__main__':
    main()