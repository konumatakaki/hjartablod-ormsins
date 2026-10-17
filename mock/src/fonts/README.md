# 見本に埋め込む書体

| ファイル | 元 | 作り方 |
|---|---|---|
| DejaVuSansMono.woff2、DejaVuSans.woff2 | Ubuntu の fonts-dejavu-core | 使う文字だけに絞った版（下のコマンド）。DejaVu のライセンスは、Bitstream と Vera の名前を使わなければ改変を許す |
| LiberationMono-Regular.ttf | Ubuntu の fonts-liberation | 元のファイルのまま（予約書体名「Liberation」があるので改変しない） |
| SourceSansPro-Regular.woff2、SourceSansPro-Bold.woff2 | Gradio 6.30 の同梱（中身は Source Sans 3） | 元のファイルのまま |

DejaVu の絞り方（fonttools の pyftsubset）:

```
pyftsubset /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf \
  --unicodes="U+0020-007E,U+00A0-00FF,U+0250-02FF,U+0300-036F,U+03B2,U+03B8,U+03C7,U+2013-2014,U+2018-201D,U+2026,U+2190-2193,U+2500-257F,U+2580-259F,U+25A0-25CF" \
  --flavor=woff2 --layout-features='*' --output-file=DejaVuSansMono.woff2
```

DejaVuSans.ttf も同じコマンドで作る。ライセンスの一覧は、リポジトリの一番上の THIRD_PARTY_NOTICES.md。
