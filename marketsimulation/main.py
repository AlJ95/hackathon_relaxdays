from api_handler import API

# TODO: Readme

if __name__ == "__main__":
    articles = requests.get(f"{API_URL}{GET_ALL_ARTICLES}")
    player = requests.get(f"{API_URL}{GET_PLAYERS}")

