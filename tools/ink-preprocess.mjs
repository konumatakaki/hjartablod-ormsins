// ink に渡す前の下ごしらえ。
// 投稿サイトと同じルビの記法「|漢字《よみ》」（半角の |）を使えるようにする。
// ink では半角の | は {a|b} のような分岐の区切りに使う記号なので、そのままでは翻訳できない。
// そこで、波括弧 { } の外にある「|漢字《よみ》」だけを、全角の「｜漢字《よみ》」に置き換える。
// 波括弧の中の | は ink の記号として残す。ルビ以外の場所の半角の | も残す（ink のエラーとして見つかる）。

const RUBY = /\|([^|《》{}\n]+)《([^》\n]+)》/g;

export function preprocessLine(line) {
  // コメント（// 以降）はそのまま
  const c = line.indexOf("//");
  const body = c >= 0 ? line.slice(0, c) : line;
  const rest = c >= 0 ? line.slice(c) : "";
  let out = "", depth = 0, chunk = "";
  const flush = () => { out += depth === 0 ? chunk.replace(RUBY, "｜$1《$2》") : chunk; chunk = ""; };
  for (const ch of body) {
    if (ch === "{") { flush(); depth++; out += ch; continue; }
    if (ch === "}") { flush(); depth = Math.max(0, depth - 1); out += ch; continue; }
    chunk += ch;
  }
  flush();
  return out + rest;
}

export function preprocess(source) {
  return source.split("\n").map(preprocessLine).join("\n");
}
