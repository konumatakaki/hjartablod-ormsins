// 台本（content/script）を検査する。
//   1. ink として正しく翻訳（コンパイル）できるか
//   2. このプロジェクトの約束（タグ、話者、ルビ、用語）を守っているか
// 使い方: npm run check:content
import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { Compiler, CompilerOptions } from "inkjs/full";
import { PosixFileHandler } from "inkjs/compiler/FileHandler/PosixFileHandler";
import { preprocess, preprocessLine } from "./ink-preprocess.mjs";

const SCRIPT_DIR = "content/script";
const ROOT = "main.ink";

// 使ってよいタグ（# の後ろ）。増やすときはここと content/README.md を更新する
const TAGS = ["場面", "通信", "show_card", "utter", "replay", "layout", "mind"];
// 台詞を言える人
const SPEAKERS = ["私", "リーダー", "エンジニア"];

let errors = 0, warnings = 0;
const err = (m) => { errors++; console.log("エラー  " + m); };
const warn = (m) => { warnings++; console.log("注意    " + m); };

// 1. 翻訳
const messages = [];
// 読み込んだファイルの中身を、翻訳の前に下ごしらえ（ink-preprocess.mjs）する
const files = new PosixFileHandler(SCRIPT_DIR + "/");
const handler = {
  ResolveInkFilename: (name) => files.ResolveInkFilename(name),
  LoadInkFileContents: (name) => preprocess(files.LoadInkFileContents(name)),
};
const options = new CompilerOptions(ROOT, [], false,
  (message, type) => messages.push({ message, type }), handler);
try {
  new Compiler(preprocess(readFileSync(join(SCRIPT_DIR, ROOT), "utf8")), options).Compile();
} catch (e) {
  if (!messages.length) messages.push({ message: String(e), type: 2 });
}
for (const { message, type } of messages) (type === 2 ? err : warn)("ink: " + message);

// 2. 約束
for (const file of readdirSync(SCRIPT_DIR).filter((f) => f.endsWith(".ink"))) {
  readFileSync(join(SCRIPT_DIR, file), "utf8").split("\n").forEach((raw, i) => {
    const at = `${file}:${i + 1}`;
    const line = preprocessLine(raw).replace(/\/\/.*$/, "").trim();
    if (!line) return;
    for (const m of line.matchAll(/#\s*([^\s:#]+)/g)) {
      if (!TAGS.includes(m[1])) warn(`${at} 知らないタグ「#${m[1]}」`);
    }
    const speaker = line.match(/^([^\s「*+\-=~#]{1,12})「/);
    if (speaker && !SPEAKERS.includes(speaker[1])) warn(`${at} 知らない話者「${speaker[1]}」`);
    const opens = (line.match(/《/g) || []).length, closes = (line.match(/》/g) || []).length;
    if (opens !== closes) err(`${at} ルビの《》の数が合わない`);
    if (line.replace(/\{[^}]*\}/g, "").includes("|")) err(`${at} ルビ以外の場所に半角の「|」がある（ink の記号として読まれる）`);
    if (line.includes("｜") && !/｜[^《》｜]+《[^》]+》/.test(line)) warn(`${at} 「｜」の後にルビ《》がない`);
    if ((line.match(/\[\[/g) || []).length !== (line.match(/\]\]/g) || []).length) err(`${at} 用語の [[ ]] の数が合わない`);
  });
}

console.log(`\nエラー ${errors} 件、注意 ${warnings} 件`);
process.exit(errors ? 1 : 0);
