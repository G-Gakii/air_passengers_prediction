
import numpy as np
import pandas as pd
# function to make data stationary
def make_data_stationary(df):
    # Make the time series stable
# log transform to stabilize variance
    df["log_passengers"]=np.log(df["total_passengers"])


    # differencing to remove trend and seasonality
    df["log_diff"]=df["log_passengers"].diff()
    df["log_diff_seasonal"]=df["log_diff"].diff(12)
    return  df

def reverse_stationary(pred,df):

    # undo seasonal differencing
    seasonal_undiff=pred+df["log_diff"].shift(12).loc[pred.index]
    #undo first order differencing
    previous_date =pred.index[0]-pd.DateOffset(months=1)
    previous_log_value=df.loc[previous_date,"log_passengers"]
    log_pred=seasonal_undiff.cumsum()+previous_log_value

    # undo log transform
    passenger_pred=np.exp(log_pred)

    return passenger_pred
