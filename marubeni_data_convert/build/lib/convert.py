from tabula import read_pdf
from tkinter import messagebox

pdf_file = "変換元データ.pdf"

df = read_pdf(pdf_file,
                  pages='all',
                  guess=False,
                  area="entire",
                  lattice=True,
                  stream=False,
                  password=None
                  )

import pandas as pd

concat_list = []

for i in range(1, len(df)-1, 3):
  table = "table_" + str(i)
  table = df[i][3:]
  concat_list.append(table)

output = pd.concat(concat_list)
output.to_csv('output.csv')

messagebox.showinfo('実行ファイル', '変換ファイルの動作確認が完了しました！')