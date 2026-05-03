# 122. Best Time to Buy and Sell Stock II

- 答えを見てしまった: sol1.py
    - 悔しい

https://github.com/tshimosake/arai60/pull/22/changes#diff-e262fd39a7deae3a1286c7400da3b1317672ae42e34582d8218de2c31f244292

> 最適解を $\sum_{k=1}^{n-1} \max(0, p_k - p_{k-1})$ と分解できることが本質だった。

つまり、i日に買ってj日に得る利益は $\sum_{k=i+1}^{j} (p_k - p_{k-1})$と分解できるので、これを最大化すると上の最適解となる

https://github.com/goto-untrapped/Arai60/pull/59#discussion_r1782748689

> 毎日できることは、株を持っているか、お金を持っているかの2択なので、未来が見える人になったとして、どちらがいいかを考えればいいのです。

https://github.com/tshimosake/arai60/pull/22/changes#diff-e262fd39a7deae3a1286c7400da3b1317672ae42e34582d8218de2c31f244292

> 二状態DP：各日で株を持っている/持っていない場合の最大利益を更新していって、最後に持っていない場合の最大利益を返す。関数呼び出しが頻繁にあるからか、少し遅くなった

なるほど。今株を持っているか持っていないかの二つを更新し続ければ良いのか。自分で答えに辿り着きたかった。

- sol2.py

https://github.com/mamo3gr/arai60/blob/122_best-time-to-buy--and-sell-stock-ii/122_best-time-to-buy--and-sell-stock-ii/memo.md

> max を使うほうがコードはシンプルなんだけど、前日からの差分で利益が出ているか見る、利益があるなら累積する、と手続きを書き下すほうがちょっとだけ分かりやすいような気がする。

なるほど。可読性ではこちらの方が高そう。

解けずに答えを再現しただけになったので、もう一回解きたい。
