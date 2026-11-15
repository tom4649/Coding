# 527. Word Abbreviation

## step1
N = words.length

L = len(word) とする

計算量：O(N * L^2 + Nlog N)

改善してソートを削減。

## step2

Trie 木を使うことが回答に書かれていた。最近書いたのに思いつくことができなかった。

計算量 O(NL)

## step3


---

Can we assume all words in the input list are unique, or could there be duplicates?

Could the input list be empty, or contain empty strings?

Just to confirm the rule: if the abbreviation isn't strictly shorter than the original word—like for 3-letter words such as 'dog'—we keep the original word as is, right?

Are all words guaranteed to be lowercase English letters, or do we need to handle uppercase letters and special characters as well?

we need to return the abbreviations in the exact same order as the input list, correct?
