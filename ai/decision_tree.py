import pydotplus
from sklearn import tree


class Dataset:
    def __init__(self, dataset, target_column, target_names):
        self.data = dataset.drop(target_column, axis=1)
        self.target = dataset[target_column]
        self.feature_names = self.data.columns.values
        self.target_names = target_names


def train_model(dataset):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(dataset.data, dataset.target)
    export_tree_to_png(clf, dataset)
    return clf


def export_tree_to_png(clf, dataset):
    dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=dataset.feature_names,
                                    class_names=dataset.target_names,
                                    filled=True, rounded=True)

    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png("out/dtree.png")
