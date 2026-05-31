import json

with open("config.json") as c:
    load_config = json.load(c)

hook_url = load_config['webhook_url']
download_dir = load_config['download_dir']
movie_dir = load_config['movie_dir']