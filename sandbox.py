#!/usr/bin/env python

from toy_datasets import *
from neural_network import *
from utils import *
from activation_functions import *
from itertools import chain
from optimization import *
import input_data


# generating test data
#X, Y = generate_2_class_moon_data()
#X2, Y2 = generate_2_class_moon_data()
#X, Y = generate_3_class_spiral_data(nb_classes=3, theta=0.5, plot=False)
#X2, Y2 = generate_3_class_spiral_data(nb_classes=3, theta=0.5, plot=False)
#X, y = load_iris_dataset()

# digit dataset
train, test = load_digit_dataset(1000, 0.1)
X = np.array([x[0] for x in train])
Y = [y[1] for y in train]
Y = np.asarray(Y)
X2 = np.array([x[0] for x in test])
Y2 = [y[1] for y in test]

#mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#d = mnist.train.next_batch(50)
#X = d[0]
#Y = d[1]

# testing library

#net = NeuralNetwork([2, 10, 2], hyperbolic_tangent)

'''
net = NeuralNetwork(input_dim=X.shape[1],
                    nb_classes=len(set(Y)),
                    hidden_dims=[10],
                    activation_function=hyperbolic_tangent)

net.mini_batch_sgd(training_data=X,
                   labels=Y,
                   epochs=1000,
                   batch_size=10,
                   epsilon=0.001,
                   lbda=0.001,
                   print_loss=True)
'''

#net.fit(X, Y, epochs=5000, epsilon=0.001, lbda=0.001, print_loss=True)
#t = net.evaluate(X2, Y2)
#print net.predict_old(X2)[1:10]
#print net.predict(X2)[1:10]
#print net.predict_old(X2)[1:10] == net.predict(X2)[1:10]
#plot_decision_boundary(lambda x: np.argmax(net.predict(x), axis=1),
#                       X, Y)

#dataset = load_data("../neural-networks-and-deep-learning/data/mnist.pkl.gz")

#X, Y = dataset[0]
#X2, Y2 = dataset[1]
#test_set_x, test_set_y = dataset[2]

tsv1 = "../marginAlign/cPecan/tests/test_alignments/conditional_model/C/tempFiles_alignment/makeson_PC_MA_286_R7.3_ZYMO_C_1_09_11_15_1714_1_ch24_file76_strand.vl.forward.tsv"
tsv2 = "../marginAlign/cPecan/tests/test_alignments/conditional_model/C/tempFiles_alignment/makeson_PC_MA_286_R7.3_ZYMO_C_1_09_11_15_1714_1_ch34_file182_strand.vl.forward.tsv"
tsv3 = "../marginAlign/cPecan/tests/test_alignments/echelon/C/tempFiles_alignment/makeson_PC_MA_286_R7.3_ZYMO_C_1_09_11_15_1714_1_ch4_file149_strand.e.forward.tsv"

alns = "../marginAlign/cPecan/tests/temp/tempFiles_alignment/"
#alns = "../marginAlign/cPecan/tests/test_alignments/echelon/C/tempFiles_alignment/"

#a = cull_motif_features_with_noise(747, tsv, True)
#s = cull_motif_features(354, tsv1, True)
#s2 = cull_motif_features(354, tsv2, True)
#d = cull_all_motif_features(354, tsv3, True)
#print d

#e = sorted(d['354'], key=lambda x: x[1], reverse=True)[:5]
#print e
#e = list(chain(*e))
#print e

#n = np.zeros([10, (5*12)])
#print n
#for _ in xrange(len(e)):
#    n[0, _] = e[_]
#print n

tr, trlb, ts, tslb = collect_deep_data_vectors(alns, True, 0, 0.5, 747, 100)
print tr.shape,
ptr, pts = preprocess_data(tr, ts, "normalize")
print ptr.shape









