import pycuda.driver as cuda
cuda.init()
device = cuda.Device(0)  # Assuming GPU 0
num_cores = device.get_attribute(cuda.device_attribute.MULTIPROCESSOR_COUNT) * \
            cuda.Device(0).get_attribute(cuda.device_attribute.MULTIPROCESSOR_CORE_COUNT)
print("Number of CUDA Cores:", num_cores)
