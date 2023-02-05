import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen, urlretrieve
import time

class MyGithubRepoPageParser(HTMLParser):
    _tag = "a"
    _class = "js-navigation-open Link--primary"
    found = []

    def handle_starttag(self, tag: str, attrs: list[tuple]):
        if tag == self._tag:
            _attribute_dict = dict(attrs)
            if _attribute_dict.get("class") == self._class:
                self.found.append(_attribute_dict["href"])


def _build_dowload_url(github_fld: str):
    match = re.search(r"/(\w+)/(\w+)/blob/(.*)", github_fld)
    user, repo_name, subdir = match.groups()
    download_url = f"https://raw.githubusercontent.com/{user}/{repo_name}/{subdir}"
    return download_url


def download_all_repo_fld(
    src_github_fld: str, dst_local_fld: Path, extensions: tuple[str]
) -> None:
    print(f"requesting github page: {src_github_fld}")
    with urlopen(src_github_fld) as response:
        body = response.read().decode()

    parser = MyGithubRepoPageParser()
    parser.feed(body)
    download_urls = [
        _build_dowload_url(i) for i in parser.found if i.endswith(extensions)
    ]
    show_fpaths ='\n'.join(download_urls)
    print(f"downloading the following files: {show_fpaths}")

    dst_local_fld.mkdir(exist_ok=True)
    for url in download_urls:
        fname = Path(url).name
        fpath = dst_local_fld / fname
        print(f"saving file: {fpath}")
        urlretrieve(url, fpath)


if __name__ == "__main__":
    SOURCE_GITHUB_REPO_FOLDER = (
        "https://github.com/gabrielecalvo/Language4Water/tree/main/2022-23_semester2"
    )
    DESTINATION_FOLDER = Path(__file__).parent / "original"

    download_all_repo_fld(
        src_github_fld=SOURCE_GITHUB_REPO_FOLDER,
        dst_local_fld=DESTINATION_FOLDER,
        extensions=(".ipynb",),
    )

    print("All good :) closing in 5 seconds..")
    time.sleep(5)
