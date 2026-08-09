# 210. Course Schedule II

## step1
最初集合で先祖を管理しようとしたが、閉路検出ができないことに気づき、statusを使う方針に書き換えた。
19mほど。

## 他の人のコードなど

> DFSのトポロジカルソートですが、preorder（行きがけ）でTEMPORARYとマークか、すでにTEMPORARYなら、サイクルと判定。postorder（帰りがけ）でPERMANENTとマークするみたいな感じですね。

https://github.com/potrue/leetcode/pull/77/changes

入次数で管理するやり方。Kahnのアルゴリズムというものだった。他の問題で見た覚えがあるが使えなかった。

https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%9D%E3%83%AD%E3%82%B8%E3%82%AB%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88

Kahnのアルゴリズムを書くのはBFS, DFSどちらでも可能だがBFSで実装する。

## step2
変数名を具体的にする
