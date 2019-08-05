import requests

_QUOTE_URL = 'https://quotes.rest/qod'

def get_random_quote():
    """Get a random quote."""

    res = requests.get(_QUOTE_URL)
    return res.json()['contents']['quotes'][0]['quote']

def display_quote():
    """Display a random quote."""

    print(f'My random quote is: "{get_random_quote()}"')

if __name__ == '__main__':
    display_quote()
