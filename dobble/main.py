import itertools

def generate_dobble_deck(n):
    symbols = list(range(1, n+1))
    deck = []
    
    # Generate the first card with all symbols
    card = symbols.copy()
    deck.append(card)
    
    # Generate the remaining cards
    for i in range(2, n+1):
        # Generate all possible combinations of symbols with size n-1
        combinations = itertools.combinations(symbols, n-1)
        for combination in combinations:
            # Add the current symbol to the combination
            card = list(combination) + [i]
            
            # Check if the current card duplicates any existing card
            is_duplicate = False
            for existing_card in deck:
                if len(set(card) & set(existing_card)) > 0:
                    is_duplicate = True
                    break
            
            # If the current card is unique, add it to the deck
            if not is_duplicate:
                deck.append(card)
    
    return deck

# Main program
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py n")
        sys.exit(1)
    
    n = int(sys.argv[1])
    deck = generate_dobble_deck(n)
    
    # Print the generated deck
    for card in deck:
        print(" ".join(str(symbol) for symbol in card))