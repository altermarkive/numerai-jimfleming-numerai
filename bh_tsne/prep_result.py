import struct
import numpy as np
import pandas as pd
import os

df_train = pd.read_csv(os.getenv('TRAINING', '/workspace/output/train_data.csv'))
df_valid = pd.read_csv(os.getenv('VALIDATING', '/workspace/output/valid_data.csv'))
df_test = pd.read_csv(os.getenv('TESTING', '/workspace/output/test_data.csv'))

with open('result.dat', 'rb') as f:
    N, = struct.unpack('i', f.read(4))
    no_dims, = struct.unpack('i', f.read(4))
    print(N, no_dims)

    mappedX = struct.unpack('{}d'.format(N * no_dims), f.read(8 * N * no_dims))
    mappedX = np.array(mappedX).reshape((N, no_dims))
    print(mappedX)

    tsne_train = mappedX[:len(df_train)]
    tsne_valid = mappedX[len(df_train):len(df_train)+len(df_valid)]
    tsne_test = mappedX[len(df_train)+len(df_valid):]

    assert(len(tsne_train) == len(df_train))
    assert(len(tsne_valid) == len(df_valid))
    assert(len(tsne_test) == len(df_test))

    prefix = os.getenv('PREFIX', '/workspace/output/')
    save_path = '{}tsne_{}d_30p.npz'.format(prefix, no_dims)
    np.savez(save_path, train=tsne_train, valid=tsne_valid, test=tsne_test)
    print('Saved: {}'.format(save_path))

    # landmarks, = struct.unpack('{}i'.format(N), f.read(4 * N))
    # costs, = struct.unpack('{}d'.format(N), f.read(8 * N))
