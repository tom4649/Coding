# 2. Add Two Numbers

- [リンク](https://leetcode.com/problems/add-two-numbers/description/)
- 関数を定義して可読性を高めたつもり
- while（など）を使って一つのループ内で加算を処理する方法も見つかったが個人的には今の回答が好み

### 解き直し
多倍長整数の処理を行うように書いた

### コメント集
https://discord.com/channels/1084280443945353267/1366423240624439378/1372611463872516096
generator と　zip_longestを使う

while 文の条件にcarryを入れないで、最後に加えることもできる

https://github.com/kazukiii/leetcode/pull/6/changes/a9c7637c616aef971424c999f24d49573541daec
dummy を使わないこともできる
