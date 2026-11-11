# Usage: python get.py exp8   (or: python get.py 8 | python get.py all)
import sys, urllib.request
BASE = "https://raw.githubusercontent.com/Subodh584/nndl-lab/main/"
F = {8: "Exp08_LeNet_Image_Classification.ipynb", 9: "Exp09_ResNet_Object_Detection.ipynb",
     10: "Exp10_Transfer_Learning_VGG16.ipynb", 11: "Exp11_Char_RNN_Language_Model.ipynb",
     12: "Exp12_LSTM_Named_Entity_Recognition.ipynb", 13: "Exp13_Neural_Machine_Translation_Attention.ipynb",
     14: "Exp14_Scene_Understanding_RBM.ipynb", 15: "Exp15_GAN_Image_Generation.ipynb"}
a = (sys.argv[1] if len(sys.argv) > 1 else "").lower().replace("exp", "")
keys = list(F) if a == "all" else [int(a)] if a.isdigit() and int(a) in F else []
if not keys: sys.exit("usage: python get.py exp8..exp15 | all")
for k in keys:
    urllib.request.urlretrieve(BASE + F[k], F[k]); print("downloaded", F[k])
