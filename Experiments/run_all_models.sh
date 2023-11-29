# Run dataset on CDIL-CNN, and other ML models, for cross-analysis 
jupyter nbconvert --to notebook --execute main.ipynb --model CDIL
jupyter nbconvert --to notebook --execute main.ipynb --model TCN
jupyter nbconvert --to notebook --execute main.ipynb --model CNN
jupyter nbconvert --to notebook --execute main.ipynb --model Deformable
jupyter nbconvert --to notebook --execute main.ipynb --model GRU
jupyter nbconvert --to notebook --execute main.ipynb --model LSTM
