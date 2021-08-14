# MSc. Thesis

This repository contains files used for my MSc. Thesis performing landslide susceptibility analysis using data-driven models. The "Sampling" notebook creates a DataFrame of explanatory variables by reading several different raster files and all other notebooks create or evaluate the performance of several different statistical or machine learning models using scikit-learn. Models include: logistic regression, SVM, classification tree and random forest.

A second folder contains Python scripts used to calculate rasters of the explanatory variables that are derived from a DEM such as slope, aspect, curvature, flow accumulation, among others. These are typical implementations of geoprocesses.
