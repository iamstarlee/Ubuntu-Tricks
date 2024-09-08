import torch
import torch.nn as nn

class ModifiedModel(nn.Module):
    def __init__(self, original_model):
        super(ModifiedModel, self).__init__()
        self.modified_layers = nn.ModuleDict()
        
        for name, module in original_model.named_children():
            if not name.startswith('head'):
                self.modified_layers[name] = module
                
    def forward(self, x):
        for name, layer in self.modified_layers.items():
            x = layer(x)
        return x

def truncate_model():
    model = torch.load('weights/best.pt')

    modified_model = ModifiedModel(model['model'])

    for name, module in modified_model.named_parameters():
        print(name)
    torch.save('weights/best-tuncate.pt', modified_model)
   
