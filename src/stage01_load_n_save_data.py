import os
import argparse
from tqdm import tqdm
from src.utils.common_utils import read_yaml,create_dirs,copy_files
import logging


logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format= '[%(asctime)s: %(levelname)s: %(modules)s]: %(message)s',
    filemode='a'
)

def get_data(config_path:str) -> None:
    """
       get the data from source dir to local dir by reading config from config.yaml
    
    Args:
        config_path: path to the yaml file
    """
    config = read_yaml(config_path)

    source_data_dirs= config['source_data_dirs']
    local_data_dirs= config['local_data_dirs']

    N= len(source_data_dirs)
    for source_data_dir, local_data_dir in tqdm(
        zip(source_data_dirs, local_data_dirs),
        total=N,
        desc='copying data from source dir to local dir',
        colour='green'):

        create_dirs([local_data_dir])
        copy_files(source_data_dir, local_data_dir)



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Loads a yaml file and returns a dictionary')
    parser.add_argument('--config', '-c', default='configs/config.yaml',help='path to the yaml file')
    parsed_args= parser.parse_args()

    try:
        logging.info('\n********************************')
        logging.info('>>>Loading configuration to start stage one.<<<<<')
        get_data(config_path=parsed_args.config)
        logging.info('>>>stage one completed and data got saved in local dir from remote dir! <<<\n')

    except Exception as e:
        logging.error(f'Error: {e}')

