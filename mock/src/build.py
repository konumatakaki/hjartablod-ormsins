import base64, pathlib, sys

scratch = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
tpl = (pathlib.Path(__file__).parent / "template.html").read_text(encoding="utf-8")

def b64(name):
    return base64.b64encode((scratch / "fonts" / name).read_bytes()).decode()

ICONS = {
    "cam": [
        "............",
        "............",
        "............",
        ".#######..#.",
        ".#.....#.##.",
        ".#.....####.",
        ".#.....####.",
        ".#.....#.##.",
        ".#######..#.",
        "............",
        "............",
        "............",
    ],
    "mic": [
        "....####....",
        "....#..#....",
        "....#..#....",
        "....#..#....",
        "..#.#..#.#..",
        "..#.####.#..",
        "..#......#..",
        "...#....#...",
        "....####....",
        ".....##.....",
        "....####....",
        "............",
    ],
    "gpu": [
        "............",
        "....#.#.#...",
        "...#######..",
        "..##.....##.",
        "...#.###.#..",
        "..##.#.#.##.",
        "...#.###.#..",
        "..##.....##.",
        "...#######..",
        "....#.#.#...",
        "............",
        "............",
    ],
    "usb": [
        ".....#......",
        "....###.....",
        ".....#......",
        ".#...#..##..",
        "###..#..##..",
        ".#...#...#..",
        "..#..#..#...",
        "...#.#.#....",
        "....###.....",
        ".....#......",
        "....###.....",
        "....###.....",
    ],
    "netoff": [
        "#...........",
        ".#..........",
        "..#######...",
        "..##.....#..",
        "..#.##.#.#..",
        "..#...#..#..",
        "..##...#.#..",
        "...#...##...",
        "...#####.#..",
        "..........#.",
        "...........#",
        "............",
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

html = (tpl.replace("{{DEJAVU_MONO}}", b64("DejaVuSansMono.woff2"))
           .replace("{{DEJAVU_SANS}}", b64("DejaVuSans.woff2"))
           .replace("{{LIB_MONO}}", b64("LiberationMono-Regular.woff2"))
           .replace("{{SSP_REG}}", b64("SourceSansPro-Regular.woff2"))
           .replace("{{SSP_BOLD}}", b64("SourceSansPro-Bold.woff2")))
for n in ICONS:
    html = html.replace("{{ICON_" + n + "}}", svg(n, "ico", 12))
    html = html.replace("{{BIG_" + n + "}}", svg(n, "ico big", 48))
assert "{{" not in html
out.write_text(html, encoding="utf-8")
print(out, len(html))
