import pandas as pd
import matplotlib.pyplot as plt


def main():

    df = pd.read_csv("Some.csv")

    # print(df.head())
    # print(df.stack())

    # print(df.pivot(index='Name', columns='English', values='Math'))
    print(df.pivot_table(index='Name', columns='English'))


    # print(df.corr())
    #
    # df.plot()
    # # plt.show()
    # plt.savefig("Some.png")



    # print(df.head())
    # print(df.tail())
    # df.to_csv("Some2.csv")

    # print(df.shape)
    # print(df.columns)
    # print(df.dtypes)
    # print(df.describe())

    # print(df.iloc[0:2])
    # print(df.loc[:,['Name', 'English']])
    # print(df[df['English'] > 80])
    # print(df.query('English > 80'))

    # grouped = df.groupby("English")
    # print(df.mean())
    # print(grouped.mean())


    return


if __name__ == "__main__":

    main()