from bs4 import BeautifulSoup
from requests import exceptions
from requests import Session
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError
from dvk_archive.processing.string_processing import get_extension


def basic_connect(url: str = None) -> BeautifulSoup:
    """
    Connects to a URL and returns a BeautifulSoup object.
    Incapable of working with JavaScript.

    Parameters:
        url (str): URL to retrieve

    Returns:
        BeautifulSoup: BeautifulSoup object of the url page
    """
    if url is None or url == "":
        return None
    session = Session()
    headers = {
        "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept-Language":
        "en-US,en;q=0.5"}
    try:
        request = session.get(url, headers=headers)
        bs = BeautifulSoup(request.text, features="lxml")
        return bs
    except (exceptions.ConnectionError, exceptions.MissingSchema):
        return None
    return None


def download(url: str = None, filename: str = None):
    """
    Downloads a file from a given url to a given file path.

    Parameters:
        url (str): URL from which to download
        filename (str): File path to save to
    """
    if (url is not None
            and not url == ""
            and filename is not None
            and not filename == ""):
        file = Path(filename)
        if file.exists():
            extension = get_extension(filename)
            base = filename[0:len(filename) - len(extension)]
            num = 1
            while file.exists():
                file = Path(base + "(" + str(num) + ")" + extension)
                num = num + 1
        try:
            urlretrieve(url, file.absolute())
        except (URLError, ValueError):
            print("Failed to download:" + url)
