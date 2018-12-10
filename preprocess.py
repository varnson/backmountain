from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler,MinMaxScaler,MaxAbsScaler




def check_variance(input_X,threshold=10e-4):
    variance = VarianceThreshold(threshold=threshold)
    out_X = variance.fit_transform(input_X)
    return variance,out_X


def feature_scaling(input_X,method='std'):
    if method=='std':
        scaler = StandardScaler()
    elif method == 'maxabs':
        scaler = MaxAbsScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise Exception('param error:{}'.format(method))
    out_X = scaler.fit_transform(input_X)
    return scaler,out_X


