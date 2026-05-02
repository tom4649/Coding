# 200. Number of Islands
- [リンク](https://leetcode.com/problems/number-of-islands/description/)
- 深さ優先探索で解いた(sol1.py)
    - はじめgridの変更を帰りがけに行ってしまい、無限ループが発生（visitedを管理すればこれでも書けるはずだが）
    - 行きがけ順に変更
    - gridでvisitedを管理している実装
- 深さ優先探索と幅優先探索の比較
    - 深さ優先探索はスタックと再帰関数を用いる実装方法がある
    - 再帰関数を用いた実装は書きやすい
    - ただし再帰が深すぎるとオーバーフローが起こる可能性がある
    - スタックを使うとこれを防げる
    - 自分で確保したスタックはヒープ領域に積まれるので、メモリが許す限りエラーは起きない
    - 再帰関数はコールスタックにフレームが積まれる
- 深さ優先探索と幅優先探索の比較
    - BFSは最短経路を見つけやすい
    - DFSは強連結成分、トポロジカルソート、サイクル検出、に応用できる
        - 強連結成分: DFSを行い帰りがけ順に番号を振る→辺を逆順にし番号が大きいものから再度DFS
        - トポロジカルソート: DFSで帰りがけ順に番号を振ればトポロジカルソートの逆順が得られる
        - サイクル検出: DFSで後退辺（探索中の頂点を訪れるか）を見る（この場合はvisitedを未訪問/探索中/探索完了で管理する）
- Pythonのスタックはcollections.dequeueを使うのが最適らしい
    - https://qiita.com/saba/items/107c4237206e31acdbef
    - 公式にも「Deque とは、スタックとキューを一般化したもの」とある
    - https://docs.python.org/ja/3.8/library/collections.html?highlight=deque#collections.deque
- 境界チェクは関数にしても良いかもしれない
    - https://github.com/Ryotaro25/leetcode_first60/pull/18#discussion_r1676873648
- 幅優先探索を使った実装
    - https://github.com/mamo3gr/arai60/blob/main/200_number-of-islands/step3.py
    - 定数をこのようにおくのは良さそう
- UnionFindも使える (sol2.py)
    - https://github.com/ichika0615/arai60/pull/9/changes/BASE..d9c2466cb7f298f4aea361af67b4a426d5d6e9b3#diff-a9252ace6e923b3224059dbabcd4824fcf13b07f168e1a31bf09af37e4720449
    - これは機能が低レベルすぎて、使う側の操作必要性が大きいとの指摘
> UnionFind の仕事をしてくれる人間いるとしましょう。自分は、numIslands の仕事をしていて電話をかけます。
> UnionFind に3種類の電話をかけているわけですが、つまり、それぞれ抽象的には「初期化」「2つが繋がっているので繋いでくれ」「ある陸地の親はどこか」を連絡しているわけですね。
> しかし、実際に頼んでいることは、一般的な自然数添字の UnionFind へのお願いですね。もうちょっと楽にしたいことを伝えられるはずなんですよ。
- メソッドは雑に呼ばれても扱えるようにするのが望ましい
    - 別の人がメソッドを使う可能性がある
    - 「将来、これをデバッグするのは自分ではない誰かと思われるので、これを条件に当てはまらないときに呼ぶと例外が投げられる、呼んだやつが悪い、というのはあまり好ましい態度ではないと思うわけです。」
    - https://github.com/sakupan102/arai60-practice/pull/18#discussion_r1582241335

### 解き直し
sol3_retry.py: DFSを自然に思いつき、stackを用いて実装
変数名にやむを得ずcurを使った
添字はrow, colが良いというレビューで指摘された点が身についていなかった
LLMにreviseさせたらかなり良くなった
