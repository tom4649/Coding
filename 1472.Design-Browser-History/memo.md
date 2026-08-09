# 1472. Design Browser History

## step1
まずlistを使ってとく。

step1_del.py: 最初にlistの要素を消去することを考えたが、配列のコピーが発生する

step1_del_v2.py: コピーを防ぐために del を使用

step1_overwrite.py: lengthをクラスで管理する

実行時間的にはstep1_overwrite.pyがもっとも速いが、不要なメモリを解放できることを考えるとstep1_del_v2.pyがもっとも良いと思った。

LinkedListを使ってもとく。この場合はGCによってメモリが自然に解放される。ただし、履歴の移動でO(steps)かかる。

## step2

https://leetcode.com/problems/design-browser-history/solutions/674486/two-stacks-pretty-code-by-interviewrecip-kbz8/

two stackを使った解法。履歴の移動でO(steps)かかる。

以下の問題でも見たことがある。

https://leetcode.com/problems/implement-queue-using-stacks/description/

自分で思いつくことができなかった。

過去と未来を行き来するような状況で発想できるようにしたい。


https://chromium.googlesource.com/chromium/src/+/main/docs/session_history.md

実際のブラウザがどうなっているか少し調べた。

> Chromium tracks the session history of each tab in NavigationController, using a list of NavigationEntry objects to represent the joint session history items. Each frame creates session history items as it navigates. A joint session history item contains the state of each frame of a page at a given point in time, including things like URL, partially entered form data, scroll position, etc.

リストとして管理しているようなので、配列の解法が最も近そう

> Each NavigationEntry uses a tree of FrameNavigationEntries to track this state.

Webページでは内部に複数のiframeがネストされているので、木構造で管理している

