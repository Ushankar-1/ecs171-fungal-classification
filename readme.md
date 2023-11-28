# ECS 171 Group 20 - Early Onset Fungal Infection Classifier 

Report will be linked [here].

`./EDA` contains dataset and Exploratory Data Analysis scripts. 
`./Models` contains CDIL-CNN, and other ML models, which can be invoked in the runtime.
`./Experiments` contains all components of the runtime. Process below:
1) Runtime is performed in `lra_main.py`, and it's also where the training happens. Methods for the training are called from `lra_train.py` 
2) `lra_all.sh` is a simple wrap-around script that executes all of the models in `./Models` to make some comparisons
3) `lra_config.py` is passed into the runtime for the CNN's hyperparameters

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




## **Experiments**

### Long Range Arena
Long Range Arena (LRA) is a public benchmark suite. The datasets and the download link can be found in [the official GitHub repository](https://github.com/google-research/long-range-arena). 

To reproduce the LRA experiment results, you should:
1. Download `lra_release.gz` (~7.7 GB), extract it, move the folder `./lra_release/lra_release` into our **./create_datasets/** folder, and run ***all_create_datasets.sh***. 
2. Run ***lra_main.py*** for one experiment or run ***lra_all.sh*** for all experiments.

The dataset creators will create 3 files for each task and store them in the **./lra_datasets/** folder in the following format:
`{task}.train.pickle`
`{task}.test.pickle`
`{task}.dev.pickle`

The **./lra_log/** folder will save all results.
The **./lra_model/** folder will save all best models.

We provide our used configurations in ***lra_config.py***.

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
