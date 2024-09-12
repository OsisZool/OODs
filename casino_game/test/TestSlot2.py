import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def is_empty(self):
        return not self.head

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

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
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.bet_history = LinkedList()

    def bet(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.bet_history.append(amount)
            return amount
        else:
            print("Insufficient balance!")
            return 0

    def add_winnings(self, amount):
        self.balance += amount
        self.bet_history.append(amount)

    def display_balance_history(self):
        print("Balance History:")
        self.bet_history.display()

def main():
    initial_balance = int(input("Enter your initial balance: "))
    player = Player(initial_balance)
    slot_machine = SlotMachine()

    while player.balance > 0:
        print("\nNew Round:")
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

    print(f"\nThank you for playing! You got ${player.balance}!")
    view_history = input("Do you want to view balance history? (y/n): ")
    if view_history.lower() == 'y':
        player.display_balance_history()

if __name__ == "__main__":
    main()
