from PIL import Image

import torchvision.transforms as transforms
from torch.utils.data import DataLoader

from .artdata import ArtDataset

class ArtLoader:
    def __init__(self, DATA_DIR='',
                 crop_size=256,
                 batch_size=1,
                 num_workers=1,
                 mode='train'):
        
        self.DATA_DIR = DATA_DIR
        self.crop_size = crop_size
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.mode = mode
        
        
    def load_data(self):
        
        if self.mode == 'train':
            train_transforms_ = [
                transforms.Resize(int(self.crop_size*1.12), Image.BICUBIC),
                transforms.RandomCrop(self.crop_size),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ]
            train_dataset = ArtDataset(
                DATA_DIR = self.DATA_DIR,
                transforms_ = train_transforms_,
                unaligned = True,
                mode = 'train'
            )
            
            train_loader = DataLoader(train_dataset, 
                            batch_size=self.batch_size, 
                            shuffle=True,
                            num_workers=self.num_workers)
            return train_loader
        elif self.mode == 'test':
            test_transforms_ = [
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ]
        
            test_dataset = ArtDataset(
                DATA_DIR = self.DATA_DIR,
                transforms_ = test_transforms_,
                unaligned = False,
                mode = 'test'
            )
        
        
        
            test_loader = DataLoader(test_dataset, 
                                batch_size=self.batch_size, 
                                shuffle=False,
                                num_workers=self.num_workers)
            
            return test_loader
        
         