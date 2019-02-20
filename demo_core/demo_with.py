with open('demo_source.txt', 'r') as read, \
        open('demo_dest.txt', 'w') as write:
    for line in read:
        if line.startswith('#'):
            continue
        if line.startswith('simon says:'):
            line = line[len('simon says:'):]
        line = line.strip()
        write.write(line + '\n')
