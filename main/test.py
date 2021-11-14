import requests


def add(id, qty):
    s= requests.Session()
    payload = {
        'id': id,
        'quantity': qty
    }
    res=s.post('https://shop.palaceskateboards.com/cart/add.js', data = payload)
    print(res.content)
    print(res.status_code)

add(39394702262349, 1)