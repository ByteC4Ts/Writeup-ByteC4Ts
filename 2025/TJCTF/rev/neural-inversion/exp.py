import numpy as np

# Use the provided model.npz to recover the hidden ASCII flag by algebraically inverting the network's layers.
data = np.load("model.npz")

print(data.files)  # ['W1', 'b1', 'W2', 'b2', 'y']

W1, b1, W2, b2, y = data["W1"], data["b1"], data["W2"], data["b2"], data["y"]

print(W1.shape, b1.shape, W2.shape, b2.shape, y.shape)  # (30, 30) (30,) (30, 30) (30,) (30,)

W1_inv = np.linalg.pinv(W1)
W2_inv = np.linalg.pinv(W2)


def rev_sigmoid(x):
    return np.log(x / (1 - x))


# t1 = W1@x + b1
# t2 = sigmoid(t1)
# t3 = W2@t2 + b2
# y = sigmoid(t3)


t3 = rev_sigmoid(y)
t2 = W2_inv @ (t3 - b2)
t1 = rev_sigmoid(t2)
x = W1_inv @ (t1 - b1)

print(x)

for i in x:
    n = int(i * 128)
    print(chr(n), end="")

# tjctf{m0d3l_1nv3rs10n_f9a93qw}
