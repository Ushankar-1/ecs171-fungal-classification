config = {
    "training": {
        "batch_size": 32,
        "epoch": 100
    },
    "models": {
        "n_class": 10,
        "n_length": 1024,
        "fix_length": True,
        "use_embedding": True,
        "vocab_size": 256,
        "dim": 64,
        "cnn_layer": 9,
        "cnn_hidden": 64,
        "cnn_ks": 3,
        "rnn_layer": 1,
        "rnn_hidden": 128
    }
}
