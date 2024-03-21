import talib
import pandas as pd
import numpy as np

def hammer(df):
    hammer = talib.CDLHAMMER(df['Open'],df['High'], df['Low'],df['Close'])

    # Find the indices of non-zero values
    non_zero_indices = np.where(hammer != 0)[0]

    # Print row numbers corresponding to non-zero values
    if non_zero_indices.size>0:
        df.loc[non_zero_indices, 'Pattern'] = 'HAMMER'
        return True
    else:
        return False
    
def inverted_hammer(df):
    inverted_hammer = talib.CDLINVERTEDHAMMER(df['Open'],df['High'], df['Low'],df['Close'])
    non_zero_indices = np.where(inverted_hammer != 0)[0]
    if non_zero_indices.size>0:
        df.loc[non_zero_indices, 'Pattern'] = 'INVERTED HAMMER'
        return True
    else:
        return False

def recognized_pattern(df):
    hammer(df)
    inverted_hammer(df)

    return df