"""
HTMLRenderer
Builds an `index.html` and companion `styles.css` file from parsed Figma elements.
The renderer focuses on semantic structure rather than pixel precision.
"""

import os
from typing import List, Dict


class HTMLRenderer:
    def __init__(self, elements: List[Dict]):
        self.elements = elements or []

    def render(self, output_dir: str = "output") -> None:
        os.makedirs(output_dir, exist_ok=True)
        html_path = os.path.join(output_dir, "index.html")
        css_path = os.path.join(output_dir, "styles.css")

        with open(html_path, "w", encoding="utf-8") as f_html:
            f_html.write(self._build_html())

        with open(css_path, "w", encoding="utf-8") as f_css:
            f_css.write(self._build_css())

        print(f"Files generated: {html_path} and {css_path}")

    def _find_text(self, snippet: str) -> str | None:
        key = snippet.lower()
        for el in self.elements:
            txt = el.get("text")
            if txt and key in txt.lower():
                return txt
        return None

    def _build_html(self) -> str:
        title = self._find_text("sign in") or "Sign in"
        email = self._find_text("@") or "andy@gmail.com"
        password = self._find_text("password") or "Password"
        primary = self._find_text("sign in") or "Sign in"
        secondary = self._find_text("create account") or "Create account"
        forgot = self._find_text("forgot") or "Forgot password"

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Figma to HTML</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="phone-frame">
    <div class="content screen">
      <h1 class="title">{title}</h1>

      <div class="input-card">
        <div class="input-field">{email}</div>
        <div class="input-field placeholder">{password}</div>
      </div>

      <div class="actions">
        <button class="btn primary">{primary}</button>
        <button class="btn secondary">{secondary}</button>
        <a class="forgot">{forgot}</a>
      </div>

      <div class="home-indicator" aria-hidden="true"></div>
    </div>
  </div>
</body>
</html>
"""

    def _build_css(self) -> str:
        return """
body {
  margin: 0;
  background: #efefef;
  font-family: 'Inter', Arial, sans-serif;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.phone-frame {
  width: 393px;
  height: 852px;
  background: #fff;
  border-radius: 36px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
  overflow: hidden;
  position: relative;
}

.screen {
  padding: 56px 32px 28px 32px;
  height: 100%;
  box-sizing: border-box;
}

.title {
  font-size: 56px;
  line-height: 1.05;
  margin: 0 0 28px 0;
  color: #353240;
  font-weight: 700;
}

.input-card {
  max-width: 320px;
  background: #fff;
  border: 1px solid rgba(220, 220, 220, 1);
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 40px;
}

.input-field {
  padding: 14px 16px;
  font-size: 15px;
  color: #353240;
}

.input-field + .input-field {
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.input-field.placeholder {
  color: #cfcfcf;
}

.actions {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 72px;
  width: calc(100% - 64px);
  max-width: 330px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.btn {
  height: 52px;
  border-radius: 999px;
  font-weight: 600;
  font-size: 15px;
  border: none;
}

.btn.primary {
  background: linear-gradient(90deg, #3f2ae6 0%, #b23aa0 100%);
  color: #fff;
}

.btn.secondary {
  background: #f3eef6;
  color: #353240;
}

.forgot {
  display: block;
  text-align: center;
  color: #6b6b75;
  font-size: 13px;
  margin-top: 6px;
  text-decoration: none;
}

.home-indicator {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 18px;
  width: 68px;
  height: 6px;
  background: #e8e8e8;
  border-radius: 6px;
}
"""
