conda env create -f environment.yml --force
CALL conda.bat activate ABD
conda install -c anaconda ipykernel -y
python -m ipykernel install --user --name=ABD