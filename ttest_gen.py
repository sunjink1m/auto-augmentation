# We can initialize the train_dataset with its transform as None.
# Later on, we will change this object's transform attribute to the policy
# that we want to test
import torchvision.datasets as datasets
import torchvision

import autoaug.child_networks as cn
from autoaug.autoaugment_learners.AaLearner import AaLearner
from autoaug.autoaugment_learners.GenLearner import GenLearner

import random
import pickle
    
# train_dataset = datasets.MNIST(root='./datasets/mnist/train',
#                                 train=True, download=True, transform=None)
# test_dataset = datasets.MNIST(root='./datasets/mnist/test', 
#                         train=False, download=True, transform=torchvision.transforms.ToTensor())


# train_dataset = datasets.FashionMNIST(root='./datasets/fashionmnist/train',
#                         train=True, download=True, transform=None)
# test_dataset = datasets.FashionMNIST(root='./datasets/fashionmnist/test', 
#                         train=False, download=True,
#                         transform=torchvision.transforms.ToTensor())


train_dataset = datasets.CIFAR10(root='./datasets/cifar10/train',
                        train=True, download=True, transform=None)
test_dataset = datasets.CIFAR10(root='./datasets/cifar10/train',
                        train=False, download=True, 
                        transform=torchvision.transforms.ToTensor())

# child_network_architecture = cn.lenet
# child_network_architecture = cn.lenet()

# child_network_architecture = cn.EasyNet(
#                                     img_height=28,
#                                     img_width=28,
#                                     num_labels=10,
#                                     img_channels=1
#                                     )

child_network_architecture = cn.LeNet(
                                    img_height=32,
                                    img_width=32,
                                    num_labels=10,
                                    img_channels=3
                                    )

agent = GenLearner(
                            num_sub_policies=2,
                            toy_size=0.01,
                            batch_size=4,
                            learning_rate=0.05,
                            max_epochs=float('inf'),
                            early_stop_num=10,
                            num_offspring=50
                            )


agent.learn(train_dataset,
            test_dataset,
            child_network_architecture=child_network_architecture,
            iterations=100)

with open('genetic_logs.pkl', 'wb') as file:
                pickle.dump(agent.history, file)
print(sorted(agent.history, key = lambda x: x[1], reverse = True))

print("ACCURACIES IN TIME: ")

for iter, (pol, acc) in enumerate(agent.history):
    print("pol: ", pol)
    print("acc: ", acc)