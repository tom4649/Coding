# Variable-Dependency-Evaluator

https://www.screna.ai/interview-questions/applied-intuition/software-engineer

問題： 変数の定義を表す文字列のリストを受け取り、各変数の値を計算するプログラムを実装してください。

仕様：
- 各行はvariable = expression形式
- 右辺には整数、変数、+、-を使用できる
- 変数は定義される前に参照されてもよい
- 空白の数は任意
- 循環参照があればValueError("Cyclic Dependency")
- 未定義変数があればValueError("Unresolvable equations")
- 変数名は英字で始まる英数字とアンダースコアの列
- 同じ変数の重複定義はないものとする

## step1
冗長なコードになってしまった。


計算量は、parse, bfsの部分で O((文字列の合計長) + (変数の数) + (依存関係))

## step2
パース処理の重複をなくす、などの改善をAIに行ってもらった。符号を先に処理する。

## step3
今回はdfsの方が書きやすい
