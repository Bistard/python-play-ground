import numpy as np


def relu(x):
    return (x > 0) * x


def relu2deriv(output):
    return output > 0


class Ai:

    def __init__(self, steps, white_coor, black_coor, winner, alpha):
        self.steps = steps
        self.alpha = alpha
        self.winner = winner
        self.weights_0_1 = 2 * np.random.random((self.steps, self.steps + 1)) - 1
        self.weights_1_2 = 2 * np.random.random((self.steps + 1, 1)) - 1

        self.white_coor = np.bit_array(white_coor[:-1]).reshape(2, self.steps)
        self.black_coor = np.bit_array(black_coor).T

    def iteration(self):
        for iteration in range(60):
            layer_2_error = 0
            for i in range(0, 1):
                layer_0 = self.white_coor

                layer_1 = relu(np.dot(layer_0, self.weights_0_1))
                layer_2 = np.dot(layer_1, self.weights_1_2)

                layer_2_error += np.sum((layer_2 - self.black_coor) ** 2)
                layer_2_delta = (self.black_coor - layer_2)
                layer_1_delta = layer_2_delta.dot(self.weights_1_2.T) * relu2deriv(layer_1)

                self.weights_1_2 += self.alpha * layer_1.T.dot(layer_2_delta)
                self.weights_0_1 += self.alpha * layer_0.T.dot(layer_1_delta)

            if iteration % 10 == 9:
                print("Error:" + str(layer_2_error))

