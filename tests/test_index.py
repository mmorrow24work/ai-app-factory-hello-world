"""Minimal smoke test for index.html (see issue #1 / M2 for the full suite)."""

from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = REPO_ROOT / "index.html"


class _SmokeParser(HTMLParser):
    """Parses without raising and counts <h1> tags."""

    def __init__(self):
        super().__init__()
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self.h1_count += 1


def test_index_html_exists():
    assert INDEX_HTML.is_file()


def test_index_html_parses_and_has_one_h1():
    html = INDEX_HTML.read_text(encoding="utf-8")
    parser = _SmokeParser()
    parser.feed(html)
    parser.close()
    assert parser.h1_count == 1
