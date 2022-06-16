import os
import time
import argparse
import logging
from src.utils.common_utils import read_config_yaml,create_dirs
from src.utils.callbacks import create_and_save_tensorboard_callbacks, create_and_save_checkpointing_callbacks


logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format= '[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    filemode='a'    
)


def prepare_callbacks(config_path:str) -> None:
    """prepare and save callbacks as binary 
    
    Args:
        config_path: path to the yaml file
    """
    config = read_config_yaml(config_path)

    artifacts= config['artifacts']
    artifacts_dir= artifacts['ARTIFACTS_DIR']

    tensorboard_log_dir= os.path.join(artifacts_dir, artifacts['TENSORBOARD_ROOT_LOG_DIR'])

    checkpoint_dir= os.path.join(artifacts_dir, artifacts['CHECKPOINT_DIR'])

    callbacks_dir= os.path.join(artifacts_dir, artifacts['CALLBACKS_DIR'])

    create_dirs([tensorboard_log_dir, checkpoint_dir, callbacks_dir])

    create_and_save_tensorboard_callbacks(callbacks_dir, tensorboard_log_dir)

    create_and_save_checkpointing_callbacks(callbacks_dir, checkpoint_dir)



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Loads a yaml file and returns a dictionary')
    parser.add_argument('--config', '-c', default='configs/config.yaml',help='path to the yaml file')
    parsed_args= parser.parse_args()

    try:
        logging.info('\n********************************')
        logging.info('>>>>>stage03 started <<<<<')
        prepare_callbacks(config_path=parsed_args.config)
        logging.info('>>>>>stage03 completed and callbacks are prepared and saved as binary! <<<<<\n')

    except Exception as e:
        logging.error(f'Error: {e}')
