# Centrality_Measure_Prediction
Are we just measuring the same social network construct repeatedly?

The goal of this project is to analyze wether certain network centrality measures can be predicted using other centrality measures through different machine learning models.

## Progress

1. Milestone01 (10/20/2019): 
  - Complete Networkx practice notebook.
  - Generate small-world, scale-free, random, and scale-free small-world networks.
2. Milestone02 (10/30/2019):  
  - Create data that contains 25 instances of each graph with node levels 100, 200, 400, 800.
  - Calculate centrality values for all nodes in the generated graphs.
  - Rank centrality values on each graph.
  - Write all results to csv file.
  - Compute pairwise correlations between the rankings for each graph type. (Get a baseline to make accurate predictions).
  - Create basic classifier to predict whether a node centrality is in the top 25% bsed on another centrality. Use three different classifiers and use 10 cross-fold validation.


This project was completed in Miami University's CSE 470C course taught by Dr. Phillippe Giabbanelli.
Contributors: Alex Freund, Jaxson Wirth, Dat Luong
