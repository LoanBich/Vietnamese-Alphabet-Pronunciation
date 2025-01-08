from pathlib import Path
from typing import Tuple

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


class VietAlphabetDataset(Dataset):
    def __init__(self):
        folder_dataset = Path(__file__).parents[1] / "dataset" / "processed"
        self._audio_files = sorted(folder_dataset.glob("*.wav"))

    def __getitem__(self, n: int) -> Tuple[Tensor, str]:
        file_audio = self._audio_files[n]
        label = file_audio.stem.split("_")[0]
        waveform, sample_rate = torchaudio.load(file_audio)

        assert sample_rate == 16000

        return torch.squeeze(waveform), label2id(label)

    def __len__(self) -> int:
        return len(self._audio_files)


def preprocess():
    raw_dataset = Path(__file__).parents[1] / "dataset" / "raw"
    processed_dataset = Path(__file__).parents[1] / "dataset" / "processed"

    for file_audio in raw_dataset.glob("*.wav"):
        waveform, sample_rate = torchaudio.load(file_audio)

        assert sample_rate == 16000

        trimmed_waveform, _ = trim(waveform.squeeze().numpy(), top_db=12)

        torchaudio.save(
            processed_dataset / file_audio.name,
            torch.unsqueeze(torch.from_numpy(trimmed_waveform), dim=0),
            sample_rate=sample_rate,
            encoding="PCM_S",
            bits_per_sample=16,
        )


if __name__ == "__main__":
    preprocess()
