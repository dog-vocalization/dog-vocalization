#!/usr/bin/python

import glob
import os

from spectrum_analysis import Spectrum
from sklearn import tree


def analyze():
    training_data, class_labels = build_dataset()
    clf = tree.DecisionTreeClassifier()

    clf.fit(training_data, class_labels)

    with open(os.getcwd() + "/image_files/tree.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)


def build_dataset():
    dataset = []
    class_labels = []

    audacity_files = glob.glob(os.getcwd() + '/audio/audacity_files/*.txt')

    for file_name in audacity_files:
        with open(file_name, 'r') as file:
            data = file.readlines()[0].replace("\r", " ").replace("\t", " ").split()

            category = file_name.split("/")
            category = category[len(category) - 1].split("_")[0]

            spectrum = Spectrum(data, category)
            dataset.append(spectrum.training_data())
            class_labels.append(category)

    return dataset, class_labels

