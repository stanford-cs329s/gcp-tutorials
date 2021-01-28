import torch

if torch.cuda.is_available():
    print("GPU used with Torch", torch.cuda.get_device_name(0))
else:
    print("Torch cannot find GPU")
    exit(1)

