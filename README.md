# Digital Humanities: Multatuli project
This is the github repository for the Multatuli project for the course Digital Humanities at the Vrije Amsterdam (2021).
Code contributors: Myrthe Buckens and Alessandra Polimeno 

### data 
In the data folder, you will find the following subfolders for Dutch and English data with the folling files: 
#### dutch
* original data file with Dutch data: `MH1881.txt`
* original data file with Dutch data, poems excluded: `MH1881_poems_excluded.txt`
* preprocessed file with labeled sentences: `labeled_sents.tsv`
* preprocessed file with labeled bundles: `bundles.tsv`
* training file for sentences: `training.tsv`
* test file for sentences: `test.tsv`
* training file for sentences with features: `training_features.tsv`
* test file for sentences with features: `test_features.tsv`
* test file for sentences with predictions by SVM: `test_features-prediction.tsv`
* training file for bundles: `training_bundles.tsv`
* test file for bundles: `test_bundles.tsv`
* training file for bundles with features: `training_bundles_features.tsv`
* test file for bundles with features: `test_bundles_features.tsv`
* test file for bundles with predictions by SVM: `test_bundles_features-prediction.tsv`

#### english
* original data file with English data, poems excluded: `Multatuli_English Corpus.txt`
* preprocessed file with labeled sentences: `eng_labeled_sents.tsv`
* preprocessed file with labeled bundles: `eng_bundles.tsv`
* training file for sentences: `eng_training.tsv`
* test file for sentences: `eng_test.tsv`
* training file for sentences with features: `eng_training_features.tsv`
* test file for sentences with features: `eng_test_features.tsv`
* test file for sentences with predictions by SVM: `eng_test_features-prediction.tsv`
* training file for bundles: `eng_training_bundles.tsv`
* test file for bundles: `eng_test_bundles.tsv`
* training file for bundles with features: `eng_training_bundles_features.tsv`
* test file for bundles with features: `eng_test_bundles_features.tsv`
* test file for bundles with predictions by SVM: `eng_test_bundles_features-prediction.tsv`

### requirements 
The needed requirements can be found in `requirements` and installed by running
```pip install requirements``` from your terminal.

### code
In the code folder, you will find the following scripts, to be run with the specified arguments:
* preprocessing and annotating the Dutch data: `nl_preprocessing` \<input data\> \<output location sentences\> \<output location bundles\> 
* preprocessing and annotating the English data: `eng_preprocessing` \<input data\> \<output location sentences\> \<output location bundles\> 
* splitting the data to training and test files: `splitting.py` \<input data\> \<output location training\> \<output location test\> 
* extracting the features for sentences: `feature_extraction.py` \<input data\> \<output location\> \<language\>
* extracting features for bundles: `features_bundles.py` \<input data\> \<output location\> \<language\>
* running the SVM classifier and saving predictions: `svm.py` \<input data\> \<output location\>

For running the mBERT model, we used google colaboration. It is possible to download this code on top of the page as .ipynb or .py, but for speed and possible hardware limitations, we advise you run the code online with the GPU from google. 
The code can be found by following the link below: 
* mBERT fine-tuned: https://colab.research.google.com/drive/1GBQZ5HO_hW5Wa1PbbYOFACFmQkgqfsDj?usp=sharing
(the link has viewer rights only, to run the code and upload the different files, create a duplicate of the code to make adjustments) 
