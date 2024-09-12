import random

class Symbol:
    def __init__(self, symbol, payout):
        self.symbol = symbol
        self.payout = payout

class SlotMachine:
    def __init__(self, symbols):
        self.symbols = symbols
        
    def spin(self):
        return [random.choice(self.symbols) for _ in range(3)]
    
    def calculate_payout(self, result):
        symbol_counts = {}
        for symbol in result:
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

def main():
    symbols = ["🍒", "🍊", "🍇", "🍌", "💎"]
    slot_machine = SlotMachine(symbols)
    
    print("Welcome to our Casino")
    print('''This is Slot Machine
-------------------------
Symbol\t\t| Payout
-------------------------
🍒  -  -\t\t| $2
🍒 🍒  -\t\t| $5
🍒 🍒 🍒\t\t| $7
🍊 🍊 (🍊 or 💎)\t| $10
🍇 🍇 (🍇 or 💎)\t| $14
🍌 🍌 (🍌 or 💎)\t| $20
💎 💎 💎\t\t| $250
''')
    
    credits = int(input("Enter your initial credits: "))
    
    while credits > 0:
        
        bet = int(input("Enter your bet (0 to quit): $"))
        if bet == 0:
            break
        if bet > credits:
            print("Insufficient credits. Please place a lower bet.")
            continue
        result = slot_machine.spin()
        print(" ".join(result))
        payout = slot_machine.calculate_payout(result)
        credits += payout - bet
        print(f"Payout: ${payout}")
        print(f"Total credits: ${credits}")
        
    print(f"Thank you for playing! You got ${credits}!")

if __name__ == "__main__":
    main()
