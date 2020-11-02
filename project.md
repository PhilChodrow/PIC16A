---
layout: page
title: Group Mini-Project
permalink: project/
---

Part of your final assessment in PIC16A is via a **group mini-project.** In this project, you and your partners will perform a complete machine learning analysis of a real data set. 

<div class="fancy-h1"> Timeline </div>

You'll have three scheduled discussion periods in occurring in Weeks 7 and 8 to work on this project (see the Schedule). In total, the project is intended to require 8-10 hours of effort from each of you (that is, 24-30 total person-hours for a three-person group, or 16-20 total hours for a two-person group). You are expected to coordinate with each other to schedule additional meetings or delegate responsibilities as appropriate to complete the project. Projects will be due on the last day of instruction, Friday, 12/11. 

There will also be homework assignments due during this time. Some of the homework problems will be specifically related to project tasks, and you are especially encouraged to work on these problems with your group members.  

<div class="fancy-h1"> Project Components </div>

Your project should be contained and submitted in a single Jupyter notebook. We will give you a template. You'll perform components of the project in different notebooks over the course of the scheduled Discussion periods; your group is responsible for moving the required code into your final project file. 

Your project should contain the following sections: 

1. **Group Contributions Statement:** Briefly describe which group members contributed to which parts of the project (parts listed below). Here is an example of an acceptable Group Contributions statement. 
> "All three of us wrote the data acquisition and preparation, Xenith led the exploratory analysis, Rodrigo and Essun led on modeling, all three of us wrote the discussion." 
2. **Data Acquisition:** read in the data from a file, and split into training and testing data sets. 
3. **Data Preparation:** clean and manipulate the data as needed. May include feature engineering. 
4. **Exploratory Analysis:** compute summary statistics and construct visualizations about the relationships between variables. You should explain how your analysis supports your modeling decisions below. Your exploratory analysis should include **at least 3 figures** and **at least 1 table**. 
5. **Modeling:** deploy two or more machine learning models and evaluate their performance. May include feature engineering. In this section, you should show how you systematically select your features to achieve optimal predictive accuracy. As part of your model evaluation, you are required to use your model(s) to make predictions on unseen (testing) data. 
6. **Discussion:** describe the performance of your model. Discuss how the model could be improved if more or different data were available. Describe possible dangers associated with interpreting or using the model. 

<div class="fancy-h1"> Project Evaluation </div>

The project is worth 10% of your final grade, and will be graded out of 10 points. All members of the team will receive the same project grade, unless I either (a) receive private communication from a team-member that raises concerns about the team's collaboration or (b) the contributions statement suggests a highly inequitable division of labor. 

Here's what I'm looking for: 

- 3 points for **Exploratory Analysis**: A helpful exploratory analysis, including figures and tables and that support your decisions in the Modeling section. `
- 3 points for **Modeling**: A full modeling pipeline, in which you deploy two or more machine learning models, train them on data, and systematically evaluate their performance. 
- 2 points for **Writing**: Clear expository writing of the analysis, including narrative text walking the reader through the analysis; docstrings and comments; and a critical discussion in the final section. 
- 2 point for a clear and equitable **Group Contributions** statement.  

Your work on the project during scheduled discussion sections will additionally count toward your participation grade, as in any other discussion section.  

<div class="fancy-h1"> Project Task </div>

An important task in the ecology of the Antarctic is to catalog the many different species of penguins in that area. Determining the species of a penguin often requires a combination of biological expertise and many precise measurements, which can be difficult to obtain. 

In the dystopian future, there are *too many penguins*: 

<figure class="image" style="width:50%">
  <img src="https://www.pluggedin.com/wp-content/uploads/2019/12/march-of-the-penguins-1536x863.jpg" class="center" alt="A large group of emperor penguins.">
  <figcaption><i>Too many penguins.</i></figcaption>
</figure>
Because there are so many, we can't take many detailed measurements on all of them! In order to classify penguins in large volume, we need to figure out *which* measurements are most important for distinguishing penguin species. 

**Your goal in this mini project is to determine which two possible measurements are most predictive of a penguin's species.** Options include the island on which the penguin was encountered, the length and depth of the culmen (bill), the length of the flipper, the body mass, and the sex of the penguin. That is, you should systematically determine which two of these features is most predictive of the penguin's species, using at least two distinct machine learning algorithms and evaluating the results. You are required to test decision trees and multinomial logistic regression. You may optionally use any additional algorithms that you would like. 


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

You can also steal some good tricks here with `pandas` and `matplotlib`!

