import xml.etree.ElementTree as ET

def main():

    tree = ET.parse('C\Some.xml')
    # name = tree.find('country').attrib
    # name_list = tree.findall('country')
    # for name in name_list:
    #     print(name.attrib)

    years_list = tree.findall('country/year')
    for year in years_list:
        year.text = "2021"

    tree.write('C\SomeB.xml', 'utf-8', True)

    return


if __name__ == '__main__':
    main()