# 改造版 Inky（半角の | のルビ対応）について

このフォルダは、ink の公式エディタ **Inky** に、半角の `|` のルビ（`|漢字《よみ》`）を使えるようにする改造を加えるためのもの。

**これは inkle Ltd による公式の Inky ではない。** inkle Ltd はこの改造版に関与しておらず、推奨もしていない。不具合は inkle ではなく、このリポジトリの側の問題として扱う。

## 元になったもの

| 項目 | 内容 |
|---|---|
| ソフトウェア | Inky（ink の公式エディタ） |
| 作者 | inkle Ltd |
| 元のソース | https://github.com/inkle/inky |
| 元にした版 | コミット `3d46aa92bf1572797f35d338bf75e37bb047f2e3`（2026-05-05）。https://github.com/inkle/inky/tree/3d46aa92bf1572797f35d338bf75e37bb047f2e3 |
| ライセンス | MIT License, Copyright (c) 2016 inkle Ltd.（全文は `licenses/Inky-MIT.txt`。元のソースでは README.md の「License」の節に記載） |

同梱されるコンパイラ inklecate（ink）も inkle Ltd の MIT ライセンスのソフトウェアで、Inky の元のソースに含まれているものをそのまま使っている。
組み立てに使う Electron（MIT）と Chromium などの部品のライセンスは、Electron の組み立ての道具が成果物の中に `LICENSE` と `LICENSES.chromium.html` として入れる。

## 加えた変更

- 変更したファイルは `app/main-process/inklecate.js` の1つだけ。
- 変更の中身: inklecate にファイルを渡す直前に、波括弧 `{ }` の外にある `|漢字《よみ》` を全角の `｜漢字《よみ》` に置き換える関数を足した。
- 差分: `inky-ruby.patch`。変更後のファイル全体: `inklecate.js`（冒頭に出どころとライセンスを記載）。

## 組み立て

- `.github/workflows/build-inky.yml` が、GitHub Actions の Windows 環境で、元のソースに差分を当て、Inky の元のソースにある組み立ての手順（`npm run build-package -- win64`）で組み立てる。
- 成果物の zip には、このファイル（`README-hjartablod.md`）と、Inky のライセンス（`LICENSE-Inky.txt`）を入れている。
