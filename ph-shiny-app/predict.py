import sys
import numpy as np
from sklearn.externals import joblib

red = sys.argv[1]
green = sys.argv[2]
blue = sys.argv[3]

MODEL_NAME = "models\\gbr-95%.pkl"

with open(MODEL_NAME, 'rb') as f:
    clf = joblib.load(f)
    predict_rgb = np.vstack([blue, green, red]).T
    ph_predict = clf.predict(predict_rgb)
    print(f"PH = {str(ph_predict).strip('[]')}")
