"""
現在の項目を表す「ノード」を作成してみましょう（ノードに関しては上級コースで詳しく学習します）。
このノードには、ToDo リストの文字列と、リストの次の項目を表す nextNode が格納されています。
リストの項目としてのノードどうしを互いに結び付けることで、リストに存在する項目をすべて出力することができます。
"""

class StringNode:
    def __init__(self, stringValue):
        # このノードは、ノードと次のノードの値の2つのインスタンス変数を持ちます
        self.value = stringValue
        self.next = None


class TodoList:
    def __init__(self):
        # Todoリストの中には1つのインスタンス変数しかありません。
        self.head = None

    # 各項目を出力します。先頭から始まり、次の項目がなくまるまで、次の項目へと進んで行きます。
    def printList(self):
        print("Printing the Todo List...")
        currentNode = self.head
        while currentNode is not None:
            # 現在のノードを値を出力します。
            print(currentNode.value)
            # 現在のノードを次のノードに変更します。
            currentNode = currentNode.next

# リストを始めます。先頭は空です。
toDoList = TodoList()

# リストの中の最初の項目に先頭を設定します。
firstItem = StringNode("Fix the alarm clock.")
toDoList.head = firstItem

# 残りの項目にも同じ処理を行います。次の項目を割り当てることによって、項目同士をつなぎます。
secondItem = StringNode("Pickup grandmother from the dentist.")
firstItem.next = secondItem

thirdItem = StringNode("Call the handyman to fix the home appliance.")
secondItem.next = thirdItem

forthItem = StringNode("Go to the park to jog.")
thirdItem.next = forthItem

# リストを読み込みます
# toDoList.printList()

"""
オブジェクトはユーザーによって定義されるものなので、思いつきや抽象的コンセプトであっても自由自在に作成することができます。
製品オブジェクト、課税オブジェクトをそれぞれ作成し、それらを組み合わせてプロダクトの最終価格を計算するプログラムを作成してください。
DownloadableProduct には、ダウンロードされるプロダクトに関する情報が含まれます。
このプロダクトの挙動の 1 つは価格の計算で、tax オブジェクトを取り込みます。
tax オブジェクトには税金に関する情報が含まれ、これは DownloadableProduct の最終的な価格に影響します。

プロダクト - 状態
String title // ダウンロード可能な製品のタイトル
String description // ダウンロード可能な製品の説明
double price // ダウンロード可能な製品の価格
double sizeMb // ダウンロード可能な製品のサイズ(Mb)
String extension // ダウンロード可能な製品の拡張子

プロダクト - 挙動
double DownloadableProduct.getFinalPrice(Tax taxObject) // 税率によって計算された後の
プロダクトの最終的な価格を返します。
"""

"""
Tax - 状態
String name // 税金の名前
Double federalTax // 連邦税率
Double stateTax // 州税率
Double localTax // 地方税率
"""

class DownloadableProduct:
    def __init__(self, title, description, price, sizeMb, extension):
        self.title = title
        self.description = description
        self.price = price
        self.sizeMb = sizeMb
        self.extension = extension

    def getFinalPrice(self, taxObject):
        # 連邦税、州税、地方税をプロダクトに適用します。
        return self.price + (self.price * taxObject.federalTax) \
               + (self.price * taxObject.stateTax) + (self.price * taxObject.localTax)

    class Tax:
        def __init__(self, name, federalTax, stateTax, localTax):
            self.name = name
            self.federalTax = federalTax
            self.stateTax = stateTax
            self.localTax = localTax

    product1 = DownloadableProduct("A hero returns - Remastered",
                                   "A movie about a hero who saves the world.",
                                   23.5, 13000, "mp4")

    taxLasVegas = Tax("Las Vegas Taxes", 0.02, 0.05, 0.01)

    print(product1.title + "'s price is: " + str(product1.price))
    print(product1.title + "'s final price for " +
          taxLasVegas.name + " is: " +
          str(product1.getFinalPrice(taxLasVegas)))


