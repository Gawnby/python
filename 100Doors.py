doors=['O']*100
skip=0
while(skip<100):
  door=skip
  print(door+1,end='. run:\n')
  while(door<100):
    if(doors[door]=='O'):
      doors[door]='X'
    else:
      doors[door]='O'
    missed=door-skip
    while(missed<door):
      print(' ',end='')
      missed=missed+1
    print(doors[door],end='')
    door=door+skip+1
  print('\n')
  skip=skip+1

print('Above you see the doors toggled each run. \nThe following doors remained open: ',end='')
for door in [door for door,open in enumerate(doors) if open=='O']:
  print(door+1,end='. ')
print('\n')

