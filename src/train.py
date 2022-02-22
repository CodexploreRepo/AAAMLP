from ast import arg
import joblib
import os 
import config
import argparse

import pandas as pd
from sklearn import metrics, tree


def run(fold):
    #read the training data with folds
    df = pd.read_csv(config.TRAINING_FILE)
    
    df_train = df[df.kfold != fold].reset_index(drop = True)
    df_valid = df[df.kfold == fold].reset_index(drop = True)
    
    x_train = df_train.drop("quality", axis = 1).values
    y_train = df_train["quality"].values
    
    x_valid = df_valid.drop("quality", axis = 1).values
    y_valid = df_valid["quality"].values
    
    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    
    preds = clf.predict(x_valid)
    accuracy = metrics.accuracy_score(y_valid, preds)
    print(f"Fold={fold}, Accuracy={accuracy}")
    
    #Save model
    joblib.dump(clf, 
                os.path.join(config.MODEL_OUTPUT, f"dt_{fold}.bin")
            )
    
if __name__ == "__main__":
    # initialize Argument Parser Class
    parser = argparse.ArgumentParser()
    #Add (arg, type)
    parser.add_argument(
        "--fold",
        type=int
    )
    #read the arguments from the command line
    args = parser.parse_args()
    run(fold=args.fold)
  