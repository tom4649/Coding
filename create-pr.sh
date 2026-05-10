#!/bin/bash

# 使用方法: ./create-pr.sh "Current Problem URL" "Problem Number (optional)"
# 例: ./create-pr.sh "https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/" "62"
#
# 前提: 既にブランチが作成されており、そのブランチで作業中であること

CURRENT_PROBLEM_URL=$1
PROBLEM_NUMBER=$2

if [ -z "$CURRENT_PROBLEM_URL" ]; then
  echo "使用方法: ./create-pr.sh <現在の問題URL>  [Arai60通し番号]"
  echo "例: ./create-pr.sh \"https://leetcode.com/problems/two-sum/description/\" \"47\""
  exit 1
fi

# URLから問題名を抽出する関数
extract_problem_name() {
  local url=$1
  # URLから "two-sum" のような部分を抽出
  local slug=$(echo "$url" | sed -n 's|.*/problems/\([^/]*\).*|\1|p')
  # ハイフンをスペースに変換し、各単語の最初の文字を大文字に
  local title=$(echo "$slug" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')
  echo "$title"
}

CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "main" ] || [ "$CURRENT_BRANCH" = "master" ]; then
  echo "エラー: mainブランチから実行しています。"
  echo "問題用のブランチを作成してから実行してください。"
  exit 1
fi

echo "現在のブランチ: $CURRENT_BRANCH"

# 現在の問題名を抽出
CURRENT_PROBLEM_TITLE=$(extract_problem_name "$CURRENT_PROBLEM_URL")
echo "現在の問題: $CURRENT_PROBLEM_TITLE"

echo "PRボディを作成中..."
cat > .github/pull_request_template.md << EOF
[${CURRENT_PROBLEM_TITLE}](${CURRENT_PROBLEM_URL})
EOF

echo "リモートにプッシュ中..."
git push -u origin "$CURRENT_BRANCH"

echo "PRを作成中..."
PR_URL=$(gh pr create \
  --base main \
  --head "$CURRENT_BRANCH" \
  --title "${CURRENT_PROBLEM_TITLE}" \
  --body "${CURRENT_PROBLEM_URL}")

PR_NUMBER=$(echo "$PR_URL" | grep -o '[0-9]*$')

git restore .github/pull_request_template.md
echo "PR作成完了！ ${PR_URL}"

# レビュー依頼コメントを生成
if [ -n "$PROBLEM_NUMBER" ]; then
  TITLE_LINE="${PROBLEM_NUMBER}. ${CURRENT_PROBLEM_TITLE}"
else
  TITLE_LINE="${CURRENT_PROBLEM_TITLE}"
fi

echo ""
echo "=== レビュー依頼コメント (コピー用) ====================="
cat << EOF
お疲れ様です。
${TITLE_LINE}に取り組みました。
お手隙の際にレビューをお願いいたします。
問題: ${CURRENT_PROBLEM_URL}
PR: ${PR_URL}
言語: Python3
EOF
echo "========================================================="
