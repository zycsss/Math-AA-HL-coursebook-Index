import pandas as pd
import fitz

Index = pd.read_table('Index Answer.csv', header=None)

toc = []

for rows in range(27):
    toc.append(
        [1, Index.iloc[rows,0], int(Index.iloc[rows,1])]
    )

with fitz.open('raw Answer.pdf') as pdf:
    pdf.set_toc(toc)
    pdf.saveIncr()