# 317. Shortest Distance from All Buildings

## step1
一度解いたことがあった

Builing からの BFS を行う（EMPTYからの BFSも考えられる）

## step2
num_reached を利用した枝刈りを加えた

最初nonloal をつけずにエラーとなった

pythonの変数規則はLEGB

今のコードでは代入文があるのでスコープがローカルになるが、はじめの代入で同時に参照を行っているため名前解決ができずエラーが生じる

listの場合はmutableなので、代入をしているわけではなく、変数のスコープは Enclosing で解釈されるため、エラーは生じない
