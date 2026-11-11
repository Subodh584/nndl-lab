#!/bin/bash
# Usage: bash get.sh exp8      (or: bash get.sh 8 | bash get.sh all)
BASE="https://raw.githubusercontent.com/Subodh584/nndl-lab/main"
declare -A F=(
 [8]=Exp08_LeNet_Image_Classification.ipynb
 [9]=Exp09_ResNet_Object_Detection.ipynb
 [10]=Exp10_Transfer_Learning_VGG16.ipynb
 [11]=Exp11_Char_RNN_Language_Model.ipynb
 [12]=Exp12_LSTM_Named_Entity_Recognition.ipynb
 [13]=Exp13_Neural_Machine_Translation_Attention.ipynb
 [14]=Exp14_Scene_Understanding_RBM.ipynb
 [15]=Exp15_GAN_Image_Generation.ipynb )
get() { curl -fsSL "$BASE/${F[$1]}" -o "${F[$1]}" && echo "downloaded ${F[$1]}" || echo "failed: exp$1"; }
a=$(echo "${1:-}" | tr 'A-Z' 'a-z' | sed 's/^exp//')
if [ "$a" = all ]; then for k in "${!F[@]}"; do get $k; done
elif [ -n "${F[$a]}" ]; then get $a
else echo "usage: bash get.sh exp8..exp15 | all"; fi
# datasets/weights are downloaded automatically when you run the notebook
