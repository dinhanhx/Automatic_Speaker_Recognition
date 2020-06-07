# Source code

## Setup
```
pip install -r requirements.txt
```

## Note

## Train the models

Make sure you follow the project's structure in README.md at root.

In `train_models.py`, alter lines 4, 5, 6

```Python
names = ['VDA', 'NNDH', 'NQT', 'LHQ', 'TQD', 'LHN', 'TMH', 'DGL'] # name of people
model_type = 'high' # train on 'datasets/high/' folder
test_type = 'high' # test on 'datasets/high/' folder
```

## Try the models

In `try_models.py`, alter lines 5, 6

```Python
audio_file_path = '' # Path to .wav you want try
model_type = '' # Model type you want to try
```
