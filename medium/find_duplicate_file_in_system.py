# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
from typing import List, Tuple


class Solution:
    """
    Given a list paths of directory info, including the directory path, and all the files with contents in this directory,
    return all the duplicate files in the file system in terms of their paths.

    You may return the answer in any order.

    A group of duplicate files consists of at least two files that have the same content.

    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
    """

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)

        def get_file(file_data: str) -> Tuple[str, str]:
            data = file_data.split("(")
            return data[0], data[1][: len(data[1]) - 1]

        for path in paths:
            data = path.split(" ")
            folder = data[0]
            for file_data in data[1:]:
                filename, content = get_file(file_data)
                content_to_path[content].append(f"{folder}/{filename}")

        print(content_to_path)
        return [values for values in content_to_path.values() if len(values) > 1]


p = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)",
]
print(Solution().findDuplicate(p))
