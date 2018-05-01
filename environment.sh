# Create an environment:
#conda create --name template python=3.6

# Active the environment:
source activate template

# Create requirements.txt:
conda list --explicit > requirements.txt

# Create environment from requirements.txt:
#conda env create template2 --file requirements.txt
