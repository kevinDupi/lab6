def encode(password):
    pList = list(password)
    for letter in range(len(pList)):
        pList[letter] = str(int(pList[letter]) + 3)
        if int(pList[letter]) >= 10:
            pList[letter] = str(int(pList[letter]) - 10)

    finalPassword = "".join(pList)
    return finalPassword

#commented this out to make my own
def decode(password):
    pList = list(password)
    for letter in range(len(pList)):
        pList[letter] = str(int(pList[letter]) - 3)
        if int(pList[letter]) < 0:
            pList[letter] = str(int(pList[letter])+10)



    finalPassword = "".join(pList)
    return finalPassword



def main():
    password = ''

    while True:
        print('Menu')
        print('------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()

        option = input('Please enter an opiton: ')
        if option == '1':
            password = input('Please enter a password: ')
            password = encode(password)
            print('Your password has been encoded and stored!')

        elif option == '2':
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
        elif option == '3':
            exit()

        print()

if __name__ == '__main__':
    main()

