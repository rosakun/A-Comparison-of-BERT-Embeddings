# FINAL BOSS: The last NN Project

 This is the final project of my neural networks introductory course.
It is a POS-Tagger that uses a simple neural network.

### Table of Contents

* General Information (#general-information)
* Preprocessing (#preprocessing)
* Setup & Usage (#setup&usage)
* Technologies (#technologies)
* Sources (#source)



#### General Information

We followed the Hugging Face's notebook for "How to fine-tune a model on token classification" at https://huggingface.co/transformers/notebooks.html. This tutorial shows a step-by-step tutorial for NER and we adapted the model for POS-tagging. For better orientation, we created a notebook for each transformer model.

Secondly, we created a dataloader to read our custom sample.tsv. We did this by looking at the conll2003 dataloader (https://github.com/huggingface/datasets/tree/master/datasets/conll2003) and also the Huggingface documentation on custom datasets (https://huggingface.co/transformers/custom_datasets.html). In order to make the dataloader work we had to split our preprocessed sample.tsv into a train.csv and dev.csv to train and test our custom dataset. 

Ultimately, we connected each jupyter notebook to wandb.ai to track our training, evaluate our findings and plot the results.


#### Setup & Usage

You will need to install Jupyter Notebook.

If you use conda, you can install it with:

	conda install -c conda-forge jupyterlab

If you use pip, you can install it with:

	pip install jupyterlab

To run the notebook, run the following command at the terminal or command prompt:

	jupyter notebook



In order for our code to compile, all notebooks must be in the same directory as our dataloader2.py, train.csv and dev.csv.
train.csv is the training set and dev.csv is the test set.


If you would like to train your model on your own dataset, see the Preprocessing section below.



To run the code, open one of the .ipynb files in Jupyter Notebook, and simply run the notebook.
Depending on which .ipynb file you choose, a different model will be run. 

NN_Bert_base_cased.ipynb runs Bert_base_cased
NN_ConvBert.ipynb runs ConvBERT
NN_Distilbert_base_cased.ipynb runs DistilBERT
NN_XLNET_base_cased.ipynb runs XLNET




#### Preprocessing

To preprocess your data, you will need the files 
- data_preprocesser.py , which contains the code that preprocesses your data
- your data in a .conll file, for example "sample.conll"

Make sure to keep these files in the same directory.

In your terminal, move to the directory where you have stored these files:

	cd NN-Project

To run the preprocesser, call it with the file you want to preprocess and the file to write the preprocessed data in as arguments: 

	py data_preprocesser.py sample.conll sample.info

This will give you a file called sample.info which contains information on the dataset, and a file sample.tsv, which contains the preprocessed data.

Unfortunately, we were unable to write a data splitting code, so there are some extra steps involved:

Convert your file sample.tsv into a .csv file, and split it into a training and a test set.
Any data splitting will work!


#### Technologies


Python 3.8.2
Datasets 1.4.1
Transformers 4.3.3
Notebook 6.2.0


#### Sources

https://huggingface.co/