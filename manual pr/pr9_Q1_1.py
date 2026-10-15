d = {'BOARD': 'StudentA', 'CO': 'StudentB', 'SEM': 'StudentC'}
del d['CO'];
for key, values in d.items():
    print(key);
d.clear();
for key,values in d.items():
    print(key)
del d;
for key,values in d.items():
    print(key)
