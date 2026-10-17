# 第三者の著作物について

このリポジトリに含まれる、または組み立てに使う第三者の著作物と、そのライセンス。ライセンスの全文は `licenses/` にある。

このリポジトリ自体（ゲームのコード、文書、文章）のライセンスは未定。

## ソフトウェア

| 名前 | 作者 | 使い方 | ライセンス | 出どころ |
|---|---|---|---|---|
| Inky | inkle Ltd | 改造版を組み立てる元（`tools/inky/`）。改造したファイル1つと差分を含む | MIT（`licenses/Inky-MIT.txt`） | https://github.com/inkle/inky（コミット 3d46aa92bf1572797f35d338bf75e37bb047f2e3） |
| inklecate / ink | inkle Ltd | 改造版 Inky に同梱（元のまま） | MIT（Inky と同じ） | https://github.com/inkle/ink |
| inkjs | inkle Ltd、inkjs contributors | 台本の検査とゲームで使う（npm から取得） | MIT（`licenses/inkjs-MIT.txt`） | https://github.com/y-lohse/inkjs |

改造版 Inky は inkle Ltd による公式のものではない。詳しくは `tools/inky/README.md`。

## 書体（見本 `mock/` に埋め込み）

| 名前 | 作者 | 使い方 | ライセンス |
|---|---|---|---|
| DejaVu Sans、DejaVu Sans Mono | DejaVu fonts team（Bitstream Vera を元にする） | 使う文字だけに絞った版を埋め込み | Bitstream Vera の許諾と、DejaVu の変更部分のパブリックドメイン（`licenses/DejaVuFonts.txt`）。改変版は「Bitstream」「Vera」の名を使わないこと |
| Liberation Mono | Red Hat, Inc.（Google の Cousine を元にする） | 元のファイルのまま埋め込み | SIL Open Font License 1.1、予約書体名「Liberation」（`licenses/LiberationFonts-OFL-1.1.txt`）。改変版を配るなら名前を変える必要があるため、改変しない |
| Source Sans Pro | Adobe | 元のファイルのまま埋め込み（Gradio が同梱しているもの） | SIL Open Font License 1.1、予約書体名「Source」（`licenses/SourceSansPro-OFL-1.1.txt`） |

見本の HTML は、Google Fonts から Noto Sans JP、Noto Serif JP、BIZ UDPGothic、BIZ UDGothic、DotGothic16 を読み込んでいる（いずれも SIL Open Font License 1.1）。本番では同梱する方針（`docs/design-rules.md`）。

## 画像

- オーナーの見本画像（`mock/local/`）は、公開するかが未定のため、このリポジトリには含めていない。
