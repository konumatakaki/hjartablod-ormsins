// Inky（ink の公式エディタ）で開くための書き出し。
// Inky は下ごしらえ（ink-preprocess.mjs）をしないので、半角の | のルビを全角に直したコピーを build/inky/ に作る。
// 使い方: npm run export:inky → Inky で build/inky/main.ink を開く
import { readFileSync, writeFileSync, readdirSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { preprocess } from "./ink-preprocess.mjs";

const SRC = "content/script", OUT = "build/inky";
mkdirSync(OUT, { recursive: true });
for (const f of readdirSync(SRC).filter((f) => f.endsWith(".ink"))) {
  writeFileSync(join(OUT, f), preprocess(readFileSync(join(SRC, f), "utf8")));
}
console.log(`書き出した: ${OUT}/（Inky で main.ink を開く）`);
