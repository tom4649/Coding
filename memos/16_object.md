# 【Pythonで学ぶオブジェクト指向】Class, Object, Enum, インターフェースの本質を徹底解説！

オブジェクト指向プログラミング（OOP）や低レベル設計（LLD）を学び始めると、必ず出会うのが**「クラス」「オブジェクト」「Enum（列挙型）」「インターフェース」**という言葉である。

なんとなく使っている方も多いかもしれないが、それぞれの本質とPythonでの正しい使い方を理解すると、コードの品質や設計の綺麗さが劇的に向上する。

今回は、Pythonの具体的なコードを交えながら、これらの概念をスッキリ図解・解説する。

---

## 1. 「Class」と「Object」の基本
まずはすべての土台となる「クラス」と「オブジェクト」である。

* **Class（クラス）：** オブジェクトを作るための **「設計図」**。
* **Object（オブジェクト / インスタンス）：** 設計図から作られた **「実体（中身のあるもの）」**。

### Pythonでの使い方
```python
# クラス（設計図）の定義
class Dog:
    def __init__(self, name):
        self.name = name  # 属性（メンバ変数）

    def bark(self):       # メソッド（振る舞い）
        return f"{self.name}が吠えました！"

# オブジェクト（実体）の生成
dog1 = Dog("ポチ")
dog2 = Dog("タロウ")

print(dog1.bark())  # ポチが吠えました！
print(dog2.bark())  # タロウが吠えました！
```

通常のクラスは、Dog("ポチ") のように () をつけて呼び出すことで、初めてメモリ上に実体（オブジェクト）が作られる。

### 2. Enum（列挙型）
Enum（列挙型）は、曜日や通貨、ステータスなど「関連する固定の選択肢（定数）」をグループ化するための仕組みである。

PythonのEnumには、通常のクラスとは違う「特殊な魔法（仕組み）」がある。それは、「クラスの中に書かれた定数（メンバ）が、すでにそのクラスのオブジェクトとして自動生成されている」という点である。

#### Pythonでの使い方

```python
from enum import Enum

class Coin(Enum):
    # これらは単なる数字ではなく、すでにCoinクラスの「オブジェクト」！
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

    def __init__(self, value):
        self.coin_value = value

    def get_value(self):
        return self.coin_value

# () をつけてインスタンス化しなくても、最初からメソッドが呼べる！
total = Coin.DIME.get_value() + Coin.QUARTER.get_value()
print(total)  # 35
```
Pythonがこのコードを読み込んだ瞬間、裏側で自動的に以下のようにオブジェクトが生成され、固定されている。

- Coin.DIME は、内部で Coin(10) として出来上がった独立したオブジェクト
- Coin.QUARTER は、内部で Coin(25) として出来上がった独立したオブジェクト

だからこそ、それぞれのオブジェクトが別々の値（10や25）を保持し、メソッドを呼び出すことができるのである。

### 3. 「インターフェース」とPythonの「ABC」

インターフェースとは、具体的な処理（中身）を書かずに、「このクラスは、絶対にこのメソッドを持っていなければならない」というルール（契約）だけを定めたものである。

Pythonには interface という専用のキーワードがない。代わりに ABC (Abstract Base Class: 抽象基底クラス) と @abstractmethod というデコレータを使ってインターフェースを再現する。

#### Pythonでの使い方

```python
from abc import ABC, abstractmethod

# ABCを継承して、ルール専用のクラス（インターフェース）を作る
class PaymentGateway(ABC):

    @abstractmethod
    def initiate_payment(self, amount):
        """このメソッドは子クラスで必ず上書き（実装）しなければならない"""
        pass

# ルールに従って具体的なクラスを作る
class PayPayGateway(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"PayPayで{amount}円を決済しました。")

# ❌ もし実装し忘れたら？
class BadGateway(PaymentGateway):
    pass

# gateway = BadGateway()
# → TypeError: Can't instantiate abstract class BadGateway... となり実行前に防げる！
```

- ABC をつけることで、不完全な設計図である PaymentGateway 自体が誤ってオブジェクト化されるのを防ぐ。
- @abstractmethod をつけることで、子クラスに対して「メソッドの実装」を強制する。

これを行うことで、呼び出し側は相手がPayPayだろうがクレジットカードだろうが、安心して initiate_payment() を呼び出すことができるようになる（これをポリモーフィズムと呼ぶ）。

## 知識確認クイズ


---

### Q1. 通常のクラスとEnum（列挙型）の最大の違いは何か？

<details>
<summary> 正解と解説を見る</summary>

**正解：**
通常のクラスは `()` をつけて手動でインスタンス化（オブジェクト化）する必要があるが、Enumクラスは**定義された時点で、中に書かれた定数（メンバ）が自動的にそのクラスのオブジェクトとして実体化されている点**である。

</details>

---

### Q2. Pythonの `ABC` クラスに `@abstractmethod` をつけたメソッドを定義した。このクラスを継承した子クラスで、そのメソッドを書き忘れた（実装し忘れた）場合、どのタイミングでどうなるか？

<details>
<summary>正解と解説を見る</summary>

**正解：**
子クラスのオブジェクト（インスタンス）を生成しようとした瞬間に、Pythonが **`TypeError` を発生させてプログラムをストップさせる。** これにより、実装漏れのバグを実際に使う（実行する）前の段階で防ぐことができる。

</details>

---

### Q3. 「値が1つしかない定数」を定義する場合でも、Global定数（通常の変数）ではなくEnum型を使うべきなのはどのようなケースか？

<details>
<summary>正解と解説を見る</summary>

**正解：**
その値が、単なるシステムの設定値（例：最大リトライ回数など）ではなく、**将来的に選択肢（カテゴリ）が増える可能性のあるもの（例：通貨の種類や注文ステータスなど）であるケース**である。Enumにすることで、関連する定数をグループ化し、型安全（Type Safety）を保証できる。

</details>

## 所感

Enum自体の存在は知っていたが、自分で使えていなかったのでこの機会に使えるようにしたい。
