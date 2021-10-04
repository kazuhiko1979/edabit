"""
あなたのチームは、開発したソフトウェアのすべての Q&A チェックに合格し、リリースの準備が整いました。
支払いシステムを追加したので、顧客の請求書の発行システムを開発する必要があります。
"""

"""
# 状態
String invoiceNumber // 請求書番号。"UC-"の後に10桁の数字が続くとします。
String invoiceDate // 請求書が作成された日付
String company // 会社名
String companyAddress // 会社の住所
String billToName // 請求書先の名前
String billToAddress //　請求書先の住所
InvoiceItemNode invoiceItemHeadNode // 購入したアイテムのリストを開始を表すInvoiceItemNode
抽象オブジェクトで学習したnodeを参照
"""

"""
// 挙動
double amountDue(bool taxes) // 請求書の支払総額を計算します。
InvoiceItemHeadNodeから始まるすべてのリスト項目を反復処理し、数量も考慮して計算する必要があります。
Tax inputがtrueに設定されている場合は、合計金額に10%を加算してください。

void printBuyingItems // 請求書の全項目と数量を出力します。item: shampoo, price: 10, quantity:7
のようにそれぞれのアイテムを出力してください。

void printInvoice // 請求書の全内容を出力します。以下のように出力してください。

/*
Invoice
No. : UC1235467890
INVOICE DATE : 2020/06/05
SHIP TO : Recursion
ADDRESS : Los Angles
BILL TO : Steven
ADDRESS : Dallas
shampoo($10)--- 7 pcs. --- AMOUNT: 70
conditioner($5)--- 9 pcs. --- AMOUNT: 45
tooth brush($3)--- 10 pcs. --- AMOUNT: 30
SUBTOTAL : 145
TAX : 14.5
TOTAL : 159.5
*/
"""

"""
InvoiceItemNodeの設計図
// 状態
int quantity // 購入する製品の数を表す
Product product // 購入される製品に関するすべての情報を含むオブジェクト
InvoiceItemNodenext // このノードのInvoiceItemNode
"""

"""
// 挙動
double getTotalPrice // 購入する数量に基づいて、製品の合計価格を計算します。
"""

"""
製品(Product)の設計図
String title // 製品のタイトル
double price // 製品の価格(ドル）
"""


class Invoice:
    def __init__(self, invoiceNumber, invoiceDate, company,
                 companyAddress, billToName, billToAdress,
                 invoiceItemHeadNode):

        self.invoiceNumber = invoiceNumber
        self.invoiceDate = invoiceDate
        self.company = company
        self.companyAddress = companyAddress
        self.billToName = billToName
        self.billToAddress = billToAdress
        self.invoiceItemHeadNode = invoiceItemHeadNode


    def amountDue(self, taxes):
        currentNode = self.invoiceItemHeadNode
        total = 0

        while currentNode is not None:
            total += currentNode.product.price * currentNode.quantity
            currentNode = currentNode.next

        return total * 1.1 if taxes else total


    def printBuyingItems(self):
        print("Printing the Item List...")
        currentNode = self.invoiceItemHeadNode
        while currentNode is not None:
            print("item :" + currentNode.product.title
                  + ", price :" + str(currentNode.product.price)
                  + ", quantity :" + str(currentNode.quantity))
            currentNode = currentNode.next

    def printInvoice(self):
        print("Invoce\n" +
              "No. : " + self.invoiceNumber + "\n" +
              "INVOICE DATE : " + self.invoiceDate +  "\n" +
              "SHIP TO : " + self.company + "\n" +
              "ADDRESS : " + self.companyAddress + "\n" +
              "BILL TO : " + self.billToName + "\n" +
              "ADDRESS : " + self.billToAddress + "\n"
              )

        currentNode = self.invoiceItemHeadNode
        while currentNode is not None:
            print(currentNode.product.title +
                  "($" + str(currentNode.product.price) +
                  ")" + "--- " + str(currentNode.quantity) +
                  " pcs. " +
                  "--- AMOUNT: " + str(currentNode.product.price * currentNode.quantity))

            currentNode = currentNode.next

        print("SUBTOTAL : " + str(self.amountDue(False)) + "\n" +
              "TAX : " + str(self.amountDue(True) - self.amountDue(False))
        + "\n" + "TOTAL : " + str(self.amountDue(True))
              )


class InvoiceItemNode:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.next = None


class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price


product1 = Product("shampoo", 10)
product2 = Product("conditioner", 5)
product3 = Product("tooth brush", 3)

firstItem = InvoiceItemNode(product1, 7)
secondItem = InvoiceItemNode(product2, 9)
firstItem.next = secondItem
thirdItem = InvoiceItemNode(product3, 10)
secondItem.next = thirdItem

invoice = Invoice("UC1234567890", "2020/05/06", "Recursion",
                "Los Angels", "Steven", "Dallas", firstItem)

invoice.printBuyingItems()
invoice.printInvoice()

print(invoice.amountDue(False))
print(invoice.amountDue(True))




