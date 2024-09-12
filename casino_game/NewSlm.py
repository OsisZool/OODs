import random
import os
print("Welcome to our Casino")
print('''This is Slot Machine
-------------------------
Symbol\t\t| Payout
-------------------------
🍒  -  -\t| $2
🍒 🍒  -\t| $5
🍒 🍒 🍒\t| $7
🍊 🍊 (🍊or💎)\t| $10
🍇 🍇 (🍇or💎)\t| $14
🍌 🍌 (🍌or💎)\t| $20
💎 💎 💎\t| $250''')

class SlotMachine:
    def __init__(self):
        self.symbols = ["🍒", "🍊", "🍇", "🍌", "💎"]

    def spin(self):
        symbols = random.choices(self.symbols, k=3)
        return symbols

    def calculate_payout(self, symbols):
        symbol_counts = {}
        for symbol in symbols:
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
            
        if "💎" in symbol_counts and symbol_counts["💎"] == 3:
            return 250
        elif "🍒" in symbol_counts:
            count = symbol_counts["🍒"]
            if count == 1:
                return 2
            elif count == 2:
                return 5
            elif count == 3:
                return 7
        elif "💎" in symbol_counts and symbol_counts["💎"] == 1 :
            if "🍊" in symbol_counts and symbol_counts["🍊"] == 2 :
                return 10
            elif "🍇" in symbol_counts and symbol_counts["🍇"] == 2:
                return 14
            elif "🍌" in symbol_counts and symbol_counts["🍌"] == 2:
                return 20
        elif "🍊" in symbol_counts and symbol_counts["🍊"] == 3 :
            return 10
        elif "🍇" in symbol_counts and symbol_counts["🍇"] == 3:
            return 14
        elif "🍌" in symbol_counts and symbol_counts["🍌"] == 3:
            return 20
        return 0

class SlotQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, symbols):
        self.queue.append(symbols)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

if __name__ == "__main__":
    starting_balance = int(input("Enter your initial balance: $"))
    balance = starting_balance
    sumPayout = 0
    slot_machine = SlotMachine()
    slot_queue = SlotQueue()

    while balance > 0:
        bet_amount = int(input("Enter your bet amount (0 to quit): "))
        os.system('cls' if os.name == 'nt' else 'clear')

        if bet_amount == 0:
            break

        if bet_amount > balance:
            print(f"Not enough money! Your balance is: ${balance}")
            continue

        balance -= bet_amount
        symbols = slot_machine.spin()
        payout = slot_machine.calculate_payout(symbols)
        print(f"Symbols: {' '.join(symbols)}\nPayout: ${payout}")
        balance += payout
        sumPayout += payout
        print(f"Your balance is: ${balance}")

        slot_queue.enqueue(symbols)

    print(f"Thank you for playing! You got: ${balance}")
    view_history = input("Do you want to view history? (y/n) : ")
    if view_history == 'y' :
        print("Play History:")
        while True:
            symbols = slot_queue.dequeue()
            if symbols:
                payout = slot_machine.calculate_payout(symbols)
                print(f"Result: {' '.join(symbols)} Payout: ${payout}")
            else:
                break
        print(f"All you got for today is ${sumPayout}")