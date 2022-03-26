import beem
import getpass
import sys

name = input('enter your account name: ')
posting_key = getpass.getpass(prompt='enter your private posting key: ')


hive = beem.Hive(keys=[posting_key])

try:
    account = beem.account.Account(name, blockchain_instance=hive)
except beem.exceptions.AccountDoesNotExistsException:
    print('Error! Invalid wallet name')
    sys.exit(1)

try:
    account.follow('ojak') 
except beem.exceptions.MissingKeyError:
    print('Error! Incorrect private posting key')
    sys.exit(1)


print('Done! Ive followed ojak')
