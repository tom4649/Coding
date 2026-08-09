# 110. Balanced Binary Tree

## step1

再帰でpost-orderのDFSを実装した。

## step2

### 他の人のコード
https://github.com/huyfififi/coding-challenges/pull/11/changes

> いや、私の良くするたとえ話としてね、木の全ノードに部下を立たせるんですよ。
> そうすると、nonlocal って、部下たちのいる部屋に共通の看板を立てておいて、全部下がその看板に書いたり消したりするんですよね。
> それだったら、部下同士のやり取り(関数呼び出し)の中で、自分より下の部分の `max_sum` の情報も報告するようにしたほうがスマートじゃないでしょうか、ということです。
> たとえば、こっちの方がスレッド増やしたくなったときに並列性が良さそうです。

nonlocal に頼らず「子から親へ情報を返す」ほうがスマート


https://github.com/ryosuketc/leetcode_grind75/pull/11/changes

https://github.com/Kitaken0107/GrindEasy/pull/16

この解法はO(n^2)となるが自分は逆にこれを思いつかなかった


ループに書き直すもの（辞書を使う）、ブール値を変えさず-1で処理するもの、望ましくない実装、を書いておく

書く中で None も dict のキーにできる -> **hashable** だと気づいた（これまで意識していなかった）。

昔のはなし
https://stackoverflow.com/questions/7681786/how-is-hashnone-calculated

- **昔の CPython（議論の中心だった頃）**: `hash(None)` は **`id(None)` を材料にした通常のオブジェクト用ハッシュ**（アドレスをビットいじりしたもの）になっていた、という説明が有力。**`None` は `_Py_NoneStruct` のように C 側で一個だけ用意されるシングルトン**なので、**同一ビルド・同一環境ではインタプリタを再起動してもメモリ上の位置が（かなりの確率で）変わらず、`hash(None)` も同じ値に見える**、というのが受け付け回答の趣旨。**別ビルド・別マシンでは値が変わりうる**点もセット。
- **実装の話と言語モデル**: **キーに必要なのは hashable（不変な同一性・ハッシュの安定）などの条件で、`None` はシングルトンとしてそれを満たす**。
- **Python 3.12 以降**: [CPython PR #99541](https://github.com/python/cpython/pull/99541) で、**再現性の支援のため `None` のハッシュを固定の定数にする変更**が入った。
