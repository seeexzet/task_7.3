file_list = ['1.txt', '2.txt', '3.txt']
len_file_list = len(file_list)

len_file = {}

for name in file_list:
    file = open(name, 'rt', encoding='utf-8')
    len_file[name] = len(file.readlines())
    file.close()

print(len_file)
file_target = open('target.txt', 'wt', encoding='utf-8')

for k in range(len_file_list):
    min_val = min(len_file.values())
    min_dict = {k: v for k, v in len_file.items() if v == min_val}
    name = list(min_dict.keys())[0]
    file = open(name, 'rt', encoding='utf-8')
    result = file.readlines()
    file_target.writelines([name, '\n', str(min_val), '\n'])
    file_target.writelines(result)
    file_target.write('\n')
    file.close()
    del(len_file[name])

file_target.close()


