from html.parser import HTMLParser
from pathlib import Path


class LinkAndTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag != "a":
            return
        attributes = dict(attrs)
        href = attributes.get("href")
        if href is not None:
            self.links.append(href)

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.text_parts.append(data.strip())

    @property
    def text(self) -> str:
        return " ".join(self.text_parts)


def parse_html(path: Path) -> LinkAndTextParser:
    parser = LinkAndTextParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def test_provider_metrics_documentation_index_lists_operational_contract() -> None:
    docs_index = Path("reference/provider-metrics-index.html")

    parser = parse_html(docs_index)

    assert "/provider/metrics" in parser.text
    assert "/provider/metrics/prometheus" in parser.text
    assert "provider_prediction_total" in parser.text
    assert "get_provider_prediction_metric_contract" in parser.text
    assert "not a production multi-instance metrics pipeline" in parser.text


def test_provider_metrics_documentation_index_links_learning_and_tests() -> None:
    docs_index = Path("reference/provider-metrics-index.html")

    parser = parse_html(docs_index)

    assert "../lessons/0058-provider-metrics-production-boundary.html" in parser.links
    assert "../lessons/0059-provider-metrics-naming-contract.html" in parser.links
    assert "../lessons/0060-provider-metrics-naming-refactor-boundary.html" in parser.links
    assert "../lessons/0061-provider-metrics-documentation-index.html" in parser.links
    assert "../tests/test_provider_http.py" in parser.links
    assert "../tests/test_openapi_contract.py" in parser.links
