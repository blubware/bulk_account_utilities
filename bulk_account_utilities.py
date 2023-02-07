import random, string
from clear_screen import clear

options = r'''[1] Username Generator
[2] Password Generator
[3] Email Generator
[4] Email/Password/Username Generator
'''

charset_options = r'''[1] 1A$
[2] 1A
'''

with open('input/names.txt') as file:
    names = file.readlines()

def bulk_account_utilities():
    try:
            
        clear()
        print(options)

        choice = input('Choice: ')
        match choice:

            case '1':
                amount = int(input('Amount: '))
                for _ in range(int(amount)):

                    name = random.choice(names).strip()
                    lastname = random.choice(names).strip()
                    number = random.randint(20, 99)

                    username = f'{name}_{lastname}_{number}'
                    
                    print(username)
                    with open('output/usernames.txt', 'a') as file:
                        file.write(f'{username}\n')

            case '2':
                amount = int(input('Amount: '))

                print(charset_options)
                charset = input('Charset: ')
                length = int(input('Length: '))
                
                match charset:
                    case '1':
                        for _ in range(int(amount)):
                            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)for _ in range(length))

                            print(password)

                            with open('output/passwords.txt', 'a') as passwords:
                                passwords.write(f'{password}\n')
                        
                        for _ in range(int(amount)):
                            password = ''.join(random.choice(string.ascii_letters + string.digits)for _ in range(length))

                            print(password)

                            with open('output/passwords.txt', 'a') as passfilewords:
                                file.write(f'{password}\n')
        
            case '3':
                amount = int(input('Amount: '))

                provider = input('Provider: ')

                for _ in range(int(amount)):
                    name = random.choice(names).strip()
                    lastname = random.choice(names).strip()
                    number = random.randint(20, 99)

                    email = f'{name}_{lastname}_{number}@{provider}'
                    
                    print(email)
                    with open('output/emails.txt', 'a') as file:
                        file.write(f'{email}\n')

            case '4':
                amount = int(input('Amount: '))

                provider = input('Provider: ')

                for _ in range(int(amount)):
                    name = random.choice(names).strip()
                    lastname = random.choice(names).strip()
                    number = random.randint(20, 99)

                    email = f'{name}_{lastname}_{number}@{provider}'
                    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)for _ in range(16))
                    username = f'{name}_{lastname}_{number}'
                    
                    epu = f'{email}:{username}:{password}'

                    print(epu)

                    with open('output/email_password_usernames.txt', 'a') as file:
                        file.write(f'{epu}\n')

            case _:
                input(f'\'{choice}\' isn\' an option, press enter to try again')
                bulk_account_utilities()
        clear()
        
            

        bulk_account_utilities()

    except KeyboardInterrupt:
        bulk_account_utilities()

if __name__ == '__main__':
    bulk_account_utilities()