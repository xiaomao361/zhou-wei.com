from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.errors = []
        self.h1 = 0

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a:
            if a['id'] in self.ids:
                self.errors.append('Duplicate ID: ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'img':
            if 'alt' not in a:
                self.errors.append('Image is missing alt text')
            if not a.get('width') or not a.get('height'):
                self.errors.append('Image is missing intrinsic dimensions')
        for key in ('src', 'href'):
            if key in a:
                self.links.append(a[key])

for file in ['index.html', '404.html']:
    page = Page()
    text = ROOT.joinpath(file).read_text()
    page.feed(text)
    assert page.h1 == 1, file + ': expected one main heading'
    assert '<html lang="zh-CN">' in text
    for link in page.links:
        url = urlsplit(link)
        if url.scheme:
            assert url.scheme == 'https', file + ': unsupported external URL ' + link
            continue
        if url.path and not url.path.startswith('/'):
            assert ROOT.joinpath(unquote(url.path)).exists(), 'Missing local asset: ' + link
        if not url.path and url.fragment:
            assert url.fragment in page.ids, 'Broken section link: ' + link
    assert not page.errors, page.errors
    assert 'zhou-wei.com' not in text or file == '404.html', 'Do not link the inactive custom domain'

for file in ROOT.joinpath('assets').glob('*.svg'):
    ET.parse(file)
    assert '<script' not in file.read_text()

css = ROOT.joinpath('styles.css').read_text()
assert 'prefers-reduced-motion' in css and ':focus-visible' in css
assert not any(ROOT.rglob('CNAME')), 'Keep working Pages URL until DNS is ready'
print('Passed: local assets, section links, heading structure, image dimensions, SVG XML, HTTPS links, focus and reduced-motion rules.')
