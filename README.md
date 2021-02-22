# FINAL BOSS: The last NN Project (Christoph Otto , Maria Francis)

 This is the final project of our neural networks introductory course.
It is a POS-Tagger that uses a simple neural network.

### Table of Contents

* General Information (#general-information)
* Features (#features)
* Setup (#setup)
* Usage (#usage)
* Preprocessing (#preprocessing)
* Technologies (#technologies)
* Sources (#source)
* Other Information (#other-information)


#### Preprocessing

To preprocess your data, you will need the files 
- data_preprocesser.py , which contains the code that preprocesses your data
- your data in a .conll file, for example "sample.conll"

Make sure to keep these files in the same directory.

In your terminal, move to the directory where you have stored these files:

	cd NN-Project

To run the preprocesser, call it with the file you want to preprocess and the file to write the preprocessed data in as arguments: 

	py data_preprocesser.py sample.conll sample.info



#### Technologies

Python 3.8.2
