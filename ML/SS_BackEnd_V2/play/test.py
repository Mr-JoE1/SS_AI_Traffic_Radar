import torch 
import numpy as np


tn = torch.rand(3,3)
print(f"tn device: {tn.device}")
if torch.cuda.is_available():
    tn = tn.to('cuda')
    print(f"tn device: {tn.device}")
else:
    print("cuda not available !")