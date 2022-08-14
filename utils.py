import requests
import click
import os
import sys


ACCOUNT = os.environ['ACCOUNT']
PASSWORD = os.environ['PASSWORD']

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://femascloud.com',
    'Pragma': 'no-cache',
    'Referer': 'https://femascloud.com/swag/accounts/login',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def initialize():
    session = requests.Session()
    session.head('https://femascloud.com/swag/accounts/login')
    session.post(
        'https://femascloud.com/swag/Accounts/login',
        headers=headers,
        data={
            'data[Account][username]': ACCOUNT,
            'data[Account][passwd]': PASSWORD,
            'data[remember]': 0
        },
        cookies=session.cookies,
    )
    return session


def punch_in():
    print('punch_it')
    session = initialize()
    session.post(
        'https://femascloud.com/swag/users/clock_listing',
        headers=headers,
            data={
            '_method': 'POST',
            'data[ClockRecord][user_id]': '22',
            'data[AttRecord][user_id]': '22',
            'data[ClockRecord][shift_id]': '2',
            'data[ClockRecord][period]': '1',
            'data[ClockRecord][clock_type]': 'S',
        },
        cookies=session.cookies,
    )


def punch_out():
    print('punch_out')
    session = initialize()
    session.post(
        'https://femascloud.com/swag/users/clock_listing',
        headers=headers,
            data={
            '_method': 'POST',
            'data[ClockRecord][user_id]': '22',
            'data[AttRecord][user_id]': '22',
            'data[ClockRecord][shift_id]': '2',
            'data[ClockRecord][period]': '1',
            'data[ClockRecord][clock_type]': 'E',
        },
        cookies=session.cookies,
    )


@click.command()
@click.option('--mode', default='in', help='in/out')
def attentance(mode: str=None):
    {
        'in': punch_in,
        'out': punch_out,

    }[mode]()

if __name__ == '__main__':
    attentance()
