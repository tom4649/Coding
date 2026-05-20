# 79. Word Search

## step1

全ての位置から探索する解法が思いつく。最悪だと
(m * n * 3^L) / 10^7 <= (36*3^15)/ 10^7 = 50
かかるが大丈夫だろうか。とりあえず実装してみる。

15mぐらいでかけてテストもクリアした。間違えた点：初期開始点のseenをTrueにし忘れた。

> Follow up: Could you use search pruning to make your solution faster with a larger board?

これを考えたいが案は思いつかず答えを見る。

## step2

### 他の人のコード

https://github.com/huyfififi/coding-challenges/pull/61

> というものが提示されていた。これを入れるだけでLeetCode上の実行時間ランキングでの順位が大きく上がった。

> また、wordをひっくり返して word search を行っても同じ結果が得られるので、wordの先頭と末尾の文字のboard上での数を比べて、末尾の文字の個数の方が小さかったら word をひっくり返して search した方がDFSを始める回数が少なく済む。

この通りにやったら確かにBeat 100msとなった

片方しか行わないと遅くなるのでどちらも効果がある。

> なるほど、確かに言われてみれば納得感はあるが、面接中にスラスラと思いつけるかは自信がない。word をひっくり返して探索しても同じ、というのは問題文を読んでいて気づけた方がいいだろうな。

自分はどちらも思いつかないのでまだまだなのだと思う。


https://github.com/potrue/leetcode/pull/74

早期リターン


https://github.com/thonda28/leetcode/pull/14

再帰 -> ループを自分も書いておく

次に試す方向の index を持たせておくのか。これは人のコードを見ないと書けなかったかもしれない。

再帰をスタックに置き換える場合、フレーウの状態を明示的に持つ必要がある。
