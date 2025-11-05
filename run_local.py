# -*- coding: utf-8 -*-
import os
from pathlib import Path
from flask import Flask, send_from_directory

NAME       = "Maryam Amanzade & Zohre Kiayee"          
PORT       = 5000                         
TARGET_DIR = Path.home() / "Desktop" / "my_page" 
FILENAME   = "index.html"

HTML = f"""<!doctype html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8"><title>{NAME}</title>
  <style>
    html,body {{height:100%;margin:0}}
    body {{
      display:flex;align-items:center;justify-content:center;background:#fff;
      font-family:Tahoma, Arial, sans-serif
    }}
    h1 {{ color:#d00; font-size:64px; margin:0; }}
  </style>
</head>
<body><h1>{NAME}</h1></body>
</html>"""

TARGET_DIR.mkdir(parents=True, exist_ok=True)
(file_path := TARGET_DIR / FILENAME).write_text(HTML, encoding="utf-8")
print("Saved file at:", file_path)

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(str(TARGET_DIR), FILENAME)


if __name__ == "__main__":
    print(f"Open: http://127.0.0.1:{PORT}/  (or http://localhost:{PORT}/)")
    app.run(host="0.0.0.0", port=PORT, debug=True)   
print("DEPLOY TEST - v1")
