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
    
    @staticmethod
    def get_even_odd(number: int) -> str:
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
    
    @staticmethod
    def get_dozen(number: int) -> int:
        if 1 <= number <= 12:
            return 1
        if 13 <= number <= 24:
            return 2
        if 25 <= number <= 36:
            return 3
        if number == 0:
            return 0
    
    def bet_on_colour(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')

        while True:
            print('\n ==== 🔴⚫️Welcome to Roulette - bet on colour⚫️🔴 ====')
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
            

    def bet_on_even_odd(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')
        
        while True:
            print('\n ==== 🔢Welcome to Roulette - bet on Even/Odd🔢 =====')
            print('Choose option (1-2):')
            print('1. Even')
            print('2. Odd')
            even_odd = input('>')

            if even_odd not in ['1', '2']:
                print('❌ Wrong option! Choose 1, 2')
                continue

            if even_odd == '1':
                chosen, multiplier = 'Even', 1.8
            else:
                chosen, multiplier = 'Odd', 1.8
    
            print(f'Your choice is {chosen}')
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
            randomed_even_odd = Roulette.get_even_odd(random_number)
            print(f'\nThe ball landed on: {random_number} [{randomed_even_odd}] ({randomed_colour})')

            if randomed_even_odd == even_odd:
                won_prize = int(bet * multiplier)
                print(f'🎉 Congratulations you won! Your total prize is {won_prize}$')
                return won_prize
            else:
                print('😢 You lost, keep trying!')
                return 0 - bet
    
    def bet_on_dozen(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')
        
        while True:
            print('\n==== 📊Welcome to Roulette - bet on dozen📊 ====')
            print('Choose dozen (1-3):')
            print('1. First (1-12)')
            print('2. Second (13-24)')
            print('3. Third (25-36)')
            dozen = input('>')

            if dozen not in ['1', '2', '3']:
                print('❌ Wrong option! Choose 1, 2, 3')
                continue

            if dozen == '1':
                chosen, multiplier = 1 , 2.5
            elif dozen == '2':
                chosen, multiplier = 2, 2.5
            elif dozen == '3':
                chosen, multiplier = 3, 2.5
    
            print(f'Your choice is {chosen}')
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
            randomed_dozen = Roulette.get_dozen(random_number)
            print(f'\nThe ball landed on: {random_number} [{randomed_dozen}] ({randomed_colour})')

            if randomed_dozen == chosen:
                won_prize = int(bet * multiplier)
                print(f'🎉 Congratulations you won! Your total prize is {won_prize}$')
                return won_prize
            else:
                print('😢 You lost, keep trying!')
                return 0 - bet
    
    def bet_on_number(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')
        
        while True:
            print('==== 🎯Welcome to Roulette - bet on number🎯 ====')
            print('Choose number (0-36):')
            number = int(input('>'))

            if number not in range(0, 36):
                print('❌ Wrong option! Choose 0-36')
                continue

            multiplier = 35
    
            print(f'Your choice is {number}')
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

            if random_number == number:
                won_prize = int(bet * multiplier)
                print(f'🎉 Congratulations you won! Your total prize is {won_prize}$')
                return won_prize
            else:
                print('😢 You lost, keep trying!')
                return 0 - bet
    
class SlotMachine:
    MIN_BET = 10
    MAX_BET = 500
    CHERRY = '🍒'
    LEMON = '🍋'
    BELL = '🔔'
    DIAMOND = '💎'
    symbols = [CHERRY, CHERRY, LEMON, LEMON, LEMON, LEMON, BELL, DIAMOND, CHERRY, CHERRY, LEMON, LEMON, LEMON, LEMON, BELL]

    def play(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')

        print('====== 🎰WELCOME TO SLOT MACHINE🎰 ======')
        print('Spinning the reels...')

        reel1 = random.choice(self.symbols)
        reel2 = random.choice(self.symbols)
        reel3 = random.choice(self.symbols)

        time.sleep(1)
        print(f'[ {reel1} ]', end='', flush=True)
        time.sleep(1)
        print(f'[ {reel2} ]', end='', flush=True)
        time.sleep(1)
        print(f'[ {reel3} ]\n')
        time.sleep(1)

        if reel1 == reel2 == reel3:
            if reel1 == self.DIAMOND:
                multiplier = 25
            elif reel1 == self.BELL:
                multiplier = 10
            elif reel1 == self.CHERRY:
                multiplier = 5
            else:
                multiplier = 2
            
            won_prize = int(bet * multiplier)
            print(f'🎉 JACKPOT! 3x {reel1}! You won {won_prize}$')
            return won_prize
        
        elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
            won_prize = int(bet * 1.5)
            print(f'👍 Nice! 2x matching symbols. You won {won_prize}$')
            return won_prize

        else:
            print('😢 No luck this time. Keep trying!')
            return 0 - bet

class BlackJack:
    MIN_BET = 10
    MAX_BET = 500

    def _create_deck(self) -> list[str]:
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = ranks * 4
        random.shuffle(deck)
        return deck
    
    def _calculate_score(self, hand: list[str]) -> int:
        score = 0
        aces = 0

        for card in hand:
            if card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                score += 11
                aces += 1
            else:
                score += int(card)
        
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        
        return score
    
    def play(self, bet: int) -> int:
        if self.MIN_BET > bet or self.MAX_BET < bet:
            raise ValueError(f'Bet must be between {self.MIN_BET}$ and {self.MAX_BET}$')
        
        deck = self._create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print('==== 🃏WELCOME TO BLACKJACK🃏 ====')

        while True:
            player_score = self._calculate_score(player_hand)
            print(f'\nYour cards: {player_hand} (Score: {player_score})')
            print(f'Dealer\'s visible card: {dealer_hand[0]}')

            if player_score == 21:
                print('✨ Blackjack!')
                break
            if player_score > 21:
                print('💥 Bust! You went over 21.')
                print(f'You lost {bet}$')
                return 0 - bet
            
            choice = input('Do you want to (1)Hit or (2)Stand\n>')

            if choice == '1':
                print('Drawing card...')
                time.sleep(0.5)
                player_hand.append(deck.pop())
            elif choice == '2':
                break
            else:
                print('❌ Invalid option! Choose 1 or 2.')

        print(f'\nDealer reveals hidden card: {dealer_hand}')
        dealer_score = self._calculate_score(dealer_hand)

        while dealer_score < 17:
            print('Dealer draws a card...')
            time.sleep(0.8)
            dealer_hand.append(deck.pop())
            dealer_score = self._calculate_score(dealer_hand)
            print(f'Dealer\'s cards: {dealer_hand} (Score: {dealer_score})')

        print(f'\nFinal Standings:')
        print(f'➡️ You: {player_score}')
        print(f'➡️ Dealer: {dealer_score}')

        if dealer_score > 21:
            print('🎉 Dealer busted! You win!')
            print(f'You won {int(bet) * 2}$')
            return int(bet * 2)
        elif player_score > dealer_score:
            print('🎉 You win!')
            print(f'You won {int(bet) * 2}$')
            return int(bet * 2)
        elif player_score < dealer_score:
            print('😢 Dealer wins!')
            print(f'You lost {bet}$')
            return 0 - bet
        else:
            print('🤝 It\'s a tie (Push)! Your bet is returned.')
            return 0