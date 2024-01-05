# MLflow Project End-to-End - Red Wine Quality Dataset

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.). This dataset is also available from the UCI machine learning repository, [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality).

### Input Variables (based on physicochemical tests):

1. fixed acidity
2. volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11. alcohol

### Output Variable (based on sensory data):

12. quality (score between 0 and 10)

### Data Source

The dataset can be downloaded from the following link: [winequality-data.zip](https://github.com/ericmaniraguha/branching_data/blob/main/winequality-data.zip)



### Environment Configuration

```bash
conda create --name mlflow-env python=3.8
```

### 1. Folder Structure (template.py)

- Create a folder structure through template.py created manually.

### 2. Environment Variable

- Create the environment variable for the project.

### 3. `Setup.py`

- Write code for `setup.py`.

### 4. Package Installations

- Configure and install packages from `requirements.txt`.

### 5. Login Exception

- Create a login exception under `ml_project` > `util` > `__init__.py`

### 6. Integration with main.py

- Write code to call ml_project into `main.py` and execute.

### 7. Common Code

- Write some code under `ml_project` > `util` > `common`.

### 8. Working with trial.ipynb

Work with the file `trial.ipynb` for an explanation of `configBox`, use ensure to strengthen the code when using integers to characters.

-Done with exception logger and util.

## Configuration Updates

After configuration, follow the order to execute the files:

### 1. Update Configuration Files

- Update` config.yaml` first.
- Configure `schema.yaml`.
- Update `params.yaml` for parameters.

### 2. Configuration Files Order

- Update the `entity`.
- Update the configuration manager in `src config`.
- Update the `components`.
- Update the `pipeline`.
- Update `main.py`.
- Update `app.py`.
`config.yaml` will assist in future code paths.

## Data Ingestion Notebook (01_data_ingestion.ipynb)

### Notebook Creation
1. Create the `01_data_ingestion.ipynb` inside the `research` folder, reading from the data ingestion configuration specified in `config.yaml`.

### Constants and Imports
2. Update the constant file `__init__.py` with path codes, and then import them into the notebook `01_data_ingestion.ipynb`.

### Configuration Manager
3. Create the ConfigurationManager inside the notebook `01_data_ingestion.ipynb`, implementing code for downloading, extraction, and setting up a pipeline for calling other functions.

### Error Handling
4. Handle potential errors during runtime. If errors occur, ensure to set or write appropriate values inside the YAML files (`schema.yaml`, `params.yaml`).


## Config Updates and Folder Structure

### 1. Update Configuration Manager

- Update the configuration manager from config folder >> `configuration.py`.

### 2. Component Folder

- Create a folder inside the component called `data_ingestion.py`.

### 3. Pipelines

- Create the pipelines - create a file called `stage_01_data_ingestion.py`.

### 4. Testing Pipelines

- Add pipelines to `main.py` for testing, focus on `python main.py`, then delete artifacts.

### 5. Configuration Updates

- Configure `configuration.py` from ml_project >> config folder >> `configuration.py`.

### 6. Entity Configuration

- Configure the entity >> config_entity.py by adding codes.

### 7. Run Apps

Run my apps inside the terminal using `python main.py`.
NB: at each run i should delete the artifact created.

### 8. Artifact Handling

## 2. Workflows Data Validation configuration

#### 1. Update Configuration Files
   - Update `config.yaml` in the `ml_project` directory.
   - Update `schema.yaml` with the columns of the dataset in the `research` directory (updated once).
   - Update `params.yaml` if needed.

#### 2. Data Validation Configuration
   - Create a new file: `02_data_validation.ipynb` inside the `ml_project` > `research` directory.
   - Configure `schema.yaml` in the notebook with dataset details (datatype, data columns, etc.).
   - Set up ConfigurationManager in the notebook.
   - Define Data Validation Configurations.

#### 3. Run Data Validation
   - Execute `02_data_validation.ipynb` to perform data validation.
   - Create an artifact file containing validation results.

#### 4. Update Configuration Manager and Entity
   - Update the data path in `config.py` located inside the `config` folder. Add `data_validation` path.
   - Update the entity with `DataValidationConfig`.
   - In the `config` > `configuration.py`, add the method `get_data_validation_config`.

#### 5. Update Components
   - Update the component 'DataValidation' to incorporate the new configurations.

#### 6. Create Pipelines
   - Create a new pipeline file `state_02_data_validation.py`.
   - Add code to integrate the Data Validation component.

#### 7. Main Application
   - Update `main.py` to include the new pipeline for data validation.

#### 8. Update the App
   - Update `app.py` to reflect any changes made in the main application or pipelines.

#### 9. Run Application
   - Clean any existing artifacts.
   - Run `python main.py` to execute the updated application.


## 4. Workflows Model Training configuration

NB: `I will use same steps as the previous steps, only some few features i will add in params.py`
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml

- ElasticNet:
      1. alpha: 0.2
      2. l1_ratio: 0.1

- After this step I can run my `04_model_trainer.ipynb`, and i should 1st perform restarting my kernel

Writing other code of : 
      4. Update the entity
      5. Update the configuration manager in src config
      6. Update the components
      7. Update the pipeline 
      8. Update the `main.py` and clear the artifacts and run my code though terminal using `python main.py`

## 4. Workflows Model Evaluation configuration

Use same approach steps i used before.

## 5. Create the prediction UI

Steps: 
1. Create the prediction pipeline 
2. Create the prediction UI

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ericmaniraguha/mlflow_project_end_to_end
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ml_project python=3.8 -y
```

```bash
conda activate ml_project
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ericmaniraguha/mlflow-project-industry.mlflow \
MLFLOW_TRACKING_USERNAME=ericmaniraguha \
MLFLOW_TRACKING_PASSWORD=bd6ba5c72da612a729968285da9d31aed7c7d68f \
python script.py

Run this to export as env variables:


```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ericmaniraguha/mlflow-project-industry.mlflow

export MLFLOW_TRACKING_USERNAME=ericmaniraguha 

export MLFLOW_TRACKING_PASSWORD=bd6ba5c72da612a729968285da9d31aed7c7d68f

```


GitHub Repository: [https://github.com/ericmaniraguha/mlflow_project_end_to_end](https://github.com/ericmaniraguha/mlflow_project_end_to_end)

Dagshub Project Tracking: [https://dagshub.com/ericmaniraguha/mlflow-project-industry](https://dagshub.com/ericmaniraguha/mlflow-project-industry)
