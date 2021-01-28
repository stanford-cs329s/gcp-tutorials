import tensorflow as tf

if tf.test.is_gpu_available():
    print("GPU used with TF", tf.test.gpu_device_name())
else:
    print("TF cannot find GPU")
    exit(1)

