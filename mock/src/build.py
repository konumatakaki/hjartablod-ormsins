"""見本の HTML を組み立てる。

使い方: python mock/src/build.py <テンプレート> <出力先>
テンプレートの {{FONT_ファイル名}} を woff2 の base64 に、{{ICON_名前}} と {{BIG_名前}} をドット絵の SVG に置き換える。
"""
import base64, pathlib, re, sys

SRC = pathlib.Path(__file__).parent

ICONS = {
    "cam": [
        "............", "............", "............",
        ".#######..#.", ".#.....#.##.", ".#.....####.", ".#.....####.", ".#.....#.##.", ".#######..#.",
        "............", "............", "............",
    ],
    "mic": [
        "....####....", "....#..#....", "....#..#....", "....#..#....", "..#.#..#.#..", "..#.####.#..",
        "..#......#..", "...#....#...", "....####....", ".....##.....", "....####....", "............",
    ],
    "gpu": [
        "............", "....#.#.#...", "...#######..", "..##.....##.", "...#.###.#..", "..##.#.#.##.",
        "...#.###.#..", "..##.....##.", "...#######..", "....#.#.#...", "............", "............",
    ],
    "usb": [
        ".....#......", "....###.....", ".....#......", ".#...#..##..", "###..#..##..", ".#...#...#..",
        "..#..#..#...", "...#.#.#....", "....###.....", ".....#......", "....###.....", "....###.....",
    ],
    "netoff": [
        "#...........", ".#..........", "..#######...", "..##.....#..", "..#.##.#.#..", "..#...#..#..",
        "..##...#.#..", "...#...##...", "...#####.#..", "..........#.", "...........#", "............",
    ],
    "ear": [
        "....####....", "...#....#...", "..#......#..", "..#..##..#..", "..#.#..#.#..", "....#..#.#..",
        ".....##.#...", "........#...", ".......#....", "...#..#.....", "....##......", "............",
    ],
}

def svg(name, cls, size):
    rects = []
    for y, row in enumerate(ICONS[name]):
        assert len(row) == 12, (name, y)
        for x, ch in enumerate(row):
            if ch == "#":
                rects.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')
    return (f'<svg class="{cls}" viewBox="0 0 12 12" width="{size}" height="{size}" '
            f'shape-rendering="crispEdges" aria-hidden="true">{"".join(rects)}</svg>')

def main(template, out):
    html = pathlib.Path(template).read_text(encoding="utf-8")
    def font(m):
        return base64.b64encode((SRC / "fonts" / (m.group(1) + ".woff2")).read_bytes()).decode()
    html = re.sub(r"\{\{FONT_([A-Za-z0-9_-]+)\}\}", font, html)
    html = re.sub(r"\{\{ICON_([a-z]+)\}\}", lambda m: svg(m.group(1), "ico", 12), html)
    html = re.sub(r"\{\{BIG_([a-z]+)\}\}", lambda m: svg(m.group(1), "ico big", 48), html)
    assert "{{" not in html, html[html.index("{{"):html.index("{{") + 40]
    pathlib.Path(out).write_text(html, encoding="utf-8")
    print(out, len(html))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
