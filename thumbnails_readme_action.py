from thumbnails_readme import thumbnails_readme
import os
from pathlib import Path

# Maximum thumbnail size - reduce to reduce final thumbnail size
MAX_SIZE = (128, 128)
# PDF quality, lower the number, lower the quality
pdf_quality = 15

# Linux
poppler_path = None

# path
#path = os.getcwd()
#path = os.path.dirname(path)
path = os.getenv('GITHUB_WORKSPACE')

# Do not forget to add your path to image thumbnails folder
skiplist = (
    ".git",
    ".github",
    ".idea",
    "idea",
    "image_thumbnails",
    "thumbnails_readme",
)

# WSL path
path_to_thumbnails_folder = Path(path + "/image_thumbnails")
path_to_readme = Path(path + "/README.md")

if __name__ == "__main__":
    thumbnails_readme.prepare_thumbnails_folder(path_to_thumbnails_folder)
    thumbnails_readme.prepare_readme(path_to_readme)
    thumbnails_readme.crawl(
        path,
        path_to_readme,
        poppler_path,
        path_to_thumbnails_folder,
        MAX_SIZE,
        pdf_quality,
        skiplist,
    )