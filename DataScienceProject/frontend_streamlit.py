import streamlit as st
import pandas as pd
from apriori_new import runApriori, dataFromFile, to_str_results

st.markdown("# Apriori on 'primary tumor' dataset")

st.sidebar.markdown(
    """The app is supposed to show information about my dataset and the rules that apriori algorithm found.
    The primary tumor domain was obtained from the University Medical Centre, Institute of Oncology, Ljubljana, Yugoslawia.
    The dataset topic is primary cancer. The variables are categorical, therefore suitable for association rule mining."""
)

default_csv = ("primary_tumor_data.csv")

st.markdown('Here are some sample rows from the dataset:')
csv_file = pd.read_csv(default_csv, header=None, lineterminator="\n")
st.write(csv_file.head())
st.markdown("The data was encoded in integers (339 instances, 18 attributes). The given description can be seen below.")
st.markdown(""" Attribute Information: (class is location of tumor)	
    --- NOTE: All attribute values in the database have been entered as	
              numeric values corresponding to their index in the list	
              of attribute values for that attribute domain as given below.	
    1. class: lung, head & neck, esophasus, thyroid, stomach, duoden & sm.int,	
              colon, rectum, anus, salivary glands, pancreas, gallblader,	
              liver, kidney, bladder, testis, prostate, ovary, corpus uteri, 	
              cervix uteri, vagina, breast	
    2. age:   <30, 30-59, >=60	
    3. sex:   male, female	
    4. histologic-type: epidermoid, adeno, anaplastic	
    5. degree-of-diffe: well, fairly, poorly	
    6. bone: yes, no	
    7. bone-marrow: yes, no	
    8. lung: yes, no	
    9. pleura: yes, no	
   10. peritoneum: yes, no	
   11. liver: yes, no	
   12. brain: yes, no	
   13. skin: yes, no	
   14. neck: yes, no	
   15. supraclavicular: yes, no	
   16. axillar: yes, no	
   17. mediastinum: yes, no	
   18. abdominal: yes, no	
""")

st.markdown('---')
st.markdown("## Inputs")

st.markdown('''
            **Support** measures directly how often combinations of items occur.

            **Confidence** the confidence is the ratio of observing the antecedent
            and the consequent together in relation to only the transactions that contain 𝑋.
            A high confidence indicates that the consequent often occurs when the antecedent is in a transaction.''')

st.latex(r'''confidence(X->Y) = \frac{support(X \cup Y)}{support(X)}''')

support_helper = ''' > Support(A) = (Number of transactions in which A appears)/(Total Number of Transactions') '''
confidence_helper = ''' > Confidence(A->B) = Support(AUB)/Support(A)') '''
st.markdown('---')

support = st.slider("Enter the Minimum Support Value", min_value=0.1,
                    max_value=0.9, value=0.15,
                    help=support_helper)

confidence = st.slider("Enter the Minimum Confidence Value", min_value=0.1,
                       max_value=0.9, value=0.6, help=confidence_helper)
st.markdown('---')
processed_csv = "preprocessed_data.csv"
inFile = dataFromFile(processed_csv)

items, rules = runApriori(inFile, support, confidence)

i, r = to_str_results(items, rules)

st.markdown("## Results")

st.markdown("### Frequent Itemsets [item, support]")
st.write(i)

st.markdown("### Frequent Rules [rule, confidence, lift, leverage, conviction]")
st.write(r)