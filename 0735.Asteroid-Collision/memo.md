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

https://leetcode.com/problems/asteroid-collision/solutions/8325855/stack-collision-simulation-on-beats-9415-66yi/

while else という文法を知らなかった。基礎的な話なのかもしれない。

https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

> while_stmt: "while" assignment_expression ":" suite
        > ["else" ":" suite]


## step3

処理を少しだけまとめた。

