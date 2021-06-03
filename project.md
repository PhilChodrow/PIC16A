---
layout: page
title: Group Mini-Project
permalink: project/
---

Part of your final assessment in PIC16A is via a **group mini-project.** In this project, you and your partners will perform and communicate about a complete data analysis of a real data set. 
<div class="fancy-h1"> Timeline </div>

You'll have three scheduled discussion periods in Weeks 7 and 8 to work on this project (see the Schedule). In total, the project is intended to require approximately 10 hours of effort from each of you (that is, ~30 total person-hours for a three-person group, or ~20 total hours for a two-person group). You are expected to coordinate with each other to schedule additional meetings or delegate responsibilities as appropriate to complete the project. Projects are due on the last day of instruction (i.e. Friday of Week 10) are submitted as a group. 

There will also be homework assignments due during this time. Some of the homework problems will be specifically related to project tasks, and you are especially encouraged to work on these problems with your group members.  

Your primary resource in this project should be your group members. However, if you are all stuck on a particular aspect, you are welcome to ask for help from your peers on Campuswire. 

<div class="fancy-h1"> Project Components </div>

Your project should be contained and submitted in a single Jupyter notebook. You'll perform components of the project in different notebooks over the course of the scheduled Discussion periods and homework assignments. Your group is responsible for moving the required code into your final project file. You may find it useful to employ [Google Colab](https://colab.research.google.com/), which allows collaboration on Jupyter Notebooks similarly to, say, Google Docs. 

Your project should contain the following sections: 

1. **Group Contributions Statement:** Briefly describe which group members contributed to which parts of the project (parts listed below). Here is an example of an acceptable Group Contributions statement. 
> "All three of us wrote the data acquisition and preparation, Xenith led the exploratory analysis, Rodrigo and Essun led on modeling, all three of us wrote the discussion." 
4. **Exploratory Analysis:** compute summary statistics and construct visualizations about the relationships between variables. You should explain how your analysis supports your modeling decisions below. Your exploratory analysis should include **at least 3 figures** and **at least 1 displayed table**. May include data loading, preparation and cleaning. *2-person groups need include only 2 figures and 1 table.* 
5. **Modeling:** deploy at least three machine learning models and evaluate their performance. Must include (cross)-validation and evaluation on unseen testing data. May include feature engineering. In this section, you should show how you systematically select your features to achieve optimal predictive accuracy. As part of your model evaluation, you are required to use your model(s) to make predictions on unseen (testing) data. You are required to use multinomial logistic regression and decision tree models. You must also select one additional model to deploy. Possibilities include but are not limited to random forests; support vector machines; nearest-neighbor classifiers; and neural networks. You will need to learn how to import and use the corresponding model. In your submission, you should describe briefly, for each model, how it works and why it is suitable for the task at hand. Your explanations don't need to be detailed -- give some intuition for someone who has never seen that model before. *2-person groups need include and discuss only two models. One model must be either a decision tree or logistic regression. The second model can either be the other required model or a different model of the group's choice.* 
6. **Discussion:** describe the performance of your models, and state which combination of model and measurements you recommend. Discuss how the model could be improved if more or different data were available. Describe possible dangers associated with interpreting or using the model. 

<div class="fancy-h1"> Project Evaluation </div>

The project is worth 10% of your final grade, and will be graded out of 100 points. All members of the team will receive the same project grade, unless I either (a) receive private communication from a team-member that raises concerns about the team's collaboration or (b) the contributions statement suggests a highly inequitable division of labor. 

Here's what I'm looking for: 

- 20% for a clear and equitable **Group Contributions** statement.  
- 20% points for **Writing, Documentation, and Style**: Clear expository writing of the analysis, including narrative text walking the reader through the analysis; description of how the models work; docstrings and comments; and a critical discussion in the final section. 
- 20% points for **Exploratory Analysis**: A helpful exploratory analysis, including at least three figures and at least one table that support your decisions in the Modeling section. *2-person groups need include only 2 figures and 1 table.* These figures and tables must be **relevant to your modeling**, and this relevance must be explained in your text. 
- 20% points for **Modeling**: A full modeling pipeline, in which you deploy three or more machine learning models, describe how they work at an intuitive level, train them on data, and systematically evaluate their performance. Your evaluation methods should include both cross-validation to select the complexity parameters of a candidate model and evaluation on unseen testing data to evaluate its overall predictive power. Finally, you should also supply an analysis of any errors that your model makes; decision regions and confusion matrices are two good ways to approach this. *2-person groups need include only two models.* 
- 20% for **Model Performance**: you should indicate your best model, and demonstrate its predictive accuracy on test data not used to train the model. **Your best model must use no more than 3 features (data columns)**. This component of your score is calculated as `20 x (test accuracy)`. For example, if you achieve 92% accuracy on the test data, then your score for this part is 18.4. 

