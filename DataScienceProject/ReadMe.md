File descriptions:

1) primary_tumor_data.csv: dataset

2) primary_tumor_names.csv: description of the dataset, provided by the source Institute

3) DataPreprocessing.ipynb: Script to adapt the dataset so that I could use the apriori algorithm

4) preprocessed_dataset.csv: dataset with items instead of integers (replaced every integer by the respective item)

5) apriori_new.py: apriori from open source github repo, modified so that every necessary metric for the association rules is included

6) associated_rules.txt: rules created by apriori algorithm

7) frontend_streamlit.py: code for the frontend

8) config.toml: config for the frontend with specific theme