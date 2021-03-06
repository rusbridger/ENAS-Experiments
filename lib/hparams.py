from torchvision.datasets import CIFAR10

args = {
    # basic hyperparameters
    "description": "ENAS",
    "search_for": "macro",

    # dataset
    "dataset": CIFAR10,
    "n_classes": 10,
    "n_train": 45000,
    "n_val": 5000,

    # training parameters
    "data_path": "export/data/",
    "output_filename": "",
    "resume": "",
    "batch_size": 128,
    "num_epochs": 300,
    "eval_every_epochs": 1,
    "seed": 69,
    "cutout": 0,
    "fixed_arc": False,
    "log_every": 50,
    "plots": False,

    # child hyperparameters
    "child_num_layers": 12,
    "child_out_filters": 36,
    "child_grad_bound": 5.0,
    "child_l2_reg": 0.00025,
    "child_keep_prob": 0.9,
    "child_lr_max": 0.05,
    "child_lr_min": 0.0005,
    "child_lr_T": 10,

    # controller hyperparameters
    "controller_lstm_size": 64,
    "controller_lstm_num_layers": 1,
    "controller_entropy_weight": 0.0001,
    "controller_train_every": 1,
    "controller_num_aggregate": 20,
    "controller_train_steps": 50,
    "controller_lr": 0.001,
    "controller_tanh_constant": 1.5,
    "controller_op_tanh_reduce": 2.5,
    "controller_skip_target": 0.4,
    "controller_skip_weight": 0.8,
    "controller_bl_dec": 0.99,

    # search space
    "set": "baseline",
    "experiment": "space_0",
}
