# https://www.1point3acres.com/bbs/thread-795507-1-1.html

# Imagine that we are writing a backup application used to backup files from your laptop
# to a remote server. To save on network bandwidth we want to identify duplicate files
# (i.e. files with the same contents). This way we only need to upload duplicate files once

# Write a function that identifies sets of files with identical contents:

# find_dupes(root_path) → sets/lists of 2 or more filepaths that have identical contents
# find_dupes("/home/airtable") → ["bashrc","Backups/2017_bashrc"], ["Photos/Vacation/DSC1234JPG","profilejpeg","trash/lej2dp28/87msnlgyr"]]

# For scale imagine running this on a computer with at most 2TB of data and at most 1 million files.
# For traversing the filesystem use these library functions:
# list_folder(path) → list of names of immediate file and folder children
# is_folder(path) → boolean

from collections import defaultdict
from typing import List

def list_folder(input_path: str) -> List[str]:
    return []

def is_folder(input_path: str) -> bool:
    return False

def hash_contents(input_path: str) -> str:
    return ""

def find_dupes(input_path: str) -> List[List[str]]:
    content_to_path = defaultdict(list)

    def get_contents(input_path: str):
        for path in list_folder(input_path):
            if is_folder(path):
                get_contents(path)
            else:
                content_to_path[hash_contents(path)].append[path]

    get_contents(input_path)
    return [paths for paths in content_to_path.values()]