# Workflow training model

Python 3

Requirements:
  - numpy==1.15.2
  - python-speech-features==0.5
  - scikit-learn==0.19.2
  - scipy==1.1.0
  - matplotlib==3.2.1

Or run this `pip install -r requirements.txt`

This workflow apply individually. In other word, you have to carry out by yourself.

All .wav files must be normalized and standardized.

## Create folder

Create a folder in `source_code` folder with your name such as `VDA` folder. This will be where you will train your own model. Also where you keep your own source code as a proof that you have done something.

## Carry out

Let assume you have script called `train_model.py` in your folder.

In `train_model.py`
```Python
import sys
sys.path.append('../') # To import all python files in `source_code` folder.
from mfcc_gmm_func import * # To import functions that you need
```
```Python
# Imagine you have a list of path to your wav files
# Something like this
audio_file_path_list = ['VDA_1.wav', 'VDA_2.wav', 'VDA_3.wav']
```
```Python
# Name your model after you
# Somthing like this
model_path = 'VDA.gmm'
```
```Python
# Run this function to generate, train, save model
generate_GMM(audio_file_path_list, model_path)
```
```Python
# Image you have a path to your wave file or someone file
audio_file_path = 'NNDH_1.wav'
# Run this function to try out your model
print(try_personal_GMM(audio_file_path, model_path))
```

## Note:

Remember to push your code to this repos.

Remember to update your model and wav files to Google Drive.
