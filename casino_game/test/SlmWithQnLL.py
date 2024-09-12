from queue import Queue
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

class Player:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.bet_history_queue = Queue()  # Queue สำหรับประวัติการเดิมพันแบบ FIFO
        self.bet_history_linked_list = LinkedList()  # Linked List สำหรับประวัติการเดิมพันแบบเชื่อมต่อ

    def bet(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.bet_history_queue.put(amount)  # เพิ่มข้อมูลใน Queue
            self.bet_history_linked_list.append(amount)  # เพิ่มข้อมูลใน Linked List
            return amount
        else:
            print("Insufficient balance!")
            return 0

    def add_winnings(self, amount):
        self.balance += amount
        self.bet_history_queue.put(amount)  # เพิ่มข้อมูลใน Queue
        self.bet_history_linked_list.append(amount)  # เพิ่มข้อมูลใน Linked List

    def display_balance_history(self):
        print("Queue-based Balance History:")
        while not self.bet_history_queue.empty():
            bet_amount = self.bet_history_queue.get()
            print(f'bet: {bet_amount}')
        print("End of history.")

        print("Linked List-based Balance History:")
        self.bet_history_linked_list.display()
        print("End of history.")

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
    player.display_balance_history()

if __name__ == "__main__":
    main()
