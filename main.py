import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        won = True
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                won = False
                break

        if won:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current)
            current.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")   #end \n kimi seydi
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Please, enter the amount of deposit $")
        if amount.isdigit():     #isdigit methodu negativeleri goturmur deye else e dusecek ve sehv mesaj
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be positive")
        else:
            print("Please enter a number (not a string)")

    return amount

def number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number (not a string)")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():     #isdigit methodu negativeleri goturmur deye else e dusecek ve sehv mesaj
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number (not a string)")

    return amount

def spin(balance):
    lines = number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}")
    print(balance, lines)


    slots = get_slot_machine_spin( ROWS, COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print("You won on lines:", *winning_lines)   #splat operator
    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit) ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()