conda env remove -n "csci1470"
conda env create -n "csci1470" -f env_setup/Other/csci1470.yml

## Install new environment.
python3 -m ipykernel install --user --name csci1470 --display-name "DL-S24 (3.10)"
