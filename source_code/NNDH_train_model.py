import sys
from mfcc_gmm_func import * # To import functions that you need

audio_file_path_list = [f'datasets/NNDH_{i+1}.wav' for i in range(135)]

model_path = 'NNDH.gmm'

generate_GMM(audio_file_path_list, model_path)

audio_file_path = 'datasets/NNDH_1.wav'

for filename in audio_file_path_list:
    print(try_personal_GMM(filename, model_path))
