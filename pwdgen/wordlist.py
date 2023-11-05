import hashlib
import os
import tempfile
from pathlib import Path

import requests

WORDLISTS_PATH = Path(tempfile.gettempdir()) / Path("py-pwgen") / Path("wordlists")
DEFAULT_WORDLIST = "https://github.com/brycedrennan/wordlists/raw/master/wordlists/archive-org-till-1830/wordlist_match1.txt"


def get_wordlist_path(url=DEFAULT_WORDLIST):
    """Download and return the path of a wordlist from the given URL."""
    url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
    wordlist_downloaded_path = WORDLISTS_PATH / Path(url_hash + ".txt")
    if not wordlist_downloaded_path.exists():
        print("\nDownloading wordlist from %s\n" % url)
        download_file(url, wordlist_downloaded_path)
    return wordlist_downloaded_path


def download_file(url, dest_path):
    """Download a file from a given URL and save it to a given destination path."""
    os.makedirs(str(dest_path.parent), exist_ok=True)
    with dest_path.open("wb") as f:
        response = requests.get(url, stream=True)
        if not response.ok:
            raise Exception("Download Failed")

        for block in response.iter_content(1024):
            f.write(block)


class LazyString:
    """Provide a lazy-evaluated string representation of a generator."""

    def __init__(self, string_generator):
        """Initialize a StringGenerator object with a string generator."""
        self.string_generator = string_generator

    def __str__(self):
        """Return a string representation of the generated string."""
        return str(self.string_generator())
