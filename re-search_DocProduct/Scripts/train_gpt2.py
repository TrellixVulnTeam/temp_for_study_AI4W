from gpt_2 import gpt2
import os

import tensorflow as tf


def train_gpt2(
        csv_path='gpt2_train_data/bertffn_crossentropy.csv',
        steps=100000,
        batch_size=1):
    tf.compat.v1.disable_v2_behavior()
    if not os.path.exists('models/117M'):
        gpt2.download_gpt2()

    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess, csv_path, steps=steps, batch_size=batch_size)