*I will have slightly lower expectations for the writing component for 2-person groups, but not **much** lower.*

Your work on the project during scheduled discussion sections will additionally count toward your participation grade, as in any other discussion section.  

<div class="fancy-h1"> Project Task </div>

An important task in the ecology of the Antarctic is to catalog the many different species of penguins in that area. Determining the species of a penguin often requires a combination of biological expertise and many precise measurements, which can be difficult to obtain. 

In the dystopian future, there are *too many penguins*: 

<figure class="image" style="width:50%">
  <img src="https://www.pluggedin.com/wp-content/uploads/2019/12/march-of-the-penguins-1536x863.jpg" class="center" alt="A large group of emperor penguins.">
  <figcaption><i>Too many penguins.</i></figcaption>
</figure>
Because there are so many, we can't take many detailed measurements on all of them! In order to classify the species of penguins in large volume, we need to figure out *which* measurements are most important for distinguishing penguin species. 

**Your goal in this mini project is to determine a small set of measurements that are highly predictive of a penguin's species.** Options include (but are not limited to) the island on which the penguin was encountered, the length and depth of the culmen (bill), the length of the flipper, the body mass, and the sex of the penguin. That is, you should systematically determine which of these features is most predictive of the penguin's species, using at least three distinct machine learning algorithms and evaluating the results. You are required to test decision trees and multinomial logistic regression. You may optionally use any additional algorithms that you would like. 

Part of the point of this project is to use a small number of measurements (i.e. columns in the data). **Your final model that you submit toward your Model Performance score must use three or fewer features.** Submissions that use a large number of measurements may receive only partial credit, even if they achieve very good predictive accuracy. 

For training and evaluating your models, we will use the Palmer Penguins data set. 
The Palmer Penguins data set was collected by collected by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station, Antarctica LTER](https://pal.lternet.edu/), a member of the [Long Term Ecological Research Network](https://lternet.edu/). [Download the CSV](https://philchodrow.github.io/PIC16A/content/IO_and_modules/IO/palmer_penguins.csv) data. 
It contains measurements on three penguin species: Chinstrap, Gentoo, and Adelie. 

<figure class="image" style="width:50%">
  <img src="https://allisonhorst.github.io/palmerpenguins/man/figures/lter_penguins.png" alt="Three stylized penguins, one each of the species Adelie, Gentoo, and Chinstrap, with labels above their heads and patches of color behind them.">
  <figcaption><i>Illustrations of the penguin species in the Palmer Penguins data set, by Allison Horst.</i></figcaption>
</figure>

In data science, it is important to develop a thorough understanding of the data that you are attempting to model. I recommend consulting [these](https://www.youtube.com/watch?v=ZbASA6fZaRI) [helpful](https://www.youtube.com/watch?v=M5UlTRrVaTk) [videos](https://www.youtube.com/watch?v=RoTVc32TLx8) to build your knowledge of penguin behaviors outside their natural habitats. 








<div class="fancy-h1"> An Example of Good Data Writing </div>

Here is a [very nice analysis](https://humansofdata.atlan.com/2016/07/machine-learning-python/) of the famous Titanic survivors data that exemplifies the stages of data analysis and good expository writing. Your projects are not required to be as detailed as shown here, but this analysis would be an excellent place from which to draw inspiration. Please notice: 

- **Explanations**: The ratio of words to code and figures is high. 
- **Iteration**: The writers often start with one machine learning model, and then improve it (or compare it to competitors) as they go. 
- **Discussion**: The author critically considers what has been learned from the model; where the model might fail; and what this implies about the data. 

You can also steal some good tricks here with `pandas`, `matplotlib`, and `scikit-learn`!
