def passing_scores(scores):

    passed = []

    for index in range(len(scores)):

        if scores[index] >= 50:
            passed.append(scores[index])

    return passed

assert passing_scores([49, 50]) == [50]
assert passing_scores([20, 80, 30]) == [80]