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

