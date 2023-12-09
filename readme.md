# ECS 171 Group 20 - Early Onset Fungal Infection Classifier 

[Report](https://www.overleaf.com/project/6552ffdb8bbc78e82820ad55)

`./EDA` contains dataset and Exploratory Data Analysis scripts. 
`./Models` contains CDIL-CNN, and other ML models, which can be invoked in the runtime.
`./Experiments` contains all components of the runtime. Process below:
1) Runtime is performed in `main.ipynb`, and it's also where the training happens. Methods for the training are called from `train.ipynb` 
2) `config.ipynb` is passed into the runtime for the CNN's hyperparameters
3) `defungi.ipynb' performs the necessary processing to complete
4) You need only run `main.ipynb` for runtime, cell by cell. It will load in the local dataset every time, invoke the architecture, and train it on the CDIL-CNN

---
***Everything below is a modified version of the readme.md from the CDIL-CNN GitHub repository.***
[Link to Repository](https://github.com/LeiCheng-no/CDIL-CNN/)
---

# Classification of Long Sequential Data using Circular Dilated Convolutional Neural Networks

paper: [https://doi.org/10.1016/j.neucom.2022.10.054](https://doi.org/10.1016/j.neucom.2022.10.054). 

## **Architecture**
CDIL-CNN is a novel convolutional model for sequence classification. We use symmetric dilated convolutions, a circular mixing protocol, and an average ensemble learning.

#### Symmetric Dilated Convolutions
<p align="left">
<img src="Misc/dil.png" width="600">
</p>


#### Circular Mixing
<p align="left">
<img src="Misc/cir1.png" width="150">
<img src="Misc/cir2.png" width="150">
<img src="Misc/cir3.png" width="150">
</p>


#### CDIL-CNN
<p align="left">
<img src="Misc/cdil.png" width="300">
</p>

# **Cite**
```
@article{cheng2022classification,
  title={Classification of long sequential data using circular dilated convolutional neural networks},
  author={Cheng, Lei and Khalitov, Ruslan and Yu, Tong and Zhang, Jing and Yang, Zhirong},
  journal={Neurocomputing},
  year={2022},
  publisher={Elsevier}
}
```
