#!/usr/bin/python

from audio.audio_mood import AudioMood

from sklearn import tree


def run_analysis(audio_files):

    training_data = []
    class_labels = []

    test_cases = {}

    for mood_category, data in audio_files.iteritems():
            class_labels.extend([ mood_category ] * len(data))

            mood = AudioMood(mood_category, data)
            mood_dataset = mood.generate_dataset()
            test_cases[mood] = mood_dataset.pop()
            training_data.append(mood_dataset)

    clf = tree.DecisionTreeClassifier()
    clf.fit(training_data, class_labels)

    print "Finished training learning tree"
    for mood, data in test_cases:
        prediction = clf.predict_proba(data)
        print "Mood: {0}, prediction: {1}".format(mood, prediction)



