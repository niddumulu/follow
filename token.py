import hiveengine.wallet

name = input('Enter wallet name: ')

wallet = hiveengine.wallet.Wallet(name).get_token('starbits')

print('@%s has %s $PIZZA' % (name, wallet['balance']))
