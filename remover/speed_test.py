from remover import process_image
from models import RembgModel, InspyrenetModel
import time

def timer(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return (f'{args[-1]} took {end-start} seconds')

rembg_time = timer(process_image, 'sample1.jpeg', 'output1.png', RembgModel())
inspyrenet_time = timer(process_image,'sample1.jpeg', 'output2.png', InspyrenetModel())
print(rembg_time, inspyrenet_time)