def change_relu_2_silu():
    model = torch.load('weights/best-truncate.pt')
    sub_model1 = model.modified_layers.net
    sub_model2 = model.modified_layers.fpn
    
    # change relu in net of backbone
    for name, module in sub_model1.named_children():
        for i in range(len(module)):
            if module[i].__class__.__name__ == 'Conv':
                setattr(module[i], 'relu', torch.nn.ReLU(inplace=True))
                # module[i].relu = torch.nn.ReLU(inplace=True)
            elif(module[i].__class__.__name__ == 'CSP'):
                # transfer conv1 conv2 conv3
                module[i].conv1.relu = torch.nn.ReLU(inplace=True)
                module[i].conv2.relu = torch.nn.ReLU(inplace=True)
                module[i].conv3.relu = torch.nn.ReLU(inplace=True)
                # transfer res_m
                for k in range(len(module[i].res_m)):
                    for j in range(len(module[i].res_m[k].res_m)):
                        module[i].res_m[k].res_m[j].relu = torch.nn.ReLU(inplace=True)
            elif(module[i].__class__.__name__ == 'SPP'):
                module[i].conv1.relu = torch.nn.ReLU(inplace=True)
                module[i].conv2.relu = torch.nn.ReLU(inplace=True)

    # change relu in fpn of neck
    for name, module in sub_model2.named_children():
        if(module.__class__.__name__ == 'CSP'):
            # transfer conv1 conv2 conv3
            module.conv1.relu = torch.nn.ReLU(inplace=True)
            module.conv2.relu = torch.nn.ReLU(inplace=True)
            module.conv3.relu = torch.nn.ReLU(inplace=True)
            # transfer res_m
            for i in range(len(module.res_m)):
                for j in range(len(module.res_m[i].res_m)):
                    module.res_m[i].res_m[j].relu = torch.nn.ReLU(inplace=True)
        elif(module.__class__.__name__ == 'Conv'):
            module.relu = torch.nn.ReLU(inplace=True)

    # for name, module in sub_model1.named_children():
    #     if(module.__class__.__name__ != 'Upsample'):
    #         for i in range(len(module)):
    #             if module[i].__class__.__name__ == 'Conv':
    #                 print(module[i])

    # for name, module in sub_model2.named_children():
    #     print(module)
    torch.save(model, 'weights/best-truncate-relu.pt')
    print(model)
