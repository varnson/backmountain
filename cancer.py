import pandas as pds
from sklearn.preprocessing import LabelEncoder
from trainmodel import  grid_search_cv
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import time
import pickle
from sklearn.preprocessing import StandardScaler,MinMaxScaler,MaxAbsScaler
import xgboost as xgb

start=time.time()
print(start)

df=pds.read_csv("/home/fanzch/ml-wdbc.data", header=None)

X=df.loc[:,2:].values
Y=df.loc[:, 1].values

le=LabelEncoder()
Y=le.fit_transform(Y)

scaler = StandardScaler()
X=scaler.fit_transform(X)

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

params={
    "learning_rate": [0.08, 0.09],
    "gamma": [0.8, 0.9],
    "n_estimators": [300],
    "max_depth": [3, 4],
    "min_child_weight": [5],
    "subsample": [0.95, 1.0],
    "colsample_bytree": [0.7, 0.8],
    "reg_alpha": [0.6],
    "scale_pos_weight": [1.1,1.2],
    "n_jobs":[2]
    ,"tree_method":["gpu_hist"]
}
elf=grid_search_cv(x_train,y_train ,params, cv=10)

cv_result = pds.DataFrame.from_dict(elf.cv_results_)

with open('/home/fanzch/cv_result.csv','w') as f:
    cv_result.to_csv(f)

print('The parameters of the best model are: ')
print(elf.best_params_)



y_pred = elf.predict(x_test)
print(classification_report(y_true=y_test, y_pred=y_pred))


end=time.time()
print(end)
print('minutes='+str((end-start)/60))

estimator=xgb.XGBClassifier(predictor="cpu_predictor", **elf.best_params_)
estimator.fit(x_train,y_train)
print(estimator.feature_importances_)

y_pred = estimator.predict(x_test)
print(classification_report(y_true=y_test, y_pred=y_pred))

pickle.dump(estimator,open("model","wb"))

est2=pickle.load(open("model","rb"))
y_pred = est2.predict(x_test)
print(classification_report(y_true=y_test, y_pred=y_pred))