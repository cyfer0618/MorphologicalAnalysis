# MorphologicalAnalysis


1_acl.csv -> ACL/1.csv


```
word;lemma;morphology

asya;idam;n. sg. g.

sūryasya;sūrya;m. sg. g.

saḥ;tad;m. sg. nom.

putraḥ;putra;m. sg. nom.
```





1_gt.csv -> ACL/1.csv


```
word;lemma;morphology

saḥ;tad;m. sg. nom.

sūryasya;sūrya;m. sg. g.

putraḥ;putra;m. sg. nom.
```



Check.ipynb - It is a file which is used to calculated recall, precision and Fscore.
Check.ipynb - It contains for Homonymy and Syncretism code also.
Ground truth files with starting time and ending time - https://drive.google.com/drive/folders/1yz6gLEwTgeoaUv1UpfJ8l95RYi7q4WJ8?usp=sharing




For Morphology Number conversion function use morphology_function.py
mapping_groundtruth_nbest.txt is having mapping 



File location # Group Utt (Ground truth Utterance) # Utterance of candidate # test/dev file
For example : shr_new_nbest/new_1/0.csv # sp007-000001_1-01-bAlakAnDaH # sp007-000001_1-01-bAlakAnDaH-1 # test
