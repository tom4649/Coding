# 735. Asteroid Collision

## step1
自然に左から順に処理していけばよい。23mほどかかった。

間違えた点:
- 絶対値が等しい時の処理を忘れた
- 最後に右に動いているasteroidを加えるのを忘れた

時間計算量、空間計算量ともにO(n)

## step2
解答を一瞬見るとスタックは一つで十分らしいことが分かったので考え直す。大きくシンプルになった。

まだ答えがあっていても最もシンプルなコードに直接辿りつけないことがある。

## 他の解法

https://github.com/sota009/swe-coding-practice/pull/2

https://leetcode.com/problems/asteroid-collision/solutions/8325855/stack-collision-simulation-on-beats-9415-66yi/

while else という文法を知らなかった。基礎的な話なのかもしれない。

> while-else への私の所感は、使ってもいいが、必要となる状況では関数化することなどによってより整理できる可能性が高い、というものです。

https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

> while_stmt: "while" assignment_expression ":" suite
        > ["else" ":" suite]

> C言語だと、 a < b < c が a < b and b < cにならないそうです。
> 言語間の違いを意識せずに済むという意味で、
> andを省略せずに書いてあげるのが親切かなと思いました。

これは自分も同意する



## step3
自分はwhile-elseを使いそうにないので、使わない方を書く。
処理を少しだけまとめた。

