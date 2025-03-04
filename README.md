# Centrality Measure Prediction
Are we just measuring the same social network construct repeatedly?

The goal of this project is to analyze wether certain network centrality measures can be predicted using other centrality measures through different machine learning models.

## Results

To view the results of the project please see the Milestone05 folder. Please see the report for a detailed explanation on the process. The results are in the results folder. Please see the specific readme in the folder for additional details.

## Progress

<strong>1. Milestone01 (10/20/2019):</strong>
  - Complete Networkx practice notebook.
  - Generate small-world, scale-free, random, and scale-free small-world networks.
  
<strong>2. Milestone02 (10/30/2019): </strong>
  - Create data that contains 25 instances of each graph with node levels 100, 200, 400, 800.
  - Calculate centrality values for all nodes in the generated graphs.
  - Rank centrality values on each graph.
  - Write all results to csv file.
  - Compute pairwise correlations between the rankings for each graph type. (Get a baseline to make accurate predictions).
  - Create basic classifier to predict whether a node centrality is in the top 25% bsed on another centrality. Use three different classifiers and use 10 cross-fold validation.
  
<strong>3. Milestone03 (11/13/2019):</strong>
  - Demonstrate how the scale-free small-world network generated has the three properties of high average clustering, low average distance, and power law degree distribution
  - Correct errors from Milestone02
  - Correct the process for 10 cross-fold validation
  - Add two more centrality measures
  - Present correlations using heatmaps
  - Summarize results into a markdown table
  - Generate 50% more data
  - Create a research report that has introduction, background, and methods sections.
  
<strong>4. Milestone04 (11/26/2019):</strong>
  - Address comments in report and make edits
  - Add a figure to illustrate the complete process
  - Provide results from classifiers. Utilize a supercomputing cluster to get results faster.
  - Add a literature survey to background section of the report to discuss related work.

<strong>5. Milestone05 (12/12/2019):</strong>
  - Package data into neat folders such as Data, Notebooks, Cluster Scripts, Results, and Report
  - Properly utilize nested cross-fold validation
  - Address comments from peer review
  - Include a results section with corelations and machine learning results
  - Add 4 other centrality metrics other than centrality measures
  - Final Report
   
Contributors: Alex Freund, Jaxson Wirth, Dat Luong<br><br>
This project was completed in Miami University's CSE 470C Machine Learning course taught by Dr. Phillippe Giabbanelli and guidance for the research was provided by Dr. Phillippe Giabbanelli.
