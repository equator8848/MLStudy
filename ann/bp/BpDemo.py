from ann.bp import DataSet
from ann.bp.NeuralNetwork import NeuralNetwork

if __name__ == '__main__':
    train_times = 20
    learn_step = 0.1
    layers = [784, 20, 40, 30, 10]
    network = NeuralNetwork(4, learn_step, layers)
    x_train, y_train = DataSet.load_data(True)
    print("训练环节...")
    for i in range(train_times):
        for j in range(len(x_train)):
            network.update(x_train[j], y_train[j])
    correct_num = 0
    print("测试环节...")
    x_test, y_test = DataSet.load_data(False)
    for i in range(len(y_test)):
        if network.test(x_test[i], y_test[i]):
            correct_num += 1
    print("正确率 %f%%" % (correct_num * 100 / len(y_test)))
