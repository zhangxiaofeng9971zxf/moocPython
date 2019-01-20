Money = input()
if  Money[0:3] in ['RMB']:
    USD = (eval(Money[3:])/6.78)
    print('USD{:.2f}'.format(USD))




elif Money[0:3] in ['USD']:
    RMB = 6.78*eval(Money[3:])
    print('RMB{:.2f}'.format(RMB))

