#!/usr/bin/python

import glob
import os

import training_data
from sklearn import tree


# This function creates an instance of a decision tree classifier based on generated
# training data. It can be used to classify other data, and creates a dot file
# displaying a visual image of the decision tree used
def generate():
    training_data, class_labels = build_dataset()
    clf = tree.DecisionTreeClassifier()

    clf.fit(training_data, class_labels)

    # dot -Tpdf image_files/tree.dot -o image_files/tree.pdf
    with open(os.getcwd() + "/image_files/tree.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

    return clf


def build_dataset():
    dataset = []
    class_labels = []

    audacity_files = glob.glob(os.getcwd() + '/audio/audio_data/*.txt')

    for file_name in audacity_files:

        if "SKIP" in file_name:
            continue

        frequencies = []
        levels = []
        with open(file_name, 'r') as file:
            category = file.readline()
            class_labels.append(category)

            lines = file.readlines()
            for line in lines:
                line = line.split(",")

                frequencies.append(float(line[0]))
                levels.append(float(line[1]))

        data = training_data.generate(frequencies, levels, file_name)
        dataset.append(data)

    return dataset, class_labels

