"""
CONTAINS THE FUNTIONS THAT THE WEBAPP CAN USE TO INTERACT WITH
THE LIBRARY
"""

import numpy as np
import torch
import torchvision
import torchvision.datasets as datasets

# # import agents and its functions
import autoaug.autoaugment_learners as aal
import autoaug.controller_networks as cont_n
import autoaug.child_networks as cn
from autoaug.main import create_toy

import pickle
from pprint import pprint
from .parse_ds_cn_arch import parse_ds_cn_arch
def parse_users_learner_spec(
            # things we need to feed into string parser
            ds, 
            ds_name, 
            IsLeNet, 
            network_name,
            # aalearner type
            auto_aug_learner, 
            # search space settings
            exclude_method, 
            num_policies, 
            num_sub_policies, 
            # child network settings
            toy_size, 
            batch_size, 
            early_stop_num, 
            iterations, 
            learning_rate, 
            max_epochs,
            ):
    train_dataset, test_dataset, child_archi = parse_ds_cn_arch(
                                                    ds, 
                                                    ds_name, 
                                                    IsLeNet,
                                                    network_name
                                                    )
    """
    The website receives user inputs on what they want the AaLearner
    to be. We take those hyperparameters and return an AaLearner

    """
    if auto_aug_learner == 'UCB learner':
        learner = aal.UcbLearner(
                        # parameters that define the search space
                        num_sub_policies=num_sub_policies,
                        exclude_method=exclude_method,
                        # hyperparameters for when training the child_network
                        batch_size=batch_size,
                        toy_size=toy_size,
                        learning_rate=learning_rate,
                        max_epochs=max_epochs,
                        early_stop_num=early_stop_num,
                        # UcbLearner specific hyperparameter
                        num_policies=num_policies
                        )
    elif auto_aug_learner == 'Evolutionary learner':
        learner = aal.EvoLearner(
                        # parameters that define the search space
                        num_sub_policies=num_sub_policies,
                        exclude_method=exclude_method,
                        # hyperparameters for when training the child_network
                        batch_size=batch_size,
                        toy_size=toy_size,
                        learning_rate=learning_rate,
                        max_epochs=max_epochs,
                        early_stop_num=early_stop_num,
                        )
    elif auto_aug_learner == 'Random Searcher':
        learner = aal.RsLearner(
                        # parameters that define the search space
                        num_sub_policies=num_sub_policies,
                        exclude_method=exclude_method,
                        # hyperparameters for when training the child_network
                        batch_size=batch_size,
                        toy_size=toy_size,
                        learning_rate=learning_rate,
                        max_epochs=max_epochs,
                        early_stop_num=early_stop_num,
                        )
    elif auto_aug_learner == 'GRU Learner':
        learner = aal.GruLearner(
                        # parameters that define the search space
                        num_sub_policies=num_sub_policies,
                        exclude_method=exclude_method,
                        # hyperparameters for when training the child_network
                        batch_size=batch_size,
                        toy_size=toy_size,
                        learning_rate=learning_rate,
                        max_epochs=max_epochs,
                        early_stop_num=early_stop_num,
                        )
    elif auto_aug_learner == 'Genetic Learner':
        learner = aal.GenLearner(
                        # parameters that define the search space
                        num_sub_policies=num_sub_policies,
                        exclude_method=exclude_method,
                        # hyperparameters for when training the child_network
                        batch_size=batch_size,
                        toy_size=toy_size,
                        learning_rate=learning_rate,
                        max_epochs=max_epochs,
                        early_stop_num=early_stop_num,
                        )

    return train_dataset, test_dataset, child_archi, learner