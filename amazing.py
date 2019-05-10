import sys
greets = ['World']
# if we're given a command-line argument, read it as a file and greet
# those people
if len(sys.argv) > 1:
    for filename in sys.argv[1:]:
        greets.extend([line for line in open(filename).read().split('\n')
                       if len(line)])
for g in greets:
    print('Hello %s!' % g)
