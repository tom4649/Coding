# 42. Trapping Rain Water

## step1

思考の流れ:

問題文の理解 -> 紙に書く -> 左右を入れ替えても同じことに気づく -> 水の高さが min(max_from_left[i], max_from_right[i]) であることに気づく -> 実装

全体で 24m ほど。問題文の理解にも時間がかかる問題だった。落ち着いて考察できたから解けたが、面接の状況では同じことができないかもしれない。

時間計算量 O(n), 空間計算量 O(n)

itertools.accumulateにreversedを適用してしまい、`TypeError: 'itertools.accumulate' object is not reversible`が発生した。

---

## step2

LLMに面接官役をやらせてみる

> Alright, that’s a solid start! Your logic is perfectly correct. You recognized that the water trapped at any given bar depends on the maximum height to its left and right, which shows you understand the core mechanics of the problem.
> Using itertools.accumulate is a clever way to build the prefix and suffix maximums quickly. However, looking at this implementation, I have a few concerns regarding its efficiency and how we are managing memory.
> Let's dig a bit deeper into this. I have a few questions for you.

1.
> Your current solution runs in $O(N)$ time, which is great. But what is the space complexity here?
> The Follow-up: "Can you optimize this to $O(1)$ auxiliary space? Imagine the input array has millions of elements; allocating all these extra lists will heavily tax the memory. Hint: Think about how we can use pointers to calculate this on the fly."

2.
> The Issue: You are reversing the list, accumulating it, converting it to a list, and then reversing it again via slicing [::-1].
> The Follow-up: "While it works, this involves multiple passes over the data just to set up the right-side maximums. It feels a bit clunky. Is there a way we can find the trapped water without needing to pre-compute and store the entire right-side history?"

3.
> The Issue: You calculated the differences first, stored them in lists, and then zipped them again. You could have just zipped max_from_left and max_from_right directly to find the bottleneck height.
> The Follow-up: "Mathematically, the water at index i is just min(max_left[i], max_right[i]) - height[i]. Why did we create two separate intermediate lists for the differences? Could we compress this logic?"

1, 3を受けて改善した。順方向のmaxはiteratorなのでメモリを消費しないが、逆方向はlistに変換するせいでO(n)のメモリを避けられない。

2でtwo pointerというキーワードが出た。解いているときに空間計算量 O(n) はかかってしまうだろうと考えて書いていたが、O(1)にできるらしい。

左と右のポインタのうち、小さいことが確定した時点でポインタを進められることに気がつきtwo pointerの解を得た。20mほどかかった。

過去に似た問題を解いた気がしたので、確認してみると以下の問題だった。

https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=rab78cw1

## 他の人のコード

https://github.com/shining-ai/leetcode/pull/63

スタックを使った解法は思いつかなかった。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left_walls = []
        total_water = 0
        for right in range(len(height)):
            while left_walls and height[left_walls[-1]] <= height[right]:
                bottom_index = left_walls.pop()
                if not left_walls:
                    break
                left = left_walls[-1]
                distance = right - left - 1
                depth = min(height[left], height[right]) - height[bottom_index]
                total_water += distance * depth
            left_walls.append(right)
        return total_water
```

> max_left ですと、最大の左を表しているように感じられます。 max_heights_in_left あたりはいかがでしょうか？

listであることがわかりやすいので、step1_revisedに反映する。max_heights_from_leftとした

https://github.com/Yuto729/leetcode/pull/69/changes

> Two Pointer 系の整合したコードの書き方

step2_two_pointerは (l, r) を未処理範囲としている。

step2_two_pointer2として [l, r]を未処理範囲としたものも書く。


## step3

最も馴染みの薄いstackを用いた解法を書く。
