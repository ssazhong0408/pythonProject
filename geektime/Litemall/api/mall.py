import requests
from requests import Response


class Mall:
    def login(self, username, password) -> Response:
        r = requests.post('https://litemall.hogwarts.ceshiren.com/wx/auth/login', json=
        {
            'username': username,
            'password': password
        })
        return r

    def item_search(self, param, head_token):
        r = requests.get('https://litemall.hogwarts.ceshiren.com/wx/goods/list', params=param, headers=head_token)
        return r

    def item_get_detail(self, param, head_token):
        r = requests.get('https://litemall.hogwarts.ceshiren.com/wx/goods/detail', params=param, headers=head_token)
        return r

    def item_add_cart(self, payload, head_token):
        r = requests.post('https://litemall.hogwarts.ceshiren.com/wx/cart/add', json=payload, headers=head_token)
        return r

    def cart_check(self, head_token):
        r = requests.get('https://litemall.hogwarts.ceshiren.com/wx/cart/index', headers=head_token)
        return r
        pass
