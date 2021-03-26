import yaml
import pprint

def main():

    with open('C\some.yaml', 'r') as f:
        data = yaml.load(f)
    #     # pprint.pprint(data)
    #
    # print(data["name"])

    with open("C\someB.yaml", 'w') as f:
        f.write(yaml.dump(data))


    return


if __name__ == '__main__':
    main()