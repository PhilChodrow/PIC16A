---
layout: page
title: Group Mini-Project
permalink: project/
---

Part of your final assessment in PIC16A is via a **group mini-project.** In this project, you and your partners will perform a complete machine learning analysis of a real data set. 

<div class="fancy-h1"> Timeline </div>

You'll have three scheduled discussion periods in occurring in Weeks 7 and 8 to work on this project (see the Schedule). In total, the project is intended to require 8-10 hours of effort from each of you (that is, 24-30 total person-hours for a three-person group, or 16-20 total hours for a two-person group). You are expected to coordinate with each other to schedule additional meetings or delegate responsibilities as appropriate to complete the project. Projects will be due on the last day of instruction, Friday, 12/11. 

There will also be homework assignments due during this time. Some of the homework problems will be specifically related to project tasks, and you are encouraged to work on these problems with your group members.  

<div class="fancy-h1"> Project Components </div>

Your project should be contained and submitted in a single Jupyter notebook. We will give you a template. You'll perform components of the project in different notebooks over the course of the scheduled Discussion periods; your group is responsible for moving the required code into your final project file. 

Your project should contain the following sections: 

1. **Group Contributions:** Briefly describe which group members contributed to which parts of the project (parts listed below). Here is an example of an acceptable Group Contributions statement. 
> "All three of us wrote the data acquisition and preparation, Xenith led the exploratory analysis, Rodrigo and Essun led on modeling, all three of us wrote the discussion." 
2. **Data Acquisition:** read in the data from a file, and split into training and testing data sets. 
3. **Data Preparation:** clean and manipulate the data as needed. May include feature engineering. 
4. **Exploratory Analysis:** compute summary statistics and construct visualizations about the relationships between variables. You should explain how your analysis supports your modeling decisions below. Your exploratory analysis should include **at least 3 figures** and **at least 1 table**. 
5. **Modeling:** deploy one or more machine learning models and evaluate their performance. May include feature engineering. In this section, you should show how you "build up" the model -- start simple with just one or two predictor variables, and then show how adding more improves (or hurts) model performance. As part of your model evaluation, you are required to use your model(s) to make predictions on unseen (testing) data. 
6. **Discussion:** describe the performance of your model. Discuss how the model could be improved if more or different data were available. Describe possible dangers associated with interpreting or using the model. 

<div class="fancy-h1"> Project Evaluation </div>

The project is worth 10% of your final grade, and will be graded out of 10 points. All members of the team will receive the same project grade, unless I either (a) receive private communication from a team-member that raises concerns about the team's collaboration or (b) the contributions statement suggests a highly inequitable division of labor. 

Here's what I'm looking for: 

- 3 points for **Exploratory Analysis**: A helpful exploratory analysis, including figures and tables and that support your decisions in the Modeling section. `
- 3 points for **Modeling**: A full modeling pipeline, in which you deploy one or more machine learning models, train them on data, and systematically evaluate performance. 
- 2 points for **Writing**: Clear expository writing of the analysis, including narrative text walking the reader through the analysis; docstrings and comments; and a critical discussion in the final section. 
- 2 point for a clear and equitable **Group Contributions** statement.  

Your work on the project during scheduled discussion sections will additionally count toward your participation grade, as in any other discussion section.  

<div class="fancy-h1"> Project Task </div>

The Palmer Penguins data set was collected by collected by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station, Antarctica LTER](https://pal.lternet.edu/), a member of the [Long Term Ecological Research Network](https://lternet.edu/). [Download the CSV](https://philchodrow.github.io/PIC16A/content/IO_and_modules/IO/palmer_penguins.csv) data. 

<figure class="image" style="width:50%">
  <img src="https://allisonhorst.github.io/palmerpenguins/man/figures/lter_penguins.png" alt="Three stylized penguins, one each of the species Adelie, Gentoo, and Chinstrap, with labels above their heads and patches of color behind them.">
  <figcaption><i>Illustrations of the penguin species in the Palmer Penguins data set, by Allison Horst.</i></figcaption>
</figure>

Your job is to create a machine learning pipeline that can distinguish between different species of penguins based on physical measurements, such as their body mass, sex, inhabitance, and length of bills and flippers. We would like this algorithm to be as reliable as possible on unseen data. Your task is to explore the data, determine the relevant features, train several models to classify penguins, evaluate the models, and discuss what you have learned. 

<div class="fancy-h1"> An Example of Good Data Writing </div>

Here is a [very nice analysis](https://humansofdata.atlan.com/2016/07/machine-learning-python/) of the famous Titanic survivors data that exemplifies the stages of data analysis and good expository writing. Your projects are not required to be as detailed as shown here, but this analysis would be an excellent place from which to draw inspiration. Please notice: 

- **Explanations**: The ratio of words to code and figures is high. 
- **Iteration**: The writers often start with one machine learning model, and then improve it (or compare it to competitors) as they go. 
- **Discussion**: The author critically considers what has been learned from the model; where the model might fail; and what this implies about the data. 

You can also steal some good tricks here with `pandas` and `matplotlib`!

