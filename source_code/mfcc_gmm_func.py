from scipy.io import wavfile # File .wav handler
from python_speech_features import mfcc # Feature exatraction
from python_speech_features import delta # Increase feature exatraction
from sklearn import preprocessing # Normalization for numerical data
import numpy as np # Data handler
from sklearn.mixture import GMM # Get Gaussian Mixture model
import pickle # To save Python objects as binary files and handle them
import warnings # To ignore warnings of sklearn.mixture.GMM
warnings.filterwarnings("ignore")

# To read an audio file then return normalized mfcc feature
def get_mfcc_feat(audio_file_path):
    rate, audio = wavfile.read(audio_file_path)
    mfcc_feature = mfcc(audio, rate, winlen = 0.05, winstep = 0.05, numcep = 5, nfilt = 30, nfft = 512, appendEnergy = True)
    mfcc_feature = preprocessing.scale(mfcc_feature)
    deltas = delta(mfcc_feature, 2)
    double_deltas = delta(deltas, 2)
    return np.hstack((mfcc_feature, deltas, double_deltas))

# To get_mfcc_feat() of many audio files of one person
# then return normalized mfcc feature of that person
def get_mfcc_feat_person(audio_file_path_list):
    mfcc_feat_person = np.asarray(())
    for audio_file_path in audio_file_path_list:
        mfcc_feat = get_mfcc_feat(audio_file_path)
        if mfcc_feat_person.size == 0:
            mfcc_feat_person = mfcc_feat
        else:
            mfcc_feat_person = np.vstack((mfcc_feat_person, mfcc_feat))


    return mfcc_feat_person

# To generate a Gaussian Mixture model
def generate_GMM(audio_file_path_list, model_path):
    # audio_file_path_list : list of paths to a person's wav files
    # model_path : should be named after that person
    # Example: model_path = VDA.gmm
    mfcc_feat_person = get_mfcc_feat_person(audio_file_path_list)
    personal_GMM = GMM(n_components = 15, n_iter = 200, covariance_type='diag', n_init = 3)
    personal_GMM.fit(mfcc_feat_person)
    with open(model_path, 'wb') as GMM_file:
        pickle.dump(personal_GMM, GMM_file)

    return None

# To try personal_GMM with an audio file
# Return score of likelyhood person
# score = log(probability)
def try_personal_GMM(audio_file_path, model_path):
    # audio_file_path : a path to someone or your wav file
    # model path : path to your model
    # Example : VDA.gmm
    personal_GMM = pickle.load(open(model_path, 'rb'))
    likelyhood_score = np.array(personal_GMM.score(get_mfcc_feat(audio_file_path))).sum()
    return likelyhood_score
