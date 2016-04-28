#!/usr/bin/python

import csv
import os

from sklearn import tree

from audio.legacy.audio_mood import AudioMood


def run_analysis(audio_files = None, file_name = ""):

    if audio_files is None and file_name is "":
        print "run_analysis requires at least one parameter. None given."
        return

    if audio_files is not None:
        training_data, class_labels = import_training_data(audio_files)
    else:
        training_data, class_labels = read_training_data(file_name)

    # training_data, class_labels, test_cases = generate_test_cases(training_data, class_labels)
    # test_cases = read_testing_data()

    if audio_files is not None:
        save_training_data(training_data, class_labels)

    clf = tree.DecisionTreeClassifier()
    clf.fit(training_data, class_labels)

    print "Finished training learning tree"
    print clf

    # correct = 0
    # incorrect = 0
    #
    # for index, data in test_cases.iteritems():
    #     mood = data[0]
    #     data = data[1]
    #     prediction = clf.predict_proba(data)
    #     prediction2 = clf.predict(data)
    #     print "Mood: {0}, prediction 1: {1}, prediction 2: {2}".format(mood, prediction, prediction2)
    #     if mood == prediction2[0]: correct += 1
    #     else: incorrect += 1
    #
    # print "Correct: {0}, incorrect: {1}".format(correct, incorrect)

    with open(os.getcwd() + "/image_files/tree.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

def generate_test_cases(training_data, class_labels):
    test_cases = {}

    test_case_indexes = {}

    for count, category in enumerate(class_labels):
        if category not in test_case_indexes.keys():
            test_cases[category] = training_data[count]
            test_case_indexes[category] = count

    training_data = delete(training_data, test_case_indexes.values(), axis = 0)
    class_labels = delete(class_labels, test_case_indexes.values(), axis=0)

    print "Test cases: {0}".format(test_cases)
    return training_data, class_labels, test_cases

def import_training_data(audio_files):
    training_data = []
    class_labels = []

    for mood_category, data in audio_files.iteritems():
        class_labels.extend([ mood_category ] * (len(data)))

        mood = AudioMood(mood_category, data)
        mood_dataset =mood.generate_dataset()#
        training_data.extend(mood_dataset)

    return training_data, class_labels

def read_training_data(file_name):
    training_data = []

    with open(os.getcwd() + file_name) as csvfile:
        reader = csv.reader(csvfile)
        csv_list = list(reader)

    class_labels = csv_list[0]
    for i in range(1, len(csv_list)):
        training_data.append(csv_list[i])

    return training_data, class_labels

# TODO clean me up
def read_testing_data(file_name = "/test_data.csv"):
    test_data = {}

    with open(os.getcwd() + file_name) as csvfile:
        reader = csv.reader(csvfile)
        csv_list = list(reader)

    class_labels = csv_list[0]
    for i in range(1, len(csv_list)):
        test_data[i - 1] = [ class_labels[i - 1], csv_list[i] ]

    print test_data
    return test_data


def save_training_data(training_data, class_labels):
    with open(os.getcwd() + "/training_data.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(class_labels)
        for index, song_data in enumerate(training_data):
            writer.writerow(song_data)
