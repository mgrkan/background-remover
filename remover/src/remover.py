from abc import ABC, abstractmethod

# Abstract class for background remover
class BackgroundRemover(ABC):
    @abstractmethod
    def remove_background(self, input_path: str, output_path:str) -> str:
        pass

# Function to process images using different models.
def process_image(input_path: str, output_path: str, model: BackgroundRemover) -> str:
    return model.remove_background(input_path, output_path)