import pandas
import sklearn.ensemble as ek
from sklearn.model_selection import train_test_split
from sklearn import tree, linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing
from sklearn import svm
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import sklearn.metrics

def train(db):
    featureSet = pandas.read_csv(db)
    featureSet.groupby(featureSet['malicious']).size()
    X = featureSet.drop(['URL','host','path','avg_path_token','malicious'], axis=1).values
    y = featureSet['malicious'].values

    model = {"DecisionTree": tree.DecisionTreeClassifier(max_depth=20),
             "RandomForest": ek.RandomForestClassifier(n_estimators=200),
             "Adaboost": ek.AdaBoostClassifier(n_estimators=50),
             "GradientBoosting": ek.GradientBoostingClassifier(n_estimators=50),
             "GNB": GaussianNB(),
             "LogisticRegression": LogisticRegression(),
             "SVC": SVC(gamma='auto')
             }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    results = {}
    for algo in model:
        clf = model[algo]
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print ("%s : %s " % (algo, score))
        results[algo] = score

    winner = max(results, key=results.get)
    print(winner)

    clf = model['SVC']
    res = clf.predict(X)
    mt = confusion_matrix(y, res)
    # mt[0][0] = tn, mt[0][1] = fp, mt[1][0] = fn, mt[1][1] = tp
    print("Recall rate : %f %%" % ((mt[1][1] / float(sum(mt[1]))) * 100))
    print('Precision rate : %f %%' % ((mt[0][0] / float(sum(mt[0])) * 100)))

    fout = open("prediction_res.txt", "w")
    for i in range(len(res)):
        fout.write(featureSet['URL'][i] + "," + str(res[i]) + "\n")
    fout.close()

    # print("False positive rate : %f %%" % ((mt[0][1] / float(sum(mt[0]))) * 100))
    # print('False negative rate : %f %%' % ((mt[1][0] / float(sum(mt[1])) * 100)))



