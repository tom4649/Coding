# 202. Happy Number

## step1
Falseのときに循環が生じることへの確証がないが、これを仮定して実装を行う。6mぐらい。

## 他の人のコードなど

https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E6%95%B0

確かに循環が生じるようだ。

> ハッピー列は1か4に到達する

https://www.reddit.com/r/learnmath/comments/nuyqf7/how_to_prove_that_happy_numbers_form_a_cycle/?tl=ja

循環の証明。桁数 n >= 5 の場合に 10^(n-1) > 81nなので5桁以上になったあと、次の数字は元の数より小さくなる。
4 桁の最大値である 9999 の二乗和は243なので、どんなに大きな数になってもいずれ1以上243以下の値となる。
あとは鳩の巣原理で循環があることが示せる。

https://github.com/hhhirokunnn/studyAlgo/pull/2#pullrequestreview-2056729822

- https://docs.python.org/3/library/functions.html#divmod
- Floyds Cycle-Finding

「循環」が出てきたらFloyds Cycle-Findingが選択肢に入るようにしたい
