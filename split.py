from operator import index
import pandas as pd


batch_no = 1

fileName = input('Enter the file name' )
chunk_size = int(input('How many rows should be  in each file?'))
for chunk in pd.read_csv(fileName + '.csv', chunksize=chunk_size):
    chunk.to_csv('convertcsv' + str(batch_no) + '.csv' , index=False)
    batch_no +=1