# 153. find-minimum-in-rotated-sorted-array

最初の要素をpivotとしてその大小比較を用いた二分探索で解ける

sol1.py:
不等号の立て方など一発で通せたわけではない
フラグにTrueが存在しないときの場合分けを以下のようにしていた
```python
if pivot <= nums[-1]:
    return pivot
```
が、最後に場合分けをしても良いことに気づいた
```python
return nums[left] if left < len(nums) else pivot
```


「二分探索で解く」という解法なら、sol2.pyの場合分けが良いと思う。
sol2.pyにはループの条件を考えたコメントを加えた。


https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0

> この問題、隣り合う a, b で、nums[a] > nums[b] となるものを探せ、ということだと思うと、閉区間でとるほうが自然かしら。

> 二分探索は、コードのパターンで覚えて書くのではなく、探索範囲が閉区間・半開区間・開区間のどれなのかを意識し、範囲を狭めるときに、範囲の端をどこまで狭めればよいかを意識して書くとよい

半開区間、閉区間のどちらでも書けるようにしておきたい。

> いましていることをメタ的にいうと、選択肢、つまり、考察の幅自体を広げたいと思っています。
> nums[0] <= nums[i] な領域と nums[0] > nums[i] な領域の境界を探せ
> nums[-1] < nums[i]  な領域と nums[-1] >= nums[i] な領域の境界を探せ

```python
def findMin(self, nums: List[int]) -> int:
        return nums[bisect_left(nums, True, key=lambda x: x <= nums[-1])]
        return nums[bisect_left(nums, True, key=partial(ge, nums[-1]))]
        return nums[bisect_right(nums, False, key=lambda x: x < nums[0]) - len(nums)]
```

> 「ここはこっちでもよくないですか」みたいなのはときどき聞かれますが、一度にたくさんは聞かれません。
> 対面だと2,3回やりとりをすると、意味が分からずに書いていると確信できるのですが、文字だけだと「なんか違和感があるが確信はできない」くらいになるので、長めに聞いています。
> left は要するに意味としては、
> 「左側、つまり、条件を満たさないことが判明している左側の最大の場所」か
> 「左側、つまり、条件を満たさないことが判明していない左側の最小の場所」かのどちらかを略して left と書いていることが多いんですよね。
> ただ、このあたりを分かっていないと、途中で言っていることをころころ変えます。

自分の場合は「左側、つまり、条件を満たさないことが判明している左側の最大の場所 + 1」

https://github.com/mamo3gr/arai60/blob/153_find-minimum-in-rotated-sorted-array/153_find-minimum-in-rotated-sorted-array/memo.md

https://github.com/naoto-iwase/leetcode/pull/25

> 私は最後に返したほうの不変条件を分かりやすくするために、最後に返す方を先に書くのですがこれは好みかもしれません。

なるほど。



bisect_left, bisect_rightを使う, nums[-1]と比較する、を自分でも書く


https://github.com/garunitule/coding_practice/pull/42#discussion_r2633261407

bisectを使った 4通り
あなたのプロンプト
bisect_right: 指定した値と同じ要素が続く区間の、一番右側のインデックス + 1
bisect_left: 指定した値と同じ要素が続く区間の、一番左側のインデックス
