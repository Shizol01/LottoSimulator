import random

def input_numbers():
    '''Takes numbers from player until 6 correct numbers are collected.
    No double numbers, no numbers outside of range 1 to 49, no crashing with other inputs.

    :rtype: int list
    :return: list of int numbers choosen by player
    '''
    numbers = []
    while len(numbers) < 6:
        number = input("Enter a number: ")
        if not number.isdigit():
            print("Please enter a number")
            continue
        number = int(number)
        if number < 1 or number > 49:
            print("Please choose a number between 1 and 49")
            continue
        if number in numbers:
            print("You have already entered the number")
            continue
        numbers.append(int(number))
    return sorted(numbers)







def lotto():
    '''Main function of game
    It randomizes list of 6 numbers from 1 to 49 and check if player matched numbers.

    :rtype: string + int list
    :return: Gives 3 lines. player numbers, random numbers and matched numbers.
    '''
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        random_number = random.randint(1, 49)
        lotto_numbers.append(random_number)
    lotto_numbers.sort()

    player_numbers = input_numbers()
    hits = 0
    for i in range(len(lotto_numbers)):
        if player_numbers[i] == lotto_numbers[i]:
            hits += 1
    print(f"Your numbers was {player_numbers}")
    print(f"Wining numbers was {lotto_numbers}")
    print(f"You matched {hits} numbers in total!")

if __name__ == "__main__":
    lotto()





