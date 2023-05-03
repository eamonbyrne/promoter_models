import setuptools

setuptools.setup(
    name='promoter_modelling',
    version='0.1',
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=["numpy", "pandas", "argparse", "wandb", "h5py", "tqdm", "scipy", "scikit-learn", "matplotlib", "seaborn",\
                      "torch==2", "torchvision", "torchmtl==0.1.8", "lightning", \
                      "kipoiseq", "pyfaidx", "joblib", "fastsk", "editdistance", "fastdist", "numba", \
                      "transformers", "tensorly", "tensorly-torch", "odfpy"]
)