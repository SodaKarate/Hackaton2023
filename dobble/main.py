import sys

def generate_dobble_cards(numberOfSymbolsOnCard):
    """
    Dobble kártyák generálása a megadott szimbólumok számával.

    Args:
        numberOfSymbolsOnCard (int): A kártyán szereplő szimbólumok száma.

    Returns:
        list: Generált Dobble kártyák listája. Minden kártyát egy lista reprezentál, amely tartalmazza a szimbólumokat.

    """
    symbols = list(range(1, numberOfSymbolsOnCard + 1))

    cards = []

    n = numberOfSymbolsOnCard - 1

    # A Dobble szabályoknak megfelelően generálható kártyák teljes száma
    numberOfCards = n ** 2 + n + 1

    # Első n+1 kártya hozzáadása
    for i in range(n + 1):
        # Új kártya hozzáadása az első szimbólummal
        cards.append([1])
        # n+1 szimbólum hozzáadása a kártyához
        for j in range(n):
            cards[i].append((j + 1) + (i * n) + 1)

    # n darab n szimbólumos kártya hozzáadása
    for i in range(0, n):
        for j in range(0, n):
            # Új kártya hozzáadása 1 szimbólummal
            cards.append([i + 2])
            # n szimbólum hozzáadása a kártyához
            for k in range(0, n):
                val = (n + 1 + n * k + (i * k + j) % n) + 1
                cards[len(cards) - 1].append(val)

    return cards

def print_dobble_cards(cards):
    """
    Dobble kártyák kiírása a konzolra.

    Args:
        cards (list): A Dobble kártyák listája.

    Returns:
        None

    """
    for card in cards:
        line =''
        for number in card:
            line = line + str(number) + " "
        line = line[:-2]
        print(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Használat: python3 main.py <kártyán szereplő szimbólumok száma>\nPl: python3 main.py 5")
        sys.exit(1)

    numberOfSymbolsOnCard = int(sys.argv[1])
    dobble_cards = generate_dobble_cards(numberOfSymbolsOnCard)
    print_dobble_cards(dobble_cards)