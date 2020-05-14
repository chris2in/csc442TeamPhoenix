import subprocess

for i in range(10):
    for o in range(10):
        subprocess.call(['python3 STEG.py -r -b -o{} -i{} -w2.txt > {}S'.format(2**i,2**o,str(i*100+o)) ],shell=True)
        