import tensorflow as tf
import os
import joblib
import logging
from src.utils.common_utils import get_timestamp

def create_and_save_tensorboard_callbacks(callbacks_dir:str, tensorboard_log_dir:str) -> None:
    """
    Creates and saves tensorboard callbacks as binary for later use

Args:
    callbacks_dir(str): path to the callbacks dir
    tensorboard_log_dir(str): path to the tensorboard log dir
    """
    unique_name = get_timestamp('tb_logs')
    tb_running_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir = tb_running_log_dir)

    tb_callback_filepath = os.path.join(callbacks_dir, 'tensorboard_cb.cb')
    joblib.dump(tensorboard_callback, tb_callback_filepath)

    logging.info(f'tensorboard call back is saved at {tb_callback_filepath} as binary file')


def create_and_save_checkpointing_callbacks(callbacks_dir:str, checkpoint_dir:str) -> None:
    """
    Creates and saves checkpointing callbacks 
Args:
    callbacks_dir(str): path to the callbacks dir
    checkpoint_dir(str): path to the checkpoint dir
    """

    checkpoint_file = os.path.join(checkpoint_dir, 'chkpt_model.h5')
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_file, save_best_only=True)

    checkpoint_callback_filepath = os.path.join(callbacks_dir, 'checkpoint_cb.cb')
    joblib.dump(checkpoint_callback, checkpoint_callback_filepath)

    logging.info(f'checkpoint call back is saved at {checkpoint_callback_filepath} as binary file')

def get_callbacks(callbacks_dir_path:str) -> list:
    """load and save call backs from callbacks dir
Args:
    callbacks_dir(str): path to the callbacks dir
Returns:
    list: list of callbacks for training
    """
    tb_callback_filepath = [os.path.join(callbacks_dir_path, pickle_file) for pickle_file in os.listdir(callbacks_dir_path) if pickle_file.endswith('.db')]  
    callbacks = [
        joblib.load(path) for path in tb_callback_filepath
    ]

    logging.info(f'saved callbacks are loaded and now they are ready to be used')
    return callbacks
    