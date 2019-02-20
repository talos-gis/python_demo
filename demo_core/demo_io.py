read = open('demo_source.txt','r')
write = open('demo_dest.txt','w')
for line in read:
    if line.startswith('#'):
        continue
    if line.startswith('simon says:'):
        line = line[len('simon says:'):]
    line = line.strip()
    write.write(line+'\n')
read.close()  # don't forget to close your files
write.close()
