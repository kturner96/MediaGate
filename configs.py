import json

with open("config.json") as c:
    load_config = json.load(c)

hook_url = load_config['webhook_url']
media_dir = load_config['media_dir']
movie_dir = load_config['movie_dir']