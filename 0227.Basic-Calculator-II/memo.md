# 227. Basic Calculator II

## step1
とりあえず答えを合わせるために書き上げたもの: step1。これでも文法ミスなどで25mほどかかった。

確認: // -> 常に小さい方向に丸める, int(・ / ・) -> 小数点以下を切り捨て

## 他の人のコード

https://leetcode.com/problems/basic-calculator-ii/solutions/7632696/a-simple-solution-by-santhanapandis-5vtt/

最後に番兵として "+" を足す

https://github.com/potrue/leetcode/pull/64

## step2

無駄が多いので書き直す。一巡目で+-も処理できる。

さらに例外処理を追加。

再帰下構文解析で書く。

空ではかけず以下の自分の解法を見ながら書いた。

https://leetcode.com/problems/basic-calculator/description/


以下の文法に従う

```
expr   := term  [ ('+' or '-')  term ]*
term   := factor [ ('*' or '/') factor ]*
factor := digit+
```

## step3

再帰下構文解析を練習する
