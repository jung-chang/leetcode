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
from re import I
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


def get_dirs(path: str):
    """
    home/
        asd/
            asd_folder1/
                asd_file1
                asd_file2
            asd_folder2/
                empty
            qwe/
                local/
                    tmp/
                        tmp_file1
                        tmp_file2
                logs/
                    log_asd
                    log_qwe
            asd_readme
    """
    dirs = {
        "/home/asd/": ["asd_folder1/", "asd_folder2/", "asd_readme", "asd_qwe/"],
        "/home/asd/asd_folder1/": ["asd_file1", "asd_file2"],
        "/home/asd/qwe/": ["local/", "logs/"],
        "/home/asd/qwe/local/": ["tmp/"],
        "/home/asd/qwe/local/tmp/": ["tmp_file1", "tmp_file2"],
        "/home/asd/qwe/logs/": ["log_asd", "log_qwe"],
    }
    return dirs.get(path, [])


def is_dir(path: str) -> bool:
    return path.endswith("/")


def all_dirs(directory: str) -> List[str]:
    dir_paths = set()

    def dfs(dir: str):
        sub_paths = get_dirs(dir)

        if not sub_paths:
            dir_paths.add(dir)
            return

        for sub_path in sub_paths:
            dfs(dir + sub_path)

    dfs(directory)
    return dir_paths


# print(all_dirs("/home/asd/"))
# print(all_dirs("/home/asd/qwe/local/"))


def smallest_common_prefix(words: List[str]) -> str:
    sorted_words = sorted(words, key=len)
    shortest_word = sorted_words[0]

    i = 0
    prefix = ""
    while i < len(shortest_word):
        for word in sorted_words[1:]:
            if shortest_word[i] != word[i]:
                return prefix
        prefix += shortest_word[i]
        i += 1
    return prefix


def autocomplete_dir(search: str, dir: str) -> str:
    """
    Cases:
    asd, /home/asd/qwe -> no matching -> asd
    lo, /home/asd/qwe -> local/ and logs/ -> /home/asd/qwe/lo
    log, /home/asd/qwe -> /home/asd/qwe/logs/log_
    """

    sub_paths = get_dirs(dir)
    if not sub_paths:
        return search

    matches = [path for path in sub_paths if path.startswith(search)]
    if not matches:
        return search
    if len(matches) > 1:
        return dir + smallest_common_prefix(matches)
    while len(matches) == 1 and is_dir(matches[0]):
        dir += matches[0]
        matches = [path for path in get_dirs(dir) if path.startswith(search)]
    return dir + smallest_common_prefix(matches)


print(autocomplete_dir("lo", "/home/asd/qwe/"))
print(autocomplete_dir("log", "/home/asd/qwe/"))

print(autocomplete_dir("a", "/home/asd/"))
print(autocomplete_dir("t", "/home/asd/qwe/local/"))
