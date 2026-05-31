#!/usr/bin/env python3
import requests
import time
from configs import *
from files import move_files

while True:
        moved_files = move_files()

        titles_sentence = ", ".join(moved_files)

        if moved_files:
                move_successful = {'content': f'🎬 **{titles_sentence}** {"is" if len(moved_files) == 1 else "are"} ready to watch on Plex!',
                # 'username': 'MediaGate',
                }
                requests.post(hook_url, json = move_successful)
                print(f"Notified Discord: {titles_sentence} moved.")
        else:
                print("Checking folder... nothing to move.")
        time.sleep(30)