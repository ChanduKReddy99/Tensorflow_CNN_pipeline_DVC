from setuptools import setup

with open('README.md', 'r', encoding= 'utf-8') as f:
    long_description = f.read()

REPO_NAME= 'DVC_TF_CNN_Pipeline'
AUTHOR_USER_NAME= 'ChanduKReddy99'
AUTHOR_EMAIL= 'chanduk.amical@gmail.com'
URL= f'https://github.com/ChanduKReddy99/Tensorflow_CNN_pipeline_DVC'
SRC_REPO= 'src'
REQUIREMENTS_LIST= [
    'dvc',
    'tensorflow',
    'tqdm',
    'joblib',
]


setup(
    name=SRC_REPO,
    version='0.0.2',
    description='A DL pipeline for DVC',
    long_description= long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    url= URL,
    packages=[SRC_REPO],
    python_requires= '>=3.6',
    license= 'MIT',
    install_requires= REQUIREMENTS_LIST
)
