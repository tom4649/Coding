# 224. Basic Calculator

## step1
難しくなさそうだと思ったが、処理に手間取り、32mほどかかった。一度再帰で書こうとしたがうまく書けずにスタックを用いた解にした。

式は再帰的だから、stackまたは再帰関数を用いれば良いというのはどこかで経験がある気がする。似た問題を見たことがある。

カッコの処理で、スタックに符号を入れ忘れて間違えた。

## step2
再帰関数で書く。スタックの解を書いた後なので、スムーズにかけた。

## 他の人のコード

https://github.com/shining-ai/leetcode/pull/65

- int() 関数は許容されているのか？自分は使わないで書いたが、char単位ならば大きな違いはない。
- 以下のコードは一見何を行っているのかわからなかったが再帰下降構文解析というらしい。言葉の文法を、そのまま再帰関数に置き換えて、上から下へと解析していく。

https://ja.wikipedia.org/wiki/%E5%86%8D%E5%B8%B0%E4%B8%8B%E9%99%8D%E6%A7%8B%E6%96%87%E8%A7%A3%E6%9E%90

https://dai1741.github.io/maximum-algo-2012/docs/parsing/

```python
class Solution:
    def calculate(self, s: str) -> int:
        index = 0

        def expr():
            nonlocal index
            if index < len(s) and s[index] == "-":
                index += 1
                result = -factor()
            else:
                result = factor()

            while index < len(s) and s[index] in "+-":
                op = s[index]
                index += 1
                if op == "+":
                    result += factor()
                else:
                    result -= factor()
            return result

        def factor():
            nonlocal index
            if index < len(s) and s[index] == "(":
                index += 1
                result = expr()
                index += 1  # ")"を読み飛ばす
                return result
            result = 0
            while index < len(s) and s[index].isdigit():
                result = 10 * result + int(s[index])
                index += 1
            return result

        s = s.replace(" ", "")
        return expr()
```

以下のような文法に基づいていると解釈できる。一般的にはtermは乗除算も含むらしいが。

```txt
expr   := <term> | <expr> + <factor> | <expr> - <factor>
term := <factor> | - <factor>
factor := (<expr>) | <number>
number := [0 - 9]+
```

これを明示的にして書いてみる

https://github.com/fhiyo/leetcode/pull/8

スペースも文法に追加している



### Pythonの文法
https://docs.python.org/3/reference/grammar.html

Parsing Expression Grammar という文法で書かれている。

---

LLMによるまとめ

学部の授業を見返したがほとんど覚えていない...

## 1. 構文解析のアプローチ分類

構文解析（パースツリーの構築方法）には、大きく分けて**トップダウン**と**ボトムアップ**の2つのアプローチがある。

| 項目 | 再帰下降構文解析（トップダウン） | CKY法（ボトムアップ） |
| :--- | :--- | :--- |
| **解析の方向** | **上から下へ**（全体の式 $\rightarrow$ 細部へ分解） | **下から上へ**（文字 $\rightarrow$ 塊へ積み上げ） |
| **主な用途** | プログラミング言語のコンパイラ、数式評価 | 自然言語処理（人間の言葉の解析） |
| **アルゴリズム** | 再帰関数、関数コールスタック | **動的計画法（DP）**（2次元テーブルの利用） |
| **文法の制約** | 左再帰のない文法（LL文法など） | チョムスキー標準形（CNF）への変換が必要 |
| **計算量** | 基本的に高速（先読みができれば $O(N)$） | 曖昧な文も解けるが重い（$O(N^3)$） |

---

## 2. LL(k)文法 と 再帰下降構文解析

* **LL(k)文法**
  * 入力を**L**eft-to-right（左から右へ）読み、**L**eftmost derivation（最左導出）で構文木を作り、次の文字を **$k$ 文字先読み（Lookahead）** すれば、次にどのルールを適用すべきかが一意に決まる文法。
* **再帰下降構文解析**
  * LL文法のルールを、そのまま「相互に再帰呼び出しする関数」としてコードに落とし込んだ実装手法。

### ⚠️ 左再帰（Left Recursion）の罠
以下のような、ルールの先頭（一番左）に自分自身が登場する文法はLL文法にできない。そのまま再帰下降でコード化すると**無限ループ**になる。
```txt
❌ 左再帰の例: expr := expr + term
