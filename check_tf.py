import tensorflow as tf

if len(tf.config.list_physical_devices('GPU')) > 0:
    print("GPU used with TF", tf.test.gpu_device_name())
else:
    print("TF cannot find GPU")
    exit(1)

