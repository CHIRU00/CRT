fam={
    'charley':
    {'sam':{'boxy','rosy'},
     'nila':{'pepsi'}},
    'devi':
    {'Tommy':{'Tony'},
     'Timmt':{"Hamster"},
     'Tammy':{"hamster"}},
    'carlos':
    {'diago':'cat','Ferret':'Fox'}
    }
for p,c in fam.items():
    print(f"{p} has {len(c)} kids(s):")
    print(f"{',and '.join([str(ch) for ch in [*c]])}")
print(fam[nila])
    
