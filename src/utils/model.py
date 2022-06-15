from distutils.log import info
from email.mime import base
import os
import io
import logging
from pickletools import optimize
from numpy import true_divide
import tensorflow as tf
from tensorflow.python.keras.backend import flatten


def _get_model_summary(model):
    with io.StringIO() as stream:
        model.summary(print_fn=lambda x: stream.write(x + '\n'))
        return stream.getvalue()

def get_VGG16_model(input_shape:tuple, model_path:str) -> tf.keras.models.Model:
    """saves and returns the base model extracted from VGG16 model

    Args:
        input_shape(str): shape of the input image
        model_path(str): path to save the model

    Returns:
        model(tf.keras.models.Model): base model extracted from VGG16 model
    """
    model= tf.keras.applications.vgg16.VGG16(
            input_shape= input_shape,
            weights= 'imagenet',
            include_top= False
    )

    logging.info(f'base model summary:\n{_get_model_summary(model)}')
    model.save(model_path)
    logging.info(f'VGG16 base model saved successfully to {model_path}')
    return model


def prepare_full_model(
    base_model, 
    learning_rate, 
    CLASSES=2, 
    freeze_all= True, 
    freeze_till=None) -> tf.keras.models.Model:
    """prepares the complete transfer learning model architecture

    Args:
        base_model(tf.keras.models.Model): base model extracted from VGG16 model
        learning_rate(float): learning rate for the model
        CLASSES(int, optional): number of classes to train in the dataset, Default is 2.
        freeze_all(bool, optional): if True, all layers are frozen to make them untrainable, else only the last layer is frozen, Default is True.
        freeze_till(int, optional): if not None, the layers till the given layer are frozen, else all layers are frozen, Default is None.

    Returns:
        model(tf.keras.models.Model): full architecture of the model ready to train
    """

    if freeze_all:
        for layer in base_model.layers:
            layer.trainable = False
    elif (freeze_till is not None) and (freeze_till > 0):
        for layer in base_model.layers[:-freeze_till]:
            layer.trainable = False
        
    ## add our layers to the base model

    flatten_in= tf.keras.layers.Flatten()(base_model.output)

    prediction= tf.keras.layers.Dense(
        units= CLASSES,
        activation= 'softmax'
    )(flatten_in)

    full_model = tf.keras.models.Model(
        inputs = base_model.input,
        outputs = prediction
    )

    full_model.compile(
        optimizer= tf.keras.optimizers.Adam(learning_rate= learning_rate),
        loss= tf.keras.losses.CategoricalCrossentropy(),
        metrics= ['accuracy']
    )

    logging.info(f'custom model is compiled and ready to be trained')

    logging.info(f'full model summary:\n{_get_model_summary(full_model)}')
    return full_model

# def load_full_model(untrained_full_model_path:str) -> tf.keras.models.Model:
#     model= tf.keras.models.load_model(untrained_full_model_path)
#     logging.info(f'untrained model is read from {untrained_full_model_path}')
#     logging.info(f'untrained model summary:\n{_get_model_summary(model)}')
#     return model

# def
#     """loads the full model from the untrained and trained model paths


#     """
