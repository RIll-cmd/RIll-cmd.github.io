# Portfolio site

My portfolio, built with a small Python script: Markdown pages in `content/` are rendered through one Jinja2 layout into `public/`, and GitHub Actions deploys `public/` to GitHub Pages on every push to `main`. No backend.

Live: https://rill-cmd.github.io/

## Build locally

```sh
python -m pip install -r requirements.txt
python build.py
python -m http.server -d public 8000
```

Then open http://localhost:8000.

Stack choice and trade-offs are explained in my FlyRank "Three Roads" assignment. AI-assisted (Claude), reviewed by me.
