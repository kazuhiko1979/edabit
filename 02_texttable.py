from texttable import Texttable

def main():

    table = Texttable()

    # # アライメント:
    # table.set_cols_align(["l", "r", "c"])
    # table.set_cols_valign(["t", "m", "b"])

    table.set_deco(Texttable.HEADER)
    # table.set_deco(Texttable.BORDER)
    # table.set_deco(Texttable.HLINES)
    # table.set_deco(Texttable.VLINES)

    # table.set_deco(Texttable.HEADER|Texttable.VLINES)

    # table.add_rows([
    # ["Name", "Age", "NickName"],
    # ["Mr\nXavier\nHuon", 32, "Xav'"],
    # ["Mr\nBaatiste\nClement", 1, "Baby'"],
    # ["Mme\nLouise\nBourgeau", 28, "Lou\n\nLoue'"]
    # ])
    #
    # print(table.draw() + "\n")

    table.set_cols_dtype(
        ['t', # text
         'f', # float (decimal)
         'e', # float (exponent)
         'i', # integer
         'a']
    )

    table.set_cols_align(["l", "r", "r", "r", "l"])
    table.add_rows([
        ["text", "float", "exp", "int", "auto"],
        ["abcd", "67", 564, 89, 128.001],
        ["efghijk", 64.5431, .654, 89.6, 128000.00023],
        ["lmn", 5e-78, 5e-78, 89.4, .00000000000000128],
        ["opqrstu", .023, 5e+78, 92, 128000000000]
    ])

    print(table.draw())

    return



if __name__ == '__main__':
    main()