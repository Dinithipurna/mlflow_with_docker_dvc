import os
import warnings
import sys
import argparse
import pandas as pd
import pickle


if __name__ == "__main__":
    data = pd.read_csv("test.csv")

    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path")
    args = parser.parse_args()

    model = pickle.load(open(args.model_path, "rb"))

    predicted_qualities = model.predict(data)

    print(predicted_qualities[0])