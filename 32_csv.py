import csv
import os
import pandas as pd


def main():

    df = pd.read_csv('C\Some.csv')

    # print(df)
    # print(df['Name'])
    # print(df['English'])
    # print(df.iloc[1])
    # print(df.iloc[0])

    df.to_csv('C\SomeB.csv')


    # print(os.getcwd())

    # with open('C\SomeA.csv', 'w') as f:
    #     writer = csv.writer(f, lineterminator='\n')
    #     writer.writerow(['Name', 'English', 'Math', 'History'])
    #     writer.writerow(['John', '87', '47', '98'])
    #     writer.writerow(['Mike', '67', '77', '95'])
    #     writer.writerow(['Paul', '76', '92', '37'])

        # reader = csv.reader(f)
        # header = next(reader)

        # for row in reader:
        #     print(row)

    return

if __name__ == '__main__':
    main()