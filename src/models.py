import pickle
from pathlib import Path

import numpy as np
import torch
from sklearn.neural_network import MLPClassifier

from src.dataset import label2id, preprocess_waveform
from src.feature_extractor import wav2vec2


def fit_model(feature_vectors, labels):
    mlp = MLPClassifier(
        hidden_layer_sizes=(40,),
        alpha=1e-4,
        solver="adam",
        verbose=10,
        random_state=1,
        learning_rate_init=0.2,
    )

    mlp.fit(feature_vectors, labels)
    return mlp


def predict_score(model, waveform, actual_label):
    processed_waveform = preprocess_waveform(waveform)
    feature_vector = wav2vec2(torch.from_numpy(processed_waveform))[:86]
    proba = model.predict_proba(np.expand_dims(feature_vector, 0))
    score = proba[:, label2id(actual_label)]

    return score


def save_model(model):
    with open(Path(__file__).parent / "model.pkl", "wb") as f:
        pickle.dump(model, f)


def load_model():
    with open(Path(__file__).parent / "model.pkl", "rb") as f:
        model = pickle.load(f)
    return model
