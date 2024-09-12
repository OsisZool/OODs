import random

class Slot:
    def __init__(self, symbol):
        self.symbol = symbol
        self.next_slot = None

class CircularLinkedList:
    def __init__(self, symbols):
        self.head = Slot(symbols[0])
        current_slot = self.head
        for symbol in symbols[1:]:
            new_slot = Slot(symbol)
            current_slot.next_slot = new_slot
            current_slot = new_slot
        current_slot.next_slot = self.head

    def shuffle_symbols(self):
        symbols = []
        current_slot = self.head
        while True:
            symbols.append(current_slot.symbol)
            current_slot = current_slot.next_slot
            if current_slot == self.head:
                break
        random.shuffle(symbols)
        current_slot = self.head
        for symbol in symbols:
            current_slot.symbol = symbol
            current_slot = current_slot.next_slot

class SlotMachine:
    def __init__(self):
        self.symbols = CircularLinkedList(['💎', '🍌', '🍇', '🍊', '🍒'])
        self.payout_table = {
            ('💎', '💎', '💎'): 250,
            (('🍌', '🍌', '🍌'), ('🍌', '🍌', '💎'), ('🍌', '💎', '🍌'), ('💎', '🍌', '🍌')): 20,
            (('🍇', '🍇', '🍇'), ('🍇', '🍇', '💎'), ('🍇', '💎', '🍇'), ('💎', '🍇', '🍇')): 14,
            (('🍊', '🍊', '🍊'), ('🍊', '🍊', '💎'), ('🍊', '💎', '🍊'), ('💎', '🍊', '🍊')): 10,
            ('🍒', '🍒', '🍒'): 7,
            (('🍒', '🍒', '-'), ('🍒', '-', '🍒'), ('-', '🍒', '🍒')): 5,
            (('🍒', '-', '-'), ('-', '🍒', '-'), ('-', '-', '🍒')): 2
        }

    def spin(self):
        self.symbols.shuffle_symbols()
        result = []
        current_slot = self.symbols.head
        for _ in range(3):
            result.append(current_slot.symbol)
            current_slot = current_slot.next_slot
        print(f"Result: {' '.join(result)}")
        return tuple(result)

    def calculate_payout(self, symbols):
        max_payout = 0
        for pattern, payout in self.payout_table.items():
            count = 0
            for symbol in symbols:
                if symbol in pattern:
                    count += 1
            if count == 3:
                max_payout = max(max_payout, payout)
            elif count == 2:
                max_payout = max(max_payout, payout // 2)  # Payout for two matching symbols
        return max_payout

class Player:
    def __init__(self, balance):
        self.balance = balance

    def bet(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print(f"Insufficient balance! Your balance is {self.balance}")
            return 0

    def add_winnings(self, amount):
        self.balance += amount

def main():
    print('''Welcome to our Casino
This is Slot Machine
This is pay out
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

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
