import sys
sys.path.append('../') # To import all python files in `source_code` folder.
from mfcc_gmm_func import * # To import functions that you need

import glob
audio_file_path_list = glob.glob('../../datasets/NNDH/*.wav')

model_path = 'NNDH.gmm'

generate_GMM(audio_file_path_list, model_path)

audio_file_path = 'datasets/NNDH/NNDH_1.wav'

for filename in audio_file_path_list:
    print(try_personal_GMM(filename, model_path))
