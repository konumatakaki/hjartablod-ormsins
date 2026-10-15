"""見本の HTML に、オーナーの画像（mock/local）を埋め込んだ版を作る。公開リポジトリには入れない。

使い方: python mock/src/with_images.py mock/interview.html mock/local mock/local/interview-images.html
"""
import base64, pathlib, sys

def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def main(src, imgdir, out):
    html = pathlib.Path(src).read_text(encoding="utf-8")
    d = pathlib.Path(imgdir)
    frame = '<div class="frame"><span>正面カメラの映像（立ち絵。顔の周りをトリミング）</span></div>'
    assert frame in html
    html = html.replace(frame, f'<img class="feed" alt="" src="{data_uri(d / "camera.jpg", "image/jpeg")}">')
    # 特徴点（目、鼻、口）と骨格（肩、肘）。位置は camera.jpg に合わせて手で測ったもの。色は仮
    start = html.index('<svg class="lm"'); end = html.index("</svg>", start) + len("</svg>")
    lm = """<svg class="lm" viewBox="0 0 704 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <g stroke="#e8e8e8" stroke-width="1.5" fill="none" opacity=".85">
    <line x1="262" y1="425" x2="455" y2="425"/><line x1="262" y1="425" x2="234" y2="600"/><line x1="455" y1="425" x2="480" y2="600"/>
    <circle cx="321" cy="297" r="7"/><circle cx="397" cy="297" r="7"/>
  </g>
  <g fill="#ff3b30">
    <circle cx="321" cy="297" r="2"/><circle cx="397" cy="297" r="2"/><circle cx="359" cy="330" r="2"/>
    <circle cx="350" cy="352" r="2"/><circle cx="368" cy="352" r="2"/>
    <circle cx="262" cy="425" r="3"/><circle cx="455" cy="425" r="3"/><circle cx="234" cy="600" r="3"/><circle cx="480" cy="600" r="3"/>
  </g>
</svg>"""
    html = html[:start] + lm + html[end:]
    badges = [data_uri(d / "badge_engineer.png", "image/png"), data_uri(d / "badge_leader.png", "image/png")]
    for uri in badges:
        assert '<div class="badge">写真</div>' in html
        html = html.replace('<div class="badge">写真</div>', f'<img class="badge" alt="" src="{uri}">', 1)
    html = html.replace("</style>", ".cam .feed { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }\n.comm img.badge { object-fit: cover; image-rendering: auto; }\n</style>", 1)
    html = html.replace("<title>hjartablod-ormsins 面接画面</title>", "<title>hjartablod-ormsins 面接画面（画像入り）</title>", 1)
    pathlib.Path(out).write_text(html, encoding="utf-8")
    print(out, len(html))

if __name__ == "__main__":
    main(*sys.argv[1:4])
