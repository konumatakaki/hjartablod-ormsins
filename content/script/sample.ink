// 書き方の見本。文章の部分は空欄（括弧）にしてある。
// 実際の台本では、このファイルを消して、日ごとのファイル（day1.ink など）を作る。

VAR shown_bread = false

=== sample_session ===
#場面 2026-10-15 13:10 / 面接室 / 聞き取り2
（内省: 聞き取りを始める前の主人公。｜椅子《いす》のルビの例。[[有気音]] の例）

- (choose)
* [見せる: 絵カード「パンを食べる人」]
    ~ shown_bread = true
    #show_card: bread
    #utter: g_014
    （内省: 少女の反応を見た主人公）
    リーダー「（台詞）」 #通信
    -> choose
* [待つ]
    #utter: g_015
    （内省: 待った結果）
    -> choose
* {shown_bread} [聞き直す: さっきの発話]
    #replay: g_014
    （内省: 聞き直した主人公）
    -> after

= after
（内省）
-> END
