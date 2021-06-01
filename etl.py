#!/usr/bin/env python3
import os
import sys
import pandas as pd
import yaml


# create titanic training set 
def create_titanic_trainset(file: str) -> str:

    df = pd.read_csv(f"{file}.csv")

    train = df[['Survived','Pclass','Sex','Age']]   

# move the survived column to the end
    cols = list(train)
    
    cols.insert(3,cols.pop(cols.index('Survived')))

    train = train.loc[:,cols] 

# clean 
    train.dropna(
        
        axis = 0,
        
        how = 'any',
        
        inplace=True
    )   

    # convert male/female to 0/1
    map = {'male': 0, 'female': 1}

    train['Sex'] = train["Sex"].map(map)

    result = train.copy()

    feature = 'Age'

    max_value = df[feature].max()
    
    min_value = df[feature].min()
    
    result[feature] = (df[feature] - min_value) / (max_value - min_value)
    
    for index in range(len(result)):
    
        result[feature].iloc[index] = float('%.4f' %result[feature].iloc[index])

    train = result

    train.to_csv('/data/titanic_trainset.csv',index = False, sep = ';')

    return '/data/titanic_trainset.csv'



# create diabetes training set 
def create_diabete_trainset(file: str) -> str:

    df = pd.read_csv(f"{file}.csv")

    train = df[['BloodPressure','BMI','Age','Outcome']] 

    # remove_bad_rows(train)
    train.dropna(
        
        axis = 0,
        
        how = 'any',
        
        inplace=True
    )   

    # repetitive part of normalization
    result = train.copy()

    feature = 'BloodPressure'

    max_value = df[feature].max()
    
    min_value = df[feature].min()
    
    result[feature] = (df[feature] - min_value) / (max_value - min_value)
    
    for index in range(len(result)):
    
        result[feature].iloc[index] = float('%.4f' %result[feature].iloc[index])

    train = result

    result = train.copy()

    feature = 'BMI'

    max_value = df[feature].max()
    
    min_value = df[feature].min()
    
    result[feature] = (df[feature] - min_value) / (max_value - min_value)
    
    for index in range(len(result)):
    
        result[feature].iloc[index] = float('%.4f' %result[feature].iloc[index])

    train = result

    result = train.copy()

    feature = 'Age'

    max_value = df[feature].max()
    
    min_value = df[feature].min()
    
    result[feature] = (df[feature] - min_value) / (max_value - min_value)
    
    for index in range(len(result)):
    
        result[feature].iloc[index] = float('%.4f' %result[feature].iloc[index])

    train = result

    train.to_csv('/data/diabete_trainset.csv',index = False, sep = ';')

    return '/data/diabete_trainset.csv'


# create heartdisease training set 
def create_heart_disease_trainset(file: str) -> str:

    df = pd.read_csv(f"{file}.csv")

    train = df[['age','sex','oldpeak','target']] 

    # remove_bad_rows(train)

    train.dropna(
        
        axis = 0,
        
        how = 'any',
        
        inplace=True
    )   

    #  repetitive part of normalization
    result = train.copy()

    feature = 'age'

    max_value = df[feature].max()
    
    min_value = df[feature].min()
    
    result[feature] = (df[feature] - min_value) / (max_value - min_value)
    
    for index in range(len(result)):
    
        result[feature].iloc[index] = float('%.4f' %result[feature].iloc[index])

    train = result
    
    result = train.copy()

    feature = 'oldpeak'

    max_value = df[feature].max()
    
    min_value = df[feature].min()
    
    result[feature] = (df[feature] - min_value) / (max_value - min_value)
    
    for index in range(len(result)):
    
        result[feature].iloc[index] = float('%.4f' %result[feature].iloc[index])

    train = result
    
    train.to_csv('/data/heart_disease_trainset.csv',index = False, sep = ';')

    return '/data/heart_disease_trainset.csv'


if __name__ == "__main__":
    
    command = sys.argv[1]
    
    functions = {
    "create_titanic_trainset": create_titanic_trainset,
    "create_diabete_trainset": create_diabete_trainset,
    "create_heart_disease_trainset": create_heart_disease_trainset
    }
    
    argument = os.environ["FILE"]


    output = functions[command](argument)
    print("--> START CAPTURE")
    print(yaml.dump({"output": output}))
    print("--> END CAPTURE")
   
   

