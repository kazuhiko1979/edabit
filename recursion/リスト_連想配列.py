# 連想配列

"""
コンピュータが文字列などのキーをインデックスとして使用する場合、これは連想配列と呼ばれます。インデックスの位置を使うよりも、
文字列を使う方が私たち人間にとっては圧倒的にわかりやすいのです。

文字列は文字で構成されており、文字は ASCII や Unicode 等の仕様表上の数字によって
識別されます。以下のように文字列を数字に変換することができます。
"""

def simpleHash(inputString):
    numberRepresentation = 0
    for char in inputString:
        "ord(char)は、文字の整数値を返します"
        numberRepresentation += ord(char)
    return numberRepresentation

print(simpleHash("myawesomestring"))

"""
キーと値のペアのリストを作成し、そのキーを使ってデータを取得するコードを見てみましょう。
今回は、ペットを連想配列によって表現します。キーは格納されてるデータの情報を示し、値は任意のデータ型になります。

ペットを表現するための連想配列を利用します。Pythonでは連想配列は辞書データ型と呼ばれています。
連想配列を初期化するには、{} initialize構文を使用します。
キーと値のペアを内部に配置します。構文は次のようになります。："{key}":value。さらに多くの項目を配置する場合は、
カンマ,が必要です。
"""

myPet = {
    "name": "fluffy",
    "species": "Pomeranian",
    "furColor": "Brown",
    "born": "2018/05/06",
    "favoriteFood": "Carrot sticks"
}

# nameを取得します
print(myPet["name"])

# ペットのfavorite foodを取得します。
print(myPet["favoriteFood"])

# このmyPet辞書にさらに情報を追加します。
myPet["napTimes"] = "11:00am, 3:30pm, 9:00pm"
print(myPet["napTimes"])

# 例題1
# 以下の車種,値段のペアを連想配列によって作成してください。

myCar = {
    "Honda Civic": 24000,
    "Chevrolet Traverse": 30000,
    "Toyota Camry": 25000,
    "Subaru Outback": 27000,
    "Tesla X": 100000
}

print(myCar["Tesla X"])
print(myCar["Toyota Camry"])
myCar["BMW X3"] = 42000

# デスクトップコンピュータには以下の部品があります マザーボード、CPU、RAM、GPU、ストレージ、電源

desktopComputer = {
    "motherboard":"AGUX 203-4344 Extreme",
    "CPU": "Fantel l9 extreme 16 core 4.5Ghz",
    # 連想配列の配列
    "RAM":[
        {
            "title": "Zolik DDR6 MegaHyper 32gb",
            "sizeMb": 32000,
            "clockSpeedMHz": 3000
        },
        {
            "title": "Zolik DDR6 MegaHyper 32gb",
            "sizeMb": 32000,
            "clockSpeedMHz": 3000
        }
    ],
    "storage":[
        {
            "title": "Skygate ST3433 4TB HDD",
            "sizeGb": 4000,
        },
        {
            "title": "Skygate GT3433 1TB SSD",
            "sizeGb": 2000,
        },
    ],
    "GPU": "Livia jtx3400i ",
    "powerSupply": "Fursair Platinum 1200W PSU DirectY 12GB VRAM"
}

# 値を出力します。
print(desktopComputer["powerSupply"])
print(desktopComputer["storage"])
print(desktopComputer["GPU"])
print(desktopComputer["RAM"][0]["title"])








