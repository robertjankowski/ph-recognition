import sys
import numpy as np
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")

red = float(sys.argv[1])
green = float(sys.argv[2])
blue = float(sys.argv[3])

MODEL_PATH = 'models\\{}.pkl'.format(sys.argv[4])

with open(MODEL_PATH, 'rb') as f:
    clf = joblib.load(f)
    predict_rgb = np.vstack([blue, green, red]).T
    ph_predict = clf.predict(predict_rgb)
    if "bin_clf" in MODEL_PATH:
        if ph_predict:
            print("Base")
        else:
            print("Acid")
    else:
        print("PH = {}".format(str(ph_predict).strip('[]')))
