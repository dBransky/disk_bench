import os
base = 4096
for i in range(0, 19):
    size = base*2**i
    os.system(f'dd if=/dev/urandom of=/scratch/tmp/tempfile.{size} bs={size} count=1')
    print('finished file of size ', size)