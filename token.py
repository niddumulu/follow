import hiveengine.wallet

name = input('Enter wallet name: ')

wallet = hiveengine.wallet.Wallet(name).get_token('STARBITS')

print('@%s has %s $STARBITS' % (name, wallet['balance']))
