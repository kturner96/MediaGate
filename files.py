from pathlib import Path
from configs import download_dir, movie_dir
import shutil

def move_files():
    p = Path(download_dir)
    target_files = list(p.rglob('*.{[mM][pP]4,[mM][kK][vV]}'))

    moved_files_list = []

    for p in target_files:
        default_name = p.stem
        words = default_name.split(".")
        title_words = words[0:2]
        final_title = " ".join(title_words)

        destination_path = Path(movie_dir) / f"{final_title}{p.suffix}"

        shutil.move(p, destination_path)

        moved_files_list.append(final_title)
        
    return moved_files_list