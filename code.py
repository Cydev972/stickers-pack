import os
import sys
from glob import glob


template = """        {{
          "image_file": "{name}",
          "emojis": ["",""]
        }},"""


if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    for name in glob('*.webp'):
        print(template.format(name=name))
