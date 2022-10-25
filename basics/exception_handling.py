
def set_quantity():
    try:
        quantity=int(input('Enter your Stock'))
    except:
        print('unsupported characters')
    else:
        print('stock is quantity is:'+str(quantity))

set_quantity()