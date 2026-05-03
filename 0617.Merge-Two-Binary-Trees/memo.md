# 617. Merge Two Binary Trees
- https://leetcode.com/problems/merge-two-binary-trees/description/
- sol1.py: 再帰で書いた。Noneの場合分けをわずかに工夫したつもりではいる。
    - 他の人のコードを読んで、このコードは破壊的であることを認識した。自分で気にできるようになりたい。
- sol2.py: 非破壊的になるように書いた
    - 速度は遅くなった
- https://github.com/Shoichifunyu/shofun/pull/17/changes
    - mergeTreesの内側に関数を定義する必要はないだろう
    - nodeのNone処理は似ている（真似てはいない）
- https://github.com/mamo3gr/arai60/blob/617_merge-two-binary-trees/617_merge-two-binary-trees/memo.md
    - https://docs.python.org/3.13/library/copy.html
    - deepcopyは新しいオブジェクトのコピーを挿入する
    - 複合オブジェクトでない場合には違いは生じない
> 浅いコピー (shallow copy) は新たな複合オブジェクトを作成し、その後 (可能な限り) 元のオブジェクト中に見つかったオブジェクトに対する 参照 を挿入します。
> 深いコピー (deep copy) は新たな複合オブジェクトを作成し、その後元のオブジェクト中に見つかったオブジェクトの コピー を挿入します。

- stackを用いた解法
    - https://github.com/tarinaihitori/leetcode/pull/23/changes/BASE..3661cef8b334d992a50e919393c5db1b8e22f9e0#diff-1ede2b2a752e6743ca4d35b115594d80caecd186a464943ab76618d8d1811252
    - 部分関数を使ってpythonでポインタを実装している
    - 面白いので写経してみる
> Python は、メンバ変数へのポインターが持てないので、どうしても繰り返し感がでますね。下のような方法は一応考えてみました。
> これも別に良いコードではないですが、C++ だとどこに書き込むかをスタックに積むことができるので、少し簡単になるのです。それを擬似的に Python で表現してみました。



