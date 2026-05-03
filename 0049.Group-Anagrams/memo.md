# 49. Group Anagrams

- [リンク](https://leetcode.com/problems/group-anagrams/description/)
- 愚直にsol1を書いたが計算量はO(nllog(l))
- histogramを用いる解法
    - https://github.com/ichika0615/arai60/pull/11/changes#diff-fa3129c54f54ceaf0d237e449d3491c5eb44eaa4660ae11dec87df81d245cb25
    - リストはmutableでhashableではないのでtupleに変換する必要がある
    - 計算量はO(nl)
    - 入力がアルファベット小文字以外のときには例外処理で対応
- 実行時間はsol1の方が速い
    - pythonのsortedが高速でloglが定数倍より速い？
