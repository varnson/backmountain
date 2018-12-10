
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler,MinMaxScaler,MaxAbsScaler

from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn.base import clone

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV,cross_val_score

import xgboost as xgb


def train_model(input_X,input_y,params_dict=None,estimator=xgb.XGBClassifier()):
    input_X,input_y = shuffle(input_X,input_y)
    if params_dict is not None:
        estimator.set_params(**params_dict)

    clf = clone(estimator)
    clf.fit(input_X,input_y)
    return clf


def train_in_pipeline(input_X,input_y,params_dict=None,scoring='roc_auc',cv=5,estimator=xgb.XGBClassifier()):
    input_X,input_y = shuffle(input_X,input_y)
    if params_dict is not None:
        estimator.set_params(**params_dict)

    pl_clf = Pipeline([('variance', VarianceThreshold(threshold=10e-4)),
                        ('scaling', StandardScaler()),
                        ('clf', estimator)])
    scores = cross_val_score(pl_clf,input_X,input_y,scoring=scoring,cv=cv)
    return scores


def grid_search_cv(input_X,input_y,params,scoring='roc_auc',cv=5,estimator=xgb.XGBClassifier()):
    #k=estimator.get_params().keys()
    #pl_clf = Pipeline([('variance', VarianceThreshold(threshold=10e-4)),
    #                   ('scaling', StandardScaler()),
    #                   ('clf', estimator)])

    grid_estor = GridSearchCV(estimator,param_grid=params,scoring=scoring,cv=cv,return_train_score=True)
    grid_estor.fit(input_X,input_y)
    return grid_estor


