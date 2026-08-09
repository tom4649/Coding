# 1235. Maximum Profit in Job Scheduling

## step1

流れ：

DPで解くことを考える -> 制約的に時間計算量はO(n^2)が厳しいと判断 -> 価値が制約にならないのでナップザックDPは難しそうだと考える -> 二次元DPは時間計算量的に難しそうだと判断 -> start timeのソート、座標圧縮

30m ぐらい考えて方針が立たず、Hint 2を見て解いた。

> Hint 2: Sort the elements by starting time, then define the dp[i] as the maximum profit taking elements from the suffix starting at i.

二分探索を用いて O(nlog n)で解けることには気がついた。

変数名などを適当にとりあえず書いたのが step1.py, 変数名を改善したのが revised

### LLMとの対話

私がこの問題を解いた時の思考の流れは以下の通りでした。この問題をHintを見ずに自力で解くためには、どのような思考が必要なのでしょうか？

> ここで必要なのは、「『どの区間を組み合わせるか』ではなく、『各時点で、それ以降の未来の最適な選択は何か』に注目する」 という思考の切り替えです。

> ブレイクスルー:「時間軸の『ある時点 $i$』に自分が立っているとする。ここから先の未来（サフィックス）だけを見て、得られる最大利益はいくらか？」

> 依存関係を一方通行にする「未来から過去へ」の思考:

> 多くの人はソートした後に「前から順に（プレフィックスで）」DPを組もうとして挫折します。

> 閃きのトリガー:
> ソートした基準（今回は startTime）が、次の状態の条件（endTime <= startTime）と直結している場合、「条件を満たす要素が綺麗に片側に寄る方向」からDPを埋めるのが鉄則です。


## step2

もう一度考えてみると、自力で異なる解法を導けた: sol2_from_start.py

前から見ていくのでこちらの方が個人的には素直。step1で解けなかったのは、start time のソートにこだわって、end timeのソートを深く考えなかったため。時間tでちょうど終わる時刻がある場合に更新が行われることがポイントだと思う。

## 他の人のコード

https://github.com/shining-ai/leetcode/pull/66

> DPとメモ付き再帰は同じものだと思っていました。 再帰の結果を保存するのがメモ付き再帰で、 ループで結果を保存するのがDP?

level_2, level_3は自分のstep1と同じ解法だがメモ化再帰で書かれている。こちらの方がわかりやすいと感じた。


> level 1 は、第一感やや複雑に感じました

ヒープの解法。自分はDPしか頭になかったので全く思いつかなかった。
手続き的に考えると自然にも思えると個人的には思った。

```python
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = list(sorted(zip(startTime, endTime, profit)))
        jobs.append((float("inf"), float("inf"), 0))
        max_profit = 0
        running_jobs = []
        for job_start, job_end, job_profit in jobs:
            while running_jobs and running_jobs[0][0] <= job_start:
                _, max_profit_from_running_job = heapq.heappop(running_jobs)
                max_profit = max(max_profit, max_profit_from_running_job)
            heapq.heappush(running_jobs, (job_end, max_profit + job_profit))
        return max_profit
```

## step3
TODO
