pre_model = "./results/model_2-9.pth"
dict = torch.load(pre_model)
for key in list(dict.keys()):
    if key.startswith('decoder1'):
        del dict[key]
torch.save(dict, './model_deleted.pth')
# # #验证修改是否成功
changed_dict = torch.load('./model_deleted.pth')
for key in dict.keys():
    print(key)

# https://blog.51cto.com/sddai/3015084
