ombor= {
    'adrenaline':{'narxi':200,'soni':20},
    'coca-cola':{'narxi':10000,'soni':30},
    'morojniy':{'narxi':20000,'soni':10},

}
jonatma={}

def update(name,price,quantity):
    global ombor
    ombor[name] = {'narxi':price,'soni':quantity}

if __name__ == '__main__':
    update('coca-cola',10000,30)