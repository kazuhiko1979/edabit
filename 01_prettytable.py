from prettytable import prettytable
from prettytable import from_html_one


def main():

    # table = PrettyTable(
    #     ['Serial Number', 'Product Name', 'Lot'])
    #
    # table.add_row(['P1214', 'Pencil', '100'])
    # table.add_row(['E9545', 'Eraser', '150'])
    # table.add_row(['N7811', 'Notebook', '200'])
    #

    with open('data.csv', 'r') as file:
        table = prettytable.from_csv(file)

        print(table)


    table.sortby      = 'Lot'
    table.reversesort = True

    # print(table)
    return


if __name__ == '__main__':
    main()

