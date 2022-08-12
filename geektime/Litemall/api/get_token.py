import requests


def get_token():
    res = requests.post('https://litemall.hogwarts.ceshiren.com/wx/auth/login', json={
        "username": "azhong123",
        "password": "azhong123"
    })
    token = res.json()['data']['token']
    return token


if __name__ == 'main':
    print(get_token())
