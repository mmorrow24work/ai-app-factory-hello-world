"""Tests for every *.html page at the repo root.

Stdlib only (html.parser, pathlib) and no network calls: external http(s)
links are recognised and skipped rather than fetched. Folds in and replaces
the M1 smoke test (see issue #1) — that check is now the "parses without
error" / "exactly one <h1>" cases below, run over every page instead of
just index.html.
"""

import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parent.parent
HTML_FILES = sorted(REPO_ROOT.glob("*.html"))


class PageParser(HTMLParser):
    """Collects the bits of page structure the tests below check."""

    def __init__(self):
        super().__init__()
        self.html_lang = None
        self.has_charset_meta = False
        self.has_viewport_meta = False
        self.title = None
        self.h1_count = 0
        self.links = []  # list of (tag, attr, value)
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.html_lang = attrs.get("lang")
        elif tag == "meta":
            if attrs.get("charset") is not None:
                self.has_charset_meta = True
            if attrs.get("name") == "viewport":
                self.has_viewport_meta = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self._in_title = True
            self.title = ""
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if value is not None:
                self.links.append((tag, attr, value))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title and self.title is not None:
            self.title += data


def parse_html(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


def is_external_http(value):
    return value.startswith("http://") or value.startswith("https://")


def is_in_page_anchor(value):
    return value.startswith("#")


def local_link_targets(page, source_path):
    """Resolved filesystem paths for a page's local (non-external, non-anchor) links."""
    targets = set()
    for _tag, _attr, value in page.links:
        if is_external_http(value) or is_in_page_anchor(value):
            continue
        targets.add((source_path.parent / value.split("#", 1)[0]).resolve())
    return targets


def test_html_files_exist():
    assert HTML_FILES, "expected at least one *.html file at the repo root"


def test_all_pages_parse_without_error():
    for path in HTML_FILES:
        parse_html(path)


def test_all_pages_have_lang_attribute():
    for path in HTML_FILES:
        page = parse_html(path)
        assert page.html_lang, f"{path.name}: <html> is missing a lang attribute"


def test_all_pages_have_charset_meta():
    for path in HTML_FILES:
        page = parse_html(path)
        assert page.has_charset_meta, f"{path.name}: missing <meta charset>"


def test_all_pages_have_viewport_meta():
    for path in HTML_FILES:
        page = parse_html(path)
        assert page.has_viewport_meta, f"{path.name}: missing viewport <meta>"


def test_all_pages_have_nonempty_title():
    for path in HTML_FILES:
        page = parse_html(path)
        assert page.title and page.title.strip(), f"{path.name}: missing or empty <title>"


def test_all_pages_have_exactly_one_h1():
    for path in HTML_FILES:
        page = parse_html(path)
        assert page.h1_count == 1, (
            f"{path.name}: expected exactly one <h1>, found {page.h1_count}"
        )


def test_all_local_links_are_relative_and_resolve():
    for path in HTML_FILES:
        page = parse_html(path)
        for tag, attr, value in page.links:
            if is_external_http(value) or is_in_page_anchor(value):
                continue
            assert not value.startswith("/"), (
                f"{path.name}: {tag} {attr}=\"{value}\" is not relative (leading slash)"
            )
            parsed = urlsplit(value)
            assert not parsed.scheme and not parsed.netloc, (
                f"{path.name}: {tag} {attr}=\"{value}\" has a scheme/host, "
                "expected a relative path"
            )
            target = (path.parent / value.split("#", 1)[0]).resolve()
            assert target.is_file(), (
                f"{path.name}: {tag} {attr}=\"{value}\" does not resolve to a file in the repo"
            )


def test_index_links_to_about_and_back():
    index_html = REPO_ROOT / "index.html"
    about_html = REPO_ROOT / "about.html"
    if not about_html.is_file():
        raise unittest.SkipTest("about.html does not exist yet (added in a later milestone)")

    index_page = parse_html(index_html)
    about_page = parse_html(about_html)

    assert about_html.resolve() in local_link_targets(index_page, index_html), (
        "index.html does not link to about.html"
    )
    assert index_html.resolve() in local_link_targets(about_page, about_html), (
        "about.html does not link back to index.html"
    )
