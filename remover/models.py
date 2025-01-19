from rembg import remove
from transparent_background import Remover
from PIL import Image
from remover import BackgroundRemover

class RembgModel(BackgroundRemover):
    def remove_background(self, input_path, output_path):
        #Read input image
        with open(input_path, 'rb') as i:
            #Open output image
            with open(output_path, 'wb') as o:
                input = i.read()
                #Remove background
                output = remove(input)
                #Write to file
                o.write(output)
        return output_path
    
class InspyrenetModel(BackgroundRemover):
    def remove_background(self, input_path, output_path):
        # Load model
        remover = Remover(mode='fast', jit=True,) # default setting
        # Usage for image
        img = Image.open(input_path).convert('RGB') # read image
        out = remover.process(img) # default setting - transparent background
        out.save(output_path) # save result
        return output_path