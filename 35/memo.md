# 35. Search Insert Position

sol1.py: bisect ライブラリを使うと秒殺

これでは何の練習にならないので自力で書く

sol2.py：インデックスの1のずれで混乱

sol3.pyに改善。bisect_leftに関数を分けるのもやめる


left == rightのときこれらが同時になりたつ→答え
leftに+1があるので無限ループが発生しない

https://discord.com/channels/1084280443945353267/1196498607977799853/1269532028819476562

> 二分探索を、 [false, false, false, ..., false, true, true, ture, ..., true] と並んだ配列があったとき、 false と true の境界の位置を求める問題、または一番左の true の位置を求める問題と捉えているか？
位置を求めるにあたり、答えが含まれる範囲を狭めていく問題と捉えているか？
範囲を考えるにあたり、閉区間・開区間・半開区間の違いを理解できているか？
用いた区間の種類に対し、適切な初期値を、理由を理解したうえで、設定できるか？
用いた区間の種類に対し、適切なループ不変条件を、理由を理解したうえで、設定できるか？
用いた区間の種類に対し、範囲を狭めるためのロジックを、理由を理解したうえで、適切に記述できるか？


```python
# 1.  [false, false, false, ..., false, true, true, ture, ..., true] と並んだ配列があったとき、
# false と true の境界の位置を求める問題と捉える。
# ここでは、 target より小さい値は false、 target 以上の値は true とする。
# 2. 位置を求めるにあたり、答えが含まれる範囲を狭めていく問題と捉える。
# 3. 範囲を考えるにあたり、半開区間を用いる。
# 4. 初期値は 0, len(numbers) とする。
def lower_bound(numbers, left, right, target):
    # 5. ループの終了状態で false, false, ..., false, [true), true, ..., true となって欲しい。
    # この書き方は正式な書き方ではなく、自分が考えるときのイメージです。
    # [ は区間の左端で、 true の左側にあります。 ) は区間の右端で、 true の右側にあります。
    # ただし、右側は開区間のため、インデックスの値は true の位置と同じで、 true を区間には含めない。
    # よってループの不変条件は left < right とする。
    while left < right:
        middle = (left + right) // 2
        # target より小さい値は false、 target 以上の値は true とする。
        if (numbers[middle] < target):
            # 6. 右に狭める場合。
            # middle の位置の要素を、狭めたあとの区間に含めたくない。
            # 左側は閉区間である。
            # middle の位置の要素を区間に含めないようにするには、
            # left の位置を middle + 1 にすればよい。
            left = middle + 1
        else:
            # 左に狭める場合。
            # middle の位置の要素を、狭めたあとの区間に含めたくない。
            # なぜならば、今回は境界の位置を求める問題と捉ええているためである。
            # 別の言い方をすると、境界の位置を middle より左側にしたい。
            # 右側は開区間である。
            # middle の位置の要素を区間に含めないようにするには、
            # right の位置を middle にすればよい。
            right = middle
    return left


def upper_bound(numbers, left, right, target):
    while left < right:
        middle = (left + right) // 2
        if (numbers[middle] <= target):
            left = middle + 1
        else:
            right = middle
    return left


if __name__ == '__main__':
    print(lower_bound([0, 1, 2, 3, 4, 5], 0, 6, 3))
    print(upper_bound([0, 1, 2, 3, 4, 5], 0, 6, 3))
```


保証している条件
nums[left-1] < target
nums[right] >= target or rightが右端

ループ不変条件: left < right

つまり flag_nums = [n>=target for n in nums] としたとき
i < left→ flag_nums[i] == False
i >= right →　flag_nums[i] == True
終了時 left = rightでは right: flag_nums[i] == Trueを満たす最小のi が保証される

---
## コメントをいただいて追記：

### ループ不変式:

i < left -> nums[i] <= target (1)

&& j >= right -> nums[j] > target (2)


### 成り立つことの確認

#### 初期化時: left=0, right=len(nums)
i < left, j >= rightとなるi, jは存在しない。

#### 維持: ある反復で成り立つと仮定して次の反復で成り立つことを示す。場合分け。
- nums[middle] <= target の場合: numsがソートされているため left=middle+1とした場合、(1) は依然として成立
- nums[middle] > target の場合 numsがソートされているため right=middle とした場合(2) は依然として成立

#### 終了: left < rightがFalseとなる。更新式よりleft==rightである
(1),(2)と合わせて、

i<left -> nums[i] <= target && i >= left -> nums[i] > target

これはleftがnums[i] > targetを満たす最小のiであることを意味する。


---

https://github.com/seal-azarashi/leetcode/pull/38

しっかりと理解する必要があるな

> 二分探索で「書き方」を固定することはできるのですが、「読む方法」を固定することは普通はできないです。書いている人がどういう考えで書くか普通は強制できないからです。
> ジャッジシステムを相手にしているならば別にいいのですが、人間に技術面接で出題された場合は、多くの場合、どうしてそのコードが動くのかを聞きます。
> 技術面接で見ているのが「一緒に働いたときに成果がより出るか」で、そのために必要な「簡単なコードが読めて書けて管理ができる」かを知りたいからです。(余計な絶対値があれば、分かっているかより気になるでしょう。)
> というわけで、書き方を固定してもいいけれども、幅のある表現を読めるようにしてくださいね、ということです。

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0

