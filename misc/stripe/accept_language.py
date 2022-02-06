# This is a potential stripe coding question

# Stage 1: Create a function that requests languages in string format and return an array of the supported languages
# Stage 2: Support non-region specific requests. ie "en" returns ["en-US", "en-CA", "en-GB"]
# Stage 3: Support wildcard matching to return the rest of the supported languages

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language

# Examples
# Accept-Language: de
# Accept-Language: de-CH
# Accept-Language: en-US,en;q=0.5

from typing import Set
import pdb


ACCEPT_LANGUAGE = "Accept-Language: "

SUPPORTED_LANGUAGES = set([])


class Parser:
    def __init__(self, header: str) -> None:
        self.header = header
        self.languages = self._parse(header)

    def is_valid(self, header: str) -> bool:
        if not header.startswith(ACCEPT_LANGUAGE):
            return False
        prefix, data = header.split(ACCEPT_LANGUAGE)
        if prefix or not data:
            return False
        return True

    def get_languages(self) -> Set[str]:
        return self.languages

    def _parse(self, header: str) -> Set[str]:
        pdb.set_trace()
        if not self.is_valid(header):
            return set()
        _, data = header.split(ACCEPT_LANGUAGE)
        languages = set()
        for directive in data.split(","):
            languages.add(directive.strip())
        return languages


import unittest


class TestParser(unittest.TestCase):
    def test_invalid_header_wrong_prefix(self):
        header = "Wrong-Prefix: de"
        parser = Parser(header)
        self.assertFalse(parser.is_valid(header))
        self.assertFalse(parser.get_languages())

    def test_invalid_header_no_data(self):
        header = "Accept-Language:"
        parser = Parser(header)
        self.assertFalse(parser.is_valid(header))
        self.assertFalse(parser.get_languages())

    def test_without_country_code(self):
        header = "Accept-Language: de"
        parser = Parser(header)
        self.assertTrue(parser.is_valid(header))
        self.assertEquals(parser.get_languages(), set(["de"]))

    def test_with_country_code(self):
        header = "Accept-Language: de-DE"
        parser = Parser(header)
        self.assertTrue(parser.is_valid(header))
        self.assertEquals(parser.get_languages(), set(["de-DE"]))

    def test_with_weight(self):
        header = "Accept-Language: en-US,en;q=0.5"
        parser = Parser(header)
        self.assertTrue(parser.is_valid(header))
        self.assertEquals(parser.get_languages(), set(["de-DE"]))

    def test_multiple_with_country_codes(self):
        header = "Accept-Language: en-US, ja-JP, es-MX"
        parser = Parser(header)
        self.assertTrue(parser.is_valid(header))
        self.assertEquals(parser.get_languages(), set(["en-US", "ja-JP", "es-MX"]))

    def test_multiple_with_and_without_country_codes(self):
        header = "Accept-Language: en, ja-JP, es-MX, de"
        parser = Parser(header)
        self.assertTrue(parser.is_valid(header))
        self.assertEquals(parser.get_languages(), set(["en", "ja-JP", "es-MX", "de"]))


if __name__ == "__main__":
    unittest.main()
