# modules import
import random

# constant regarding the maximum number of lines of the slot machine
MAX_LINES = 3
# constant regarding the maximum number allowed for a bet
MAX_BET = 100
# constant regarding the minimum number allowed for a bet
MIN_BET = 1

# number of rown and columns for the slot machine
ROWS = 3
COLS = 3

# how many symbols should be in total
symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6, 
    "D": 8
}

# the value of each symbol to multiply the bet
symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3, 
    "D": 2
}

# check how the user can win
def check_winnings(columns, line, bet, values):
    winnings = 0
    symbol = columns[0][line - 1]
    for column in columns:
        symbol_to_check = column[line - 1]
        if symbol != symbol_to_check:
            break
    else:
        winnings += values[symbol] * bet

    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    # store all items from the dictionary into a list of symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    # generate the columns of the slot machine
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            # remove values in order to not repeat values over the limits of the dictionary
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)

    return columns

# transpose the elements of the matrix to resemble a slot machine
def print_slot_machine(columns):
    try:
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" | ")
                else: 
                    print(column[row], end="")
            print()
    except IndexError:
        print("There are not values in the matrix.")


# ask input from the user regarding the deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_line():
    while True:
        line = input(f"Enter the line to bet on: ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Enter a valid number for line.")
        else:
            print("Please enter a number.")

    return line

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between {MIN_BET} - {MAX_BET}.".format(MIN_BET = MIN_BET, MAX_BET=MAX_BET))
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    line = get_line()
    while True:
        bet = get_bet()
        
        if bet > balance:
            print("You do not have enough to bet that amount. You current balance is ${balance}".format(balance = balance))
        else:
            break
    
    print("You are betting ${bet} on {lines} line. Total bet is equal to: ${total}".format(bet = bet, lines= line, total = bet))

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings = check_winnings(slots, line, bet, symbol_value)
    print(f"You won ${winnings}.")

    return winnings - bet

if __name__ == "__main__":
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")
