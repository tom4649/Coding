# 528. Random Pick with Weight

## step1
9mぐらいでまず naive を書く。計算量 O(N)。

bisectを使って高速化。計算量 O(log N)

## step2
いい加減な名前で書いてしまったので改善

乱数の書き方を調べる:

- random.randint: uniformと同じ書き方で書ける。もともと整数なのでこちらの方が良さそう
- random.choices: `return random.choices(list(range(len(self.prefix_sums))), cum_weights=self.prefix_sums)[0]`
    - 内部で二分探索が走っている
    - https://github.com/python/cpython/blob/219768ff531fc0686de623139562ee9f9537df98/Lib/random.py#L460
- np.random.choice: O(N)だがバッチジョブだと高速化

---

Alias method

https://leetcode.com/problems/random-pick-with-weight/solutions/671439/python-smart-o1-solution-with-detailed-e-r0gx/?envType=problem-list-v2&envId=7p55wqm

https://en.wikipedia.org/wiki/Alias_method

O(N)の前計算を行なっておくことでO(1)で生成できる

乱数を考えると非効率な状況もある（e.g. p= 1/2, 1）

## step3
TODO: alias法を書く
