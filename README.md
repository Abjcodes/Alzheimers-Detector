# Alzheimer's Detection using MRI report data
## Objective: 
What is Alzhiemer's ?
Alzheimer's disease is thought to be caused by the abnormal build-up of proteins in and around brain cells. One of the proteins involved is called amyloid, deposits of which form plaques around brain cells. The other protein is called tau, deposits of which form tangles within brain cells.

Detection of Alzheimer's is very important for early treatment. Our aim with this project is to provide an easier way to predict early Alzheimer's symptoms.

## Project Description

### Data
The data used is longitudinal MRI data from Open Access Series of Imaging Studies.

## Model and Prediction
We performed essential data cleaning by dropping unnecessary columns and imputing other missing value. 
Decision tree is used for training the algorithm.

## Deployment
ML model is deployed using streamlit in heroku.

## Conclusion
We were able to build an end to end ML model that predicts early ALzhheimer's symptoms. The parameters can be modified by excluding parameters such as educational status etc.
This project can be modified to automatically detect required parameters from images of MRI reports as input.
