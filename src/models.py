import pickle
from pathlib import Path

import numpy as np
import torch
from sklearn.neural_network import MLPClassifier

from src.dataset import label2id, preprocess_waveform
from src.feature_extractor import wav2vec2


def fit_model(feature_vectors, labels):
    mlp = MLPClassifier(
        hidden_layer_sizes=(
            86,
            86,
            40,
            20,
            10,
        ),
        solver="sgd",
        verbose=10,
        tol=1e-5,
        random_state=1,
        learning_rate_init=1e-2,
        max_iter=1000,
    )

    mlp.fit(feature_vectors, labels)
    return mlp


def predict_score(model, waveform, actual_label):
    # processed_waveform = preprocess_waveform(waveform)
    feature_vector = wav2vec2(torch.from_numpy(waveform))[:86]
    proba = model.predict_proba(np.expand_dims(feature_vector, 0))
    score = proba[:, label2id(actual_label)]

    return renormalize(score, (0, 1), (1, 5))


def save_model(model):
    with open(Path(__file__).parent / "model.pkl", "wb") as f:
        pickle.dump(model, f)


def load_model():
    with open(Path(__file__).parent / "model.pkl", "rb") as f:
        model = pickle.load(f)
    return model


def renormalize(n, range1, range2):
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    return (delta2 * (n - range1[0]) / delta1) + range2[0]
