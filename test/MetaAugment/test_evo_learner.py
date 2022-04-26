import MetaAugment.autoaugment_learners as aal
import MetaAugment.child_networks as cn
import torchvision
import torchvision.datasets as datasets
from pprint import pprint

def test_evo_learner():
    child_network_architecture = cn.SimpleNet
    train_dataset = datasets.FashionMNIST(root='./datasets/fashionmnist/train',
                            train=True, download=True, transform=None)
    test_dataset = datasets.FashionMNIST(root='./datasets/fashionmnist/test', 
                            train=False, download=True,
                            transform=torchvision.transforms.ToTensor())


    learner = aal.evo_learner(
        # parameters that define the search space
                sp_num=5,
                p_bins=11,
                m_bins=10,
                discrete_p_m=True,
                exclude_method=['ShearX'],
                # hyperparameters for when training the child_network
                batch_size=8,
                toy_size=0.0001,
                learning_rate=1e-1,
                max_epochs=float('inf'),
                early_stop_num=30,
                # evolutionary learner specific settings
                num_solutions=3,
                num_parents_mating=2,
    )

    # learn on the 3 policies we generated
    learner.learn(
        train_dataset=train_dataset,
        test_dataset=test_dataset,
        child_network_architecture=child_network_architecture,
        iterations=2
        )


if __name__=="__main__":
    test_evo_learner()
