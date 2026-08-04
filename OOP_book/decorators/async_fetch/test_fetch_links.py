import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fetch_links
from bs4 import BeautifulSoup


class FetchLinksTests(unittest.TestCase):
    def test_extract_links_from_example_domain(self):
        html = """
        <html><body>
          <a href="https://example.org">Example</a>
          <a href="/about">About</a>
          <a href="#section">Section</a>
          <a href="mailto:test@example.com">Mail</a>
        </body></html>
        """

        soup = BeautifulSoup(html, "html.parser")
        links = fetch_links.extract_links(soup, "https://example.com")

        self.assertEqual(links, ["https://example.org", "https://example.com/about"])


if __name__ == "__main__":
    unittest.main()
