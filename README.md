# Automatic speaker recognition

A repos for USTH Digital Signal Processing 2020 Group 3 project. It's quite obvious in the title.

[![Img](https://img.shields.io/badge/Python-3-green)](https://www.python.org/downloads/)

## Introduction

[What is speaker recognition](https://en.wikipedia.org/wiki/Speaker_recognition)

[What is digital signal processing](https://en.wikipedia.org/wiki/Digital_signal_processing)

This project harness the power of function [mfcc](https://github.com/jameslyons/python_speech_features/blob/9a2d76c6336d969d51ad3aa0d129b99297dcf55e/python_speech_features/base.py#L25) from `python_speech_features` and model [gmm](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture) from `sklearn`.

Read more about [Mel frequency cepstrum coefficients](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum) and [Gaussian Mixture model](https://en.wikipedia.org/wiki/Mixture_model#Gaussian_mixture_model).

## Datasets

This is the [datasets](https://drive.google.com/drive/folders/1kzTGzFeVPPxlAYj0nsVZlHpKJePSD0fy?usp=sharing). Remember to read AudioInfo.txt in `Sunday datasets` before processing.

135 .wav files of each person are 135 lines in `transcripts/random_sentences.txt`.

Note that `Friday datasets` is just an archive of `Sunday datasets`. Please use `Sunday datasets`.

## Approach

Each `Sunday_datasets/mix`, `Sunday_datasets/low`, `Sunday_datasets/high`, I take 100 out of 135 .wav files of each person then I fit these files into a model which will represent that person's unique voice features. The rest 35 .wav files of each person are used to test the system of models.

100 .wav files are be shuffled to show that order of files is not important.


Plan:
  - Train models with `Sunday_datasets/mix` folder.
  - Train models with `Sunday_datasets/low` folder.
  - Train models with `Sunday_datasets/high` folder.
  - Then test each system of models on `Sunday_datasets/mix`, `Sunday_datasets/low`, `Sunday_datasets/high` folders.

Read our [report](https://www.overleaf.com/read/pvgxhcmffyfc) for more details.

## Project structure
To have clear view of folders and files
```
+--venv/
|
+--transcripts/
|  +--usth.txt
|  +--random_sentences.txt
|
|--datasets/
|  +--mix/
|  |  +AudioInfo.txt
|  |
|  +--low/
|  |  +AudioInfo.txt
|  |
|  +--high/
|     +AudioInfo.txt
|  
|--source_code/
|  +--Friday_script_models/ # Ignorable
|  +--models/ # Where models are saved as binary files
|  +--mfcc_gmm_func.py # Script of functions to call mfcc and gmm
|  +--requirements.txt # pip install -r requirements.txt
|  +--train_models.py
|  +--try_models.py
|
+--LICENSE
+--README.md
+--.gitignore
```

## Group's member
- [Vu Dinh Anh](https://github.com/dinhanhx)
- [Ngo Ngoc Duc Huy](https://github.com/Huy-Ngo)
- [Nguyen Quoc Thong](https://github.com/NhacBatQuan)
- [Le Huy Quang](https://github.com/quangLH195)
- [Trinh Quoc Dat](https://github.com/TrinhQuocDat99du)
- [Luu Hai Nam](https://github.com/namluu25)
- [Tran Minh Hieu](https://github.com/pcranger)
- [Dinh Gia Luong](https://github.com/gialuong2801)
