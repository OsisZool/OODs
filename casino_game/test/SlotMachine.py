import random

print('''Welcome to our Casino
This is Slot Machine
-------------------------
Symbol\t\t| Payout
-------------------------
🍒  -  -\t| $2
🍒 🍒  -\t| $5
🍒 🍒 🍒\t| $7
🍊 🍊 🍊 or 💎\t| $10
🍇 🍇 🍇 or 💎\t| $14
🍌 🍌 🍌 or 💎\t| $20
💎 💎 💎\t| $250
''')

class SlotMachine:
    def __init__(self):
        self.symbols = ['💎', '🍌', '🍇', '🍊', '🍒']
        self.payout_table = {
            (('🍌', '🍌', '🍌'), ('🍌', '🍌', '💎'), ('🍌', '💎', '🍌'), ('💎', '🍌', '🍌')): 20,
            (('🍇', '🍇', '🍇'), ('🍇', '🍇', '💎'), ('🍇', '💎', '🍇'), ('💎', '🍇', '🍇')): 14,
            (('🍊', '🍊', '🍊'), ('🍊', '🍊', '💎'), ('🍊', '💎', '🍊'), ('💎', '🍊', '🍊')): 10,
            (('🍒', '🍒', '🍒'),('🍒', '🍒', '🍒'),('🍒', '🍒', '🍒')): 7,
            (('🍒', '🍒', '-'), ('🍒', '-', '🍒'), ('-', '🍒', '🍒')): 5,
            (('🍒', '-', '-'), ('-', '🍒', '-'), ('-', '-', '🍒')): 2,
            (('💎','💎','💎'),('💎','💎','💎'),('💎','💎','💎')): 250
        }

    def spin(self):
        result = [random.choice(self.symbols) for _ in range(3)]
        print(f"Result: {' '.join(result)}")
        return tuple(result)
    
    def calculate_payout(self, symbols):
        unsorted_symbols = tuple(symbols)
        sorted_symbols = tuple(sorted(symbols))

        for pattern, payout in self.payout_table.items():
            if unsorted_symbols in pattern or sorted_symbols in pattern:
                return payout
        return 0

class Player:
    def __init__(self, balance):
        self.balance = balance

    def bet(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print("Insufficient balance!")
            return 0

    def add_winnings(self, amount):
        self.balance += amount

def main():
    initial_balance = int(input("Enter your initial balance: "))
    player = Player(initial_balance)
    slot_machine = SlotMachine()

    while player.balance > 0:
        bet_amount = int(input("Enter your bet amount (0 to quit): "))
        if bet_amount == 0:
            break

        bet = player.bet(bet_amount)
        if bet == 0:
            continue

        symbols = slot_machine.spin()
        payout = slot_machine.calculate_payout(symbols)
        print(f"Payout: {payout}")
        player.add_winnings(payout)

        print(f"Current balance: {player.balance}")

    print(f"Thank you for playing! You got ${player.balance}!")

if __name__ == "__main__":
    main()