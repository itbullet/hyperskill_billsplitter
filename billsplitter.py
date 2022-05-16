import random


def check_input(number_str):
    try:
        number = int(number_str)
    except ValueError:
        return 0
    return number


def bill_split():
    number_of_friends = check_input(input('Enter the number of friends joining (including you):\n'))
    if number_of_friends > 0:
        print('Enter the name of every friend (including you), each on a new line:')
        friends_list = {input(): 0 for _ in range(number_of_friends)}
        print('Enter the total bill value:')
        total_bill_value = int(input())
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        if input() == 'Yes':
            random_friend = random.choice(list(friends_list))
            print(f'{random_friend} is the lucky one!')
            split_value = round(total_bill_value / (number_of_friends - 1), 2)
            friends_list = {friend: split_value if friend != random_friend else 0 for friend in friends_list}
        else:
            print(f'No one is going to be lucky')
            split_value = round(total_bill_value / number_of_friends, 2)
            friends_list = {friend: split_value for friend in friends_list}
        print(friends_list)
    else:
        print('No one is joining for the party')


if __name__ == '__main__':
    bill_split()
