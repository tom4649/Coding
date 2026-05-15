# 21. Merge Two Sorted Lists

## step1

10m 未満で解けた

## step2
解くだけなら簡単だが、ロジックが流暢かどうか

https://github.com/colorbox/leetcode/pull/5

破壊的な解法

> これも、
> ListNode * smaller = list1;
> ListNode * bigger = list2;
> としてからやっていたらそんなに違和感がないと思うんですよ。
>         while(smaller && bigger){
>             if(smaller->val > bigger->val){
>                 swap(smaller, bigger);
>             }
>             current->next = smaller;
>             current = current->next;
>             smaller = smaller->next;
>         }

`smaller`, `bigger` という作業用ポインタに置き換えると分かりやすい。

片方が尽きたらそのまま後ろにつなげばよい。
