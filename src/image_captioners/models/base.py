from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union
from PIL import Image
import torch

class BaseModel(ABC): 
    
    @abstractmethod
    def load_model(self) -> None:
        pass
    
    @abstractmethod
    def caption_images(self, images: Union[List[Image.Image], Image.Image], **kwargs) -> List[str]:
        pass 
    
    @abstractmethod 
    def model_info(self) -> Dict: 
        pass 
    
class BaseProcessor(ABC): 
    
    @abstractmethod
    def load_processor(self) -> None:  
        pass
    
    @abstractmethod
    def preprocess(self, images: Union[List[Image.Image], Image.Image]) -> torch.Tensor:
        pass
    
    @abstractmethod
    def postprocess(self, outputs: torch.Tensor) -> Union[str, List[str]]:
        pass
    
        