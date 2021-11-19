conda env create -f environment.yml --force

CONDA_PATH=$(conda info | grep -i 'base environment' | awk '{print $4}')
source $CONDA_PATH/etc/profile.d/conda.sh

conda activate ABD
conda install -c anaconda ipykernel -y
python -m ipykernel install --user --name=ABD
mkdir Model
mkdir Data
jupyter notebook