import os
import yaml
import logging
from tqdm import tqdm
import shutil


def read_config_yaml(file_path:str) -> dict:
    """
    Loads a yaml file and returns a dictionary

    Args:
        file_path: path to the  yaml file

    Returns:
        A dictionary containing the yaml file's contents
    """
    with open(file_path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f'content from {file_path} read successfully!')
    return content


def create_dirs(dir_paths:list) -> None:
    """
    Creates directories if they do not exist    
    Args:
        dir_paths: list of directories to be created
    """
    for dir_path in dir_paths:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            logging.info(f'{dir_path} created successfully!')

def copy_files(source_data_dir:str, local_data_dir:str) -> None:
    """
    Copies files from source dir to dest dir
    Args:
        source_dir: path to the source dir  
        dest_dir: path to the destination dir
    """
    list_of_files= os.listdir(source_data_dir)
    N= len(list_of_files)
    for file_name in tqdm(
        list_of_files,
        total=N,
        desc=f'copying files from source dir to dest dir',
        colour='green'
    ):
        source_file_path = os.path.join(source_data_dir, file_name)
        dest_file_path = os.path.join(local_data_dir, file_name)
        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path, dest_file_path)
            
    logging.info(f'{source_file_path} copied successfully to {dest_file_path}')

