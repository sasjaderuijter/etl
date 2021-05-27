# etl
_Universiteit van Amsterdam - Web Services and Cloud-Based Systems: assignment 5_

This Brane package is used as the data cleaning part of the pipeline.
It uses the CSV datasets: _titanic.csv, diabetes.csv_ and _heart_disease.csv_

## Installation
Import the package as follows:
```shell
$ brane import sasjaderuijter/etl
```
## Running package in JupyterLab
Import the package using BraneScript in a JupyterLab notebook.
```shell
import etl;
```

Create the titanic training data, using the dataset _titanic.csv_
```shell
create_titanic_trainset("/data/titanic");
```

Create the diabetes training data, using the dataset _diabetes.csv_
```shell
create_diabete_trainset("/data/diabetes");
```

Create the heart disease training data, using the dataset _heart_disease.csv_
```shell
create_heart_disease_trainset("/data/heart_disease");
```
