import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def show_banner():
    print("\n========================")
    print("      SLOT MANIAC 🎰")
    print("========================\n")


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_char = " | " if i != len(columns) - 1 else ""
            print(column[row], end=end_char)
        print()


def deposit():
    while True:
        amount = input("Enter deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("Invalid input.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
        print("Invalid number of lines.")


def get_bet():
    while True:
        amount = input(f"Bet per line (${MIN_BET}-${MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
        print("Invalid bet amount.")


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not enough balance. Current balance: ${balance}")
        else:
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_values)

    print(f"\nYou won: ${winnings}")
    print("Winning lines:", *winning_lines if winning_lines else "None")

    return winnings - total_bet


def main():
    show_banner()

    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")

        balance += spin(balance)

        print(f"New balance: ${balance}")

        if balance <= 0:
            print("You're out of money.")
            break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


main()
