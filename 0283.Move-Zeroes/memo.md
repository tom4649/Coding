# 283. Move Zeroes

ゼロの最初のインデックスとノンゼロの最初のインデックスを覚えておいて、それらを入れ替える操作を続ければ良い

sol1.py: この操作を素直に書いた。が、コードが長くなって可読性が低い
sol2.py: 似た操作を関数化してわかりやすくしたつもり。ただし、同じアルゴリズムなのに関数の呼び出しによって速度が落ちてしまった

sol3.py: よく考えるとscannnig indexはnonzeroに対してのみ操作を行うので、forとif文で置き換えられることに気づく


### コメントと他の方のコード

https://github.com/fhiyo/leetcode/pull/54/changes/BASE..40f6172e4c7a6b29303a6b66464dd512300ac477#diff-2f8b85074aa38861aa9dd6fbe0c5f1b540a06f8618d7552b4ffd05da21f795d3

inplaceだけど他の配列を用意しても解くことはできる。
inplaceの意味がなくなりそうだけど

解法2は変数名までほぼ同じ。自然な解法ということだろうか。クイックソートのpartitionと似ているのはなるほど。

https://github.com/fhiyo/leetcode/pull/54#discussion_r1729721970

関数化しているのも自分のと同じ考え方だ

https://github.com/olsen-blue/Arai60/pull/55#discussion_r2024137192

> Generator を使って変なコードを書いてみました
> StopIteration を捕まえるのが正しいでしょうね。
> next の第2引数の default を使えば例外がなくせますね。

Generatorを使って走査するのか。自分では思いつきそうにない。

https://github.com/shining-ai/leetcode/pull/54

> first_zero_index というか、私の感覚は、ゼロが削除された文字列の長さですね。

> https://en.wikipedia.org/wiki/Erase–remove_idiom
> Erase–remove idiom
> が頭に思い浮かんでいたら、助けになるかもしれません。

背景はこれなのかな。
remove削除するように見せかけて削除条件に合わないものを前側によせるアルゴリズム。
削除だけを行うeraseでは毎回削除した要素の後ろにある要素を全て前に詰める必要がある。
removeを行ったあとにeraseを行うと、要素を前に詰める操作を一回にまとめることができる


https://github.com/mamo3gr/arai60/blob/283_move-zeroes/283_move-zeroes/memo.md

https://github.com/mamo3gr/arai60/blob/283_move-zeroes/283_move-zeroes/step2_linked_list.py

Linked listを使って解いている
