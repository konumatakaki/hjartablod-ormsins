# hjartablod-ormsins

言語解読をテーマにしたブラウザゲームの制作用リポジトリ。
記録装置越しに、異世界から来た話者の言葉を、現代の言語学の道具で解読していく調査ゲーム。

まだ制作の途中で、遊べる版はない。

## まず読むもの

| 読む人 | 文書 |
|---|---|
| 全体を知りたい | [docs/premises.md](docs/premises.md)（土台の決定。末尾に全文書の地図） |
| 残っている仕事を知りたい | [docs/open-questions.md](docs/open-questions.md) |
| 台本を書く | [content/README.md](content/README.md)（書き方、タグ、ルビ、検査、Inky） |
| 画面を作る | [docs/design-rules.md](docs/design-rules.md) |
| 技術を知りたい | [docs/tech.md](docs/tech.md) |

## 道具

```
npm install
npm run check:content   # 台本の検査（GitHub の上でも自動で走る）
npm run export:inky     # Inky（公式版）で開くための書き出し
```

半角の `|` のルビを使える改造版の Inky は、このリポジトリの Releases にある（[tools/inky/README.md](tools/inky/README.md)）。inkle Ltd による公式の Inky ではない。

## ライセンス

- このリポジトリ自体（コード、文書、文章）のライセンスは未定。
- 第三者の著作物（Inky、inkjs、書体など）とそのライセンスは [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) と `licenses/`。
- `reference/` にあるオーナーの過去作は、このリポジトリのライセンスの対象外。
