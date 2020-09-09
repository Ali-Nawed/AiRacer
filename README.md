# AiRacer

## Starting Envirionment

```bash
#Create the environment (airacer) via environment.yml
conda env create -f environment.yml
#Activate the environment
conda activate airacer
#check to see if installed correctly
conda env list
```

## Updating the Environment
While inside the conda environment if you change the dependecies run:
```bash
conda env update --prefix ./env --file environment.yml --prune
```