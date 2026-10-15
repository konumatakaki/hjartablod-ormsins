"""オーナーの見本画像から、カメラの映像風の画像と入館証の写真を作る。

使い方: python mock/src/camera_filter.py <入力のフォルダ> <出力のフォルダ>
入力: 1.png（少女）、2.png（リーダー）、3.png（エンジニア）。背景はほぼ白。
出力: camera.jpg（1408x1400、カメラの窓の素材）、badge_leader.png、badge_engineer.png（各 68x84）。
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def cut_out(im, tol=14):
    """四隅から背景を塗りつぶして、人物だけのアルファを作る。"""
    rgb = im.convert("RGB")
    marker = (255, 0, 255)
    work = rgb.copy()
    for xy in [(0, 0), (work.width - 1, 0), (0, work.height - 1), (work.width - 1, work.height - 1)]:
        ImageDraw.floodfill(work, xy, marker, thresh=tol)
    a = np.array(work)
    mask = ~((a[..., 0] == 255) & (a[..., 1] == 0) & (a[..., 2] == 255))
    # 髪と腕の間など、四隅から届かない背景も抜く（ほぼ白で、色味のない画素）
    o = np.array(rgb).astype(int)
    near_white = (o.min(axis=2) >= 240) & (o.max(axis=2) - o.min(axis=2) <= 8)
    mask &= ~near_white
    out = rgb.convert("RGBA")
    out.putalpha(Image.fromarray((mask * 255).astype(np.uint8)))
    return out

def room(w, h):
    """病院の個室の壁。上は明るく、腰の高さに手すり、左に扉の枠。"""
    y = np.linspace(0, 1, h)[:, None, None]
    wall = np.array([206, 211, 203]) * (1.02 - 0.10 * y) * np.ones((h, w, 1))
    img = wall.copy()
    rail = int(h * 0.80)
    img[rail:rail + 18] = [150, 154, 148]
    img[rail + 18:] *= 0.93
    img[:, 120:134] = [168, 172, 165]
    img[:, 134:150] *= 0.9
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))

def camera(img, seed=0):
    """カメラの映像らしさ: 少しぼかす、蛍光灯の色、粒子、色ずれ、周辺減光、アクリル板の映り込み、圧縮。"""
    rng = np.random.default_rng(seed)
    img = img.filter(ImageFilter.GaussianBlur(1.1))
    a = np.asarray(img).astype(np.float32)
    a = a * np.array([0.97, 1.0, 0.99]) + np.array([4, 7, 6])            # 蛍光灯で少し緑がかる
    a = 12 + a * (235 / 255)                                              # 黒が浮き、白が飛ばない
    h, w = a.shape[:2]
    a += rng.normal(0, 5.5, (h, w, 1))                                    # 明るさの粒子
    a += rng.normal(0, 2.0, (h, w, 3))                                    # 色の粒子
    a[..., 0] = np.roll(a[..., 0], 1, axis=1)                             # 色ずれ（赤と青を1画素ずらす）
    a[..., 2] = np.roll(a[..., 2], -1, axis=1)
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    a *= (1 - 0.16 * np.clip(r - 0.35, 0, None) ** 1.6)[..., None]        # 周辺減光
    band = np.exp(-(((xx + yy * 0.55) - w * 0.95) / (w * 0.10)) ** 2)     # アクリル板に映る斜めの光
    a += (band * 10)[..., None]
    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    return out

def main(src, dst):
    src, dst = pathlib.Path(src), pathlib.Path(dst)
    dst.mkdir(parents=True, exist_ok=True)

    # 少女: 目の中点（元画像で 71.5, 57）を、素材の (704, 600) に置く。倍率 5.5
    girl = cut_out(Image.open(src / "1.png"))
    s = 5.5
    girl = girl.resize((round(girl.width * s), round(girl.height * s)), Image.LANCZOS)
    canvas = room(1408, 1400).convert("RGBA")
    canvas.alpha_composite(girl, (round(704 - 71.5 * s), round(600 - 57 * s)))
    cam = camera(canvas.convert("RGB"))
    cam.save(dst / "camera.jpg", quality=72)

    # 入館証の写真: 顔の周りを切り抜き、証明写真の背景（薄い青灰色）に置く
    for name, box in [("leader", (10, 0, 72, 78)), ("engineer", (16, 0, 70, 66))]:
        person = cut_out(Image.open(src / ("2.png" if name == "leader" else "3.png")))
        crop = person.crop(box)
        bg = Image.new("RGBA", crop.size, (196, 208, 220, 255))
        bg.alpha_composite(crop)
        bg.convert("RGB").resize((68, 84), Image.LANCZOS).save(dst / f"badge_{name}.png")
    print("ok", dst)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
