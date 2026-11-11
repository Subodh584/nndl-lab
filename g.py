import urllib.request as _u
_B = "https://raw.githubusercontent.com/Subodh584/nndl-lab/main/"
_F = {8: "Exp08_LeNet_Image_Classification", 9: "Exp09_ResNet_Object_Detection", 10: "Exp10_Transfer_Learning_VGG16",
      11: "Exp11_Char_RNN_Language_Model", 12: "Exp12_LSTM_Named_Entity_Recognition",
      13: "Exp13_Neural_Machine_Translation_Attention", 14: "Exp14_Scene_Understanding_RBM", 15: "Exp15_GAN_Image_Generation"}
def get(n):
    f = _F[n] + ".ipynb"; _u.urlretrieve(_B + f, f); print("downloaded", f)
