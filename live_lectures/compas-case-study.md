# Fact Sheet: COMPAS Case Study

*This fact sheet is derived from [this ProPublica article](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) and the [accompanying technical documentation](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm).* 

## Overview

COMPAS is recidivism prediction algorithm, created by a for-profit company called Northpointe. 

*Recidivism* refers to criminal re-offense, i.e. committing a crime after one has already been arrested or convicted for a previous crime. 

The COMPAS algorithm produces a *recidivism score* between 0 and 1 for criminal defendants. Northpointe claims that the score estimates the probability that the individual will commit a future crime in the next two years. 
For example, an individual with a COMPAS score of 0.7 has, according to Northpointe, a 70% chance of committing a crime in the future.

COMPAS and similar algorithms are used in many courtrooms across the US to inform: 

- Setting of bail (how much money a defendant must pay in order to not be placed in jail prior to their criminal hearing).
- Sentencing (e.g. how much time a convicted defendant will spend in prison).
- Parole decisions (whether a convicted defendant can be released early from prison on a probationary basis).

## COMPAS Inputs

The COMPAS algorithm is a machine learning model. The target variable is whether or not the individual commits a future criminal offense.  

The predictor data is the individual's response to a [long questionnaire](https://www.documentcloud.org/documents/2702103-Sample-Risk-Assessment-COMPAS-CORE.html). Some of the questions include: 

1. The gender and marital status of the individual. 
1. The criminal history of the individual. 
2. The individual's family history, including: 
    - Whether they were raised by two parents 
    - Whether they were adopted. 
    - How often they speak with their family. 
2. The criminal history of the individual's family. 
3. The criminal history, gang membership, and drug use of the individual's friends. 
4. Whether or not the individual has used drugs or alcohol. 
5. The housing status of the individual, including: 
    - Whether or not they are homeless
    - How many times they have moved, - Whether or not they have roommates. 
5. The neighborhood in which the individual lives, including: 
    - Whether the neighborhood is dangerous. 
    - Whether any of the individual's friends have been victims of crimes. 
    - Whether or not drugs are easily accessible within the neighborhood. 
6. The individual's educational history, including: 
    - Whether they completed high school. 
    - Their grades. 
    - Whether they were suspended or expelled from school. 
7. The individual's employment and financial status, including: 
    - Whether they have a job. 
    - Whether they have ever been fired. 
    - Whether they struggle to support themselves financially. 
8. Various self-reported personality measures, such as:
    - Whether the individual often feels bored or discouraged in their leisure time. 
    - Whether the individual often feels sad or isolated. 
    - Whether the individual tends to keep their commitments. 
    - Whether the individual is prone to anger. 

**The survey does not inquire about the race of the individual.**

## COMPAS Performance

According to [an analysis](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) by ProPublica, the COMPAS algorithm was able to correctly predict whether or not an individual defendant would commit a criminal offense within the next two years 61% of the time. 

However, the errors that the algorithm makes are not evenly distributed between Black and White defendants. 

| | WHITE	| AFRICAN AMERICAN |
| - |-------|---------------------|
| Labeled Higher Risk, But Didn’t Re-Offend	| 23.5% |	44.9%|
| Labeled Lower Risk, Yet Did Re-Offend |	47.7%	| 28.0%|


