from operator import index
import pandas as pd
import fitz

Index = pd.read_table('Index Course.CSV', header=None)

toc = []

for rows in range(270):
    if Index.iloc[rows,0].isdigit():
        toc.append([
                    1, 
                    Index.iloc[rows,0] + ' ' + Index.iloc[rows,1], 
                    int(Index.iloc[rows,2]) + 1
                    ])
    else:
        if len(Index.iloc[rows,0]) == 1:
            toc.append([
                        2, 
                        Index.iloc[rows,0] + ' ' + Index.iloc[rows,1], 
                        int(Index.iloc[rows,2]) + 1
                        ])
        else:
            if Index.iloc[rows,0] == 'ANSWERS' or Index.iloc[rows,0] == 'INDEX':
                toc.append([1, Index.iloc[rows,0], int(Index.iloc[rows,1]) + 1])
            else:
                toc.append([2, Index.iloc[rows,0], int(Index.iloc[rows,1]) + 1])

with fitz.open('raw Course.pdf') as pdf:
    pdf.set_toc(toc)
    pdf.saveIncr()