[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

# House Prices Dataset Analysis (Group 4 Final Project)

# Project Description

In our final project, we analyzed a house prices dataset that is publicly available on Kaggle which can be found using this link: [Housing Prices Dataset] (https://www.kaggle.com/datasets/lespin/house-prices-dataset). This dataset contains housing price data from Ames, Iowa. The dataset has already been cleaned, and has been separated into a training and testing set, making it suitable for linear regression. We used linear regression techniques to predict housing price based on certain factors (more information about our process can be found in Part 1 and Part 2 of this project).

# Repository Contents

Our repository contains the following:

- `Part1-EDA`: This folder contains our initial exploratory data analysis steps and the data used in this project.
- `Part2-Prediction`: This folder contains our prediction process that followed after the EDA.
- `pdf_builds`: This folder contains pdf files of our analysis notebooks.
- `src`: This folder contains the functions we made to aid our analysis.
- `tests`: This folder contains tests to test our functions.
- `environment.yml`: This is an environment file with all of the required packages for our project.
- `main.ipnyb`: This notebook contains an overview of our project.
- `Makefile`: This is a Makefile containing env and all targets. The env target makes or updates the environment (run "make env" in the terminal) and the all target runs all of the notebooks (run "make all" in the terminal).

All of the figures are saved into separate folders within the `Part1-EDA` and `Part2-Prediction` folders. 

# Testing

**To run the tests, execute the following command in the terminal from the root directory of the project:**

```bash
pytest tests/
```

# How to Install Environment

**To install the environment run the following in the terminal:** 

```bash
conda env create -f environment.yml
conda activate final_env
```

# LICENSE

This project is licensed under the BSD 3-Clause License. 
