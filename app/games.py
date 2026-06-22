import random
import time

class Roulette:
    MIN_BET = 10
    MAX_BET = 500
    @staticmethod
    def get_colour(number: int) -> str:
        if number == 0:
            return 'Green🟢'
        return "Red🔴" if (number + (number - 1) // 10) % 2 != 0 else "Black⚫️"
    
    def bet_on_colour(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')

        while True:
            print('\nWelcome to Roulette - bet on colour')
            print('Choose colour (1-3):')
            print('1. Red🔴')
            print('2. Black⚫️')
            print('3. Green🟢')
            colour = input('>')

            if colour not in ['1', '2', '3']:
                print('❌ Wrong option! Choose 1, 2 or 3.')
                continue

            if colour == '1':
                chosen_colour, multiplier = 'Red🔴', 1.8
            elif colour == '2':
                chosen_colour, multiplier = 'Black⚫️', 1.8
            else:
                chosen_colour, multiplier = 'Green🟢', 15.0

            print(f'Your colour is {chosen_colour}')
            confirmed = input('Confirm (y/n): ').lower().strip()

            if confirmed == 'n':
                print('Coming back to Roulette menu...')
                return bet

            if confirmed != 'y':
                print('❌ Wrong option! Enter "y" or "n".')
                continue

            print('Drawing...')
            time.sleep(0.5)
            print('.')
            time.sleep(0.5)
            print('.')
            
            random_number = random.randint(0, 36)
            randomed_colour = Roulette.get_colour(random_number)
            print(f'\nThe ball landed on: {random_number} ({randomed_colour})')

            if randomed_colour == chosen_colour:
                won_prize = int(bet * multiplier)
                print(f'🎉 Congratulations you won! Your total prize is {won_prize}$')
                return won_prize
            else:
                print('😢 You lost, keep trying!')
                return 0 - bet