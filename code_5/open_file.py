

import sys
import errno 

if len(sys.argv) != 2:
    print('Usage: %s input_filename' % __file__)
    sys.exit()
    
try:
    with open(sys.argv[1], 'r', encoding='utf-8') as fin:
        for i, line in enumerate(iter(fin.readline, '\n')):
            print('%03d  %s' % (i+1, line), end='')
except OSError as e:
    if e.errno == errno.ENOENT:
        print('File %s does not exist.' % sys.argv[1])
    elif e.errno == errno.EACCES:
        print('No permission to read the file %s.', sys.argv[1])
    elif e.errno == errno.EISDIR:
        print('%s is not a file.' % sys.argv[1])
except UnicodeDecodeError:
    print('%s is not a UTF-8-encoded text file.' % sys.argv[1])
except Exception as e:
        print('Unknown Error: ' + str(e))

#### 
# try:
    # with open(sys.argv[1], 'r', encoding='utf-8') as fin:
        # for i, line in enumerate(fin):
            # print('%03d  %s' % (i+1, line), end='')
# except FileNotFoundError:
    # print('File %s does not exist.' % sys.argv[1])
# except PermissionError:
    # print('No permission to read the file %s.', sys.argv[1])
# except IsADirectoryError:
    # print('%s is not a file.' % sys.argv[1])
# except UnicodeDecodeError:
    # print('%s is not a UTF-8-encoded text file.' % sys.argv[1])
# except Exception as e:
        # print('Unknown Error: ' + str(e))
