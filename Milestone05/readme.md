## Read Me for Milestone 5

In this milestone, we used the redhawk cluster to generate new data. We added 4 network properties to our data, including average distance, average clustering, number of cliques, and strongly connected.

All code used to generate the data on the redhawk cluster is in the data_generation folder. The code.py file was used to submit code for each job. For each job, we would change the bottom of code.py to a different network type and/or network size. Because there were 4 network types and 4 network sizes, there were 16 total jobs. The generate.job file was used to submit each job and had to be modified to reflect each job name. All the generated data is also in the data_generation folder, organized by network type and size.

Then, we used the ipython notebook to attach all the data files together and built binary columns for the 7 centrality measures. Using this binary_data file, we trained 5 classifiers in the notebook and recorded their accuracy, precision, and recall. The output data for each classifier is in the xx_results folder, where xx is a two letter abbreviation for the classifier type. Within this folder, there is an overall_results file that contains average accuracies, precisions, and recalls for each network type. More specific results for each network type, as well as the best grid search parameters, can be found in the corresponding network type file (e.g. Scale-Free.csv).

For example, to view the overall results from the decision tree classifier, open the dt_results folder and click on the overall_results file. Here you will see the network name followed by the average accuracy, precision, and recall for each network type. At the bottom there is the overall accuracy, precision, and recall for the decision tree classifier.

Key:
dt: Decision Tree
rf: Random Forest
nb: Naive Bayes
sv: Support Vector
gd: Gradient Descent
