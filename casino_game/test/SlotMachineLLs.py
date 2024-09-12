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

class Node:
    def __init__(self, symbols, payout):
        self.symbols = symbols
        self.payout = payout
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, symbols, payout):
        new_node = Node(symbols, payout)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # def find_payout(self, symbols):
    #     current = self.head
    #     while current:
    #         if symbols in current.symbols:
    #             return current.payout
    #         current = current.next
    #     return 0

    def find_payout(self, symbols):
        current = self.head
        while current:
            symbol_combinations = current.symbols
            if isinstance(symbol_combinations[0], tuple):
                for combination in symbol_combinations:
                    if all(symbol in symbols for symbol in combination):
                        return current.payout
            else:
                # If there's a single combination for a payout
                if all(symbol in symbols for symbol in symbol_combinations):
                    return current.payout
            current = current.next
        return 0

class SlotMachine:
    def __init__(self):
        self.symbols = ['💎', '🍌', '🍇', '🍊', '🍒']
        self.payout_table = LinkedList()
        self.initialize_payout_table()

    def initialize_payout_table(self):
        self.payout_table.insert(('💎', '💎', '💎'), 250)
        self.payout_table.insert((('🍌', '🍌', '🍌'), ('🍌', '🍌', '💎'), ('🍌', '💎', '🍌'), ('💎', '🍌', '🍌')), 20)
        self.payout_table.insert((('🍇', '🍇', '🍇'), ('🍇', '🍇', '💎'), ('🍇', '💎', '🍇'), ('💎', '🍇', '🍇')), 14)
        self.payout_table.insert((('🍊', '🍊', '🍊'), ('🍊', '🍊', '💎'), ('🍊', '💎', '🍊'), ('💎', '🍊', '🍊')), 10)
        self.payout_table.insert(('🍒', '🍒', '🍒'), 7)
        self.payout_table.insert((('🍒', '🍒', '-'), ('🍒', '-', '🍒'), ('-', '🍒', '🍒')), 5)
        self.payout_table.insert((('🍒', '-', '-'), ('-', '🍒', '-'), ('-', '-', '🍒')), 2)

    def spin(self):
        result = [random.choice(self.symbols) for _ in range(3)]
        print(f"Result: {' '.join(result)}")
        return tuple(result)

    def calculate_payout(self, symbols):
        return self.payout_table.find_payout(symbols)

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
