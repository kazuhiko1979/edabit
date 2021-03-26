import json
import pprint
import simplejson

def main():

    with open('C\Some.json', 'r') as f:
        j = simplejson.load(f)

    # print(j)
    # print(j['employee'])
    # pprint.pprint(j, width=50)

    with open('C\someB.json', 'w') as f:
        simplejson.dump(j, f, indent=4)


    return


if __name__ == '__main__':
    main()
