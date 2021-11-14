import requests


class Selection:
    def __init__(self, item, size, amount):
        self.item = item
        self.size = size
        self.amount = amount

def printItems(products):
    for product in products['products']:
        for variant in product['variants']:
            print(product['title'] + " " + variant['option1'] + " " + str(variant['available']))
       

def findItem(item, size, products):
    for product in products['products']:
        for variant in product['variants']:
            if (product['title'] == item and variant['option1'].lower() == size.lower() and variant['available'] == True):
                print("Item is available")
                return True
    return False

def open():
    a = requests.get("https://shop.palaceskateboards.com/products/z4ozkwjd6d57")
    print(a.text)

def main():
    s1 = Selection('YE OLDE HOOD WHITE', 'Small', 1)
    r = requests.get('https://shop-usa.palaceskateboards.com/products.json')
    products = r.json()
    #printItems(products)
    #findItem(s1.item, s1.size, products)
    open()


main()

