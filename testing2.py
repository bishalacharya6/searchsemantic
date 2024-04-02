import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"cuDNN version: {torch.backends.cudnn.version()}")
    print(f"GPU device: {torch.cuda.get_device_name()}")
    print(f"Available GPU memory: {torch.cuda.get_device_properties(torch.cuda).total_memory / (1024 ** 3)} GB")



