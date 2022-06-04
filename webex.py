import requests
import json


def main():
    notif = input("enter message: ")
    input_message = notif
    access_token = 'N2E3ZjNiOTEtMjRiNC00YWJmLWJhZmQtOTU3YjZhOTAxZDU4OGNmMTgwZmYtMmI4_P0A1_b982ef45-7539-41ce-a74b-a59496977693'
    room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYWRlM2UwZjAtYjYzNC0xMWVjLWE4NzAtNTNjMGU2ZTEzOWU4'
    message = input_message
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())


if __name__ == '__main__':
    main()