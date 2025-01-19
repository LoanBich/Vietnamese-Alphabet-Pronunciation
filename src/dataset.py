from pathlib import Path
from typing import Tuple

import librosa
import numpy as np
import torch
import torchaudio
from librosa.effects import trim
from torch import Tensor
from torch.utils.data import Dataset


def label2id(label: str) -> int:
    return {
        "E": 0,
        "H": 1,
        "i": 2,
        "L": 3,
        "N": 4,
        "Ơ": 5,
        "U": 6,
        "V": 7,
    }[label]


def id2label(id: int) -> str:
    return {
        0: "E",
        1: "H",
        2: "i",
        3: "L",
        4: "N",
        5: "Ơ",
        6: "U",
        7: "V",
    }[id]


class VietAlphabetRawDataset(Dataset):
    def __init__(self):
        folder_dataset = Path(__file__).parents[1] / "dataset" / "raw"
        self._audio_files = sorted(folder_dataset.glob("*.wav"))

    def __getitem__(self, n: int) -> Tuple[Tensor, str]:
        file_audio = self._audio_files[n]
        label = file_audio.stem.split("_")[0]
        waveform, sample_rate = torchaudio.load(file_audio)

        assert sample_rate == 16000

        return torch.squeeze(waveform), label2id(label)

    def __len__(self) -> int:
        return len(self._audio_files)


def load_processed_dataset():
    processed_dataset = (
        Path(__file__).parents[1] / "dataset" / "processed" / "processed.npz"
    )
    dataset = np.load(processed_dataset)
    return dataset["waveforms"], dataset["list_label_str"], dataset["list_label_id"]


def preprocess_dataset():
    raw_dataset = Path(__file__).parents[1] / "dataset" / "raw"
    processed_dataset = Path(__file__).parents[1] / "dataset" / "processed"

    waveforms, list_label_str, list_label_id = [], [], []

    for file_audio in raw_dataset.glob("*.wav"):
        waveform, sample_rate = librosa.load(file_audio, sr=None)
        label_str = file_audio.stem.split("_")[0]

        assert sample_rate == 16000

        processed_waveform = preprocess_waveform(waveform)

        waveforms.append(processed_waveform)
        list_label_str.append(label_str)
        list_label_id.append(label2id(label_str))

    np.savez(
        processed_dataset / "processed.npz",
        waveforms=np.asarray(waveforms),
        list_label_str=np.asarray(list_label_str),
        list_label_id=np.asarray(list_label_id),
    )


def preprocess_waveform(waveform):
    sample_rate = 16000

    trimmed_waveform, _ = trim(waveform.squeeze(), top_db=12)

    one_second_waveform = trimmed_waveform[:sample_rate]
    one_second_waveform = np.pad(
        one_second_waveform,
        (0, sample_rate - one_second_waveform.shape[0]),
    )

    return one_second_waveform


if __name__ == "__main__":
    preprocess_dataset()
