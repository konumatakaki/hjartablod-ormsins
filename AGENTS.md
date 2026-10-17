# AGENTS.md

このリポジトリで作業する AI エージェント向けの案内。人間向けの入口は README.md。

## このリポジトリ

- 言語解読をテーマにしたブラウザゲームの制作用リポジトリ。まだ制作の途中。
- 土台の決定は `docs/premises.md`。末尾に全文書の地図がある。**作業の前に必ず読む。**
- 文書はすべて日本語。オーナーとのやり取りも日本語。

## 正本

同じ内容を複数の場所に書かない。次の文書を正本とし、ほかの文書からは参照する。

| 内容 | 正本 |
|---|---|
| 土台の決定、文書の地図 | `docs/premises.md` |
| 未決事項、残っている仕事 | `docs/open-questions.md` |
| 台本の書き方、使えるタグ、ルビ | `content/README.md` |
| 書体、アイコン、画面の見た目 | `docs/design-rules.md` |
| 人物の細部 | `docs/characters.md` |
| 第三者の著作物とライセンス | `THIRD_PARTY_NOTICES.md`、`licenses/` |

決定が変わったら、正本だけでなく、古い記述が残っているほかの文書も直す。大きな変更の後は、`.claude/agents/repo-critic.md` の手順（古い記述、矛盾、重複、壊れた参照、公開の問題、ライセンスの漏れを探す）で点検する。

## 守ること

- **台詞と本文は書かない。** 本文と台詞はオーナーが書く。骨組みを作るときも、文章の部分は「（内省）」「（台詞）」のような空欄にする。頼まれた直し（誤字、表記、癖の指摘）は `docs/style.md` の4段階に従う。
- **主人公の性別は明かさない。** 性別の分かる描写や代名詞を入れない。
- **このリポジトリは公開されている。** オーナーの画像と音声は Git に入れない（`mock/local/`、`content/images/`、`content/audio/` は Git の管理から外してある）。鍵や個人情報も入れない。
- **第三者のものを足したら**、`THIRD_PARTY_NOTICES.md` と `licenses/` に載せる。予約書体名のある OFL の書体は改変しない。
- **画面の文字には出どころを持たせる**（`docs/design-rules.md`）。ソフトの初期値やログの文言は、記憶で書かずに実物で確かめる。
- 確かな知識と推測を分けて書く。推測には確度を添える。

## 道具

```
npm install
npm run check:content   # 台本の検査。台本や tools/ を変えたら必ず通す
npm run export:inky     # 公式版 Inky で開くための書き出し（build/inky/）
python mock/src/build.py <テンプレート> <出力先>   # 画面の見本の組み立て（mock/src/）
```

- ルビ `|漢字《よみ》` は、ink に渡す前に `tools/ink-preprocess.mjs` で全角に置き換える。同じ処理が改造版 Inky（`tools/inky/`）にもある。片方を直したらもう片方も直す（検査が一致を確かめる）。
- GitHub Actions: `check-content`（台本の検査）、`build-inky`（改造版 Inky を組み立てて Releases に置く）。

## ブランチ

- 今は `claude/eloquent-fermi-y614zu` が既定で、唯一のブランチ。まだ `main` は作らない（オーナーの判断）。
