import numpy as np
from sklearn import datasets


def split(X, Y, train_size):
    len_train = int(X.shape[0] * train_size)
    index = np.arange(X.shape[0])
    np.random.shuffle(index)
    X_train = X[index[:len_train]]
    X_test = X[index[len_train:]]
    Y_train = Y[index[:len_train]]
    Y_test = Y[index[len_train:]]
    return X_train, Y_train, X_test, Y_test


def get_data_and_class():
    iris = datasets.load_iris()
    data = iris['data']
    target = iris['target']
    result = split(data, target, 0.08)
    return result


def find_k_neighbors(X_train, sample, k):
    distances = np.array(np.sqrt(np.sum(((X_train - sample) ** 2), axis=1)))
    index_neighbors = np.argsort(distances)
    return index_neighbors[:k]


def voting_round(neighbors_types):
    incidence = np.bincount(neighbors_types)
    return np.where(incidence == incidence.max())[0]


def voting(neighbors_types):
    selected = voting_round(neighbors_types)
    while len(selected) > 1:
        neighbors_types = neighbors_types[:-1]
        selected = voting_round(neighbors_types)
    return selected[0]


def knn(data_training, type_training, data_testing, type_testing):
    k = 5
    matches = 0
    for i in range(len(data_testing)):
        index_neighbors = find_k_neighbors(data_training, data_testing[i], k)
        type_neighbors = type_training[index_neighbors]
        estimated_type_i = voting(type_neighbors)
        if estimated_type_i == type_testing[i]:
            matches += 1
            # data_training = np.append(data_training, data_testing[i])
            # type_training = np.append(type_training, type_testing[i])
    success_rate = matches / len(type_testing)
    return success_rate


data_training, type_training, data_testing, type_testing = get_data_and_class()

print(knn(data_training, type_training, data_testing, type_testing))
