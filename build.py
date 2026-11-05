"""Build the portfolio: content/*.md -> public/*.html using one Jinja2 layout."""
import shutil
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
OUT = ROOT / "public"
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)


def build():
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(ROOT / "static", OUT)
    for src in sorted((ROOT / "content").rglob("*.md")):
        md = markdown.Markdown(extensions=["meta", "tables", "fenced_code"])
        body = md.convert(src.read_text(encoding="utf8"))
        rel = src.relative_to(ROOT / "content").with_suffix(".html")
        # relative links only, so the site works under any base path
        root = "../" * (len(rel.parts) - 1)
        title = md.Meta.get("title", ["Cyrill Gerard Cajucom"])[0]
        html = env.get_template("base.html").render(title=title, body=body, root=root)
        (OUT / rel).parent.mkdir(parents=True, exist_ok=True)
        (OUT / rel).write_text(html, encoding="utf8")
        print("built", rel)


if __name__ == "__main__":
    build()
    assert (OUT / "index.html").exists(), "home page missing"
