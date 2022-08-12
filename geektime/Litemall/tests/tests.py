import requests

from geektime.Litemall.api.get_token import get_token
from geektime.Litemall.api.mall import Mall


class TestMall:

    def setup_class(self):
        self.mall = Mall()

    def setup(self):
        ...

    def test_login(self):
        r = self.mall.login('azhong123', 'azhong123')
        assert r.status_code == 200
        print(r.text)
        print(r.json())
        return r.json()['data']['token']

    def test_item_search(self):
        param = 'keyword=3D&page=1&limit=10&categoryId=0'
        head = {
            'X-Litemall-Token': get_token()
        }
        r = self.mall.item_search(param=param, head_token=head)
        assert r.status_code == 200
        print(r.text)

    def test_item_detail(self):
        param = 'id=1064006'
        head = {
            'X-Litemall-Token': get_token()
        }
        r = self.mall.item_get_detail(param=param, head_token=head)
        assert r.status_code == 200
        print(r.text)

    def test_cart_add(self):
        head = {
            'X-Litemall-Token': get_token()
        }
        json = {
            "goodsId": 1064006,
            "number": 1,
            "productId": 76
        }
        r = self.mall.item_add_cart(payload=json, head_token=head)
        print(r.text)
        assert r.json()['errmsg'] == '成功'

    def test_cart_index(self):
        head = {
            'X-Litemall-Token': get_token()
        }
        r = self.mall.cart_check(head_token=head)
        print(r.text)
        assert r.json()['errmsg'] == '成功'

    def teardown(self):
        ...

    def tear_down(self):
        ...