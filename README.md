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

``` Notebook Creation
 Create the 01_data_ingestion.ipynb inside the research folder, reading from the data ingestion of `config.yaml`.

 Constants and Imports
 Update the constant file` __init__.py `with path codes, then import them into the notebook 01_data_ingestion.ipynb.

 Configuration Manager
 Create the configurationManager inside the notebook `01_data_ingestion.ipynb`, writing code for download, extraction, and the pipeline for calling other functions.

 Error Handling
 Face an error during runtime, should set or write something inside the yaml files (`schema.yaml`, `params.yaml`).
```

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

Add the artifact inside the gitignore folder - do not want to push them.

```
This dataset appears to have 12 columns with the following features:
fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality

```

GitHub Repository: [https://github.com/ericmaniraguha/mlflow_project_end_to_end](https://github.com/ericmaniraguha/mlflow_project_end_to_end)

Dagshub Project Tracking: [https://dagshub.com/ericmaniraguha/mlflow-project-industry](https://dagshub.com/ericmaniraguha/mlflow-project-industry)
