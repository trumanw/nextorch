name = 'nextorch'
__version__ = '0.1.0'

import torch
# use a GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dtype = torch.float
torch.set_default_dtype(dtype)


