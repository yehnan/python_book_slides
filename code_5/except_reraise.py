

def reraise():
    try:
        int('!@#')
    except ValueError as e:
        raise RuntimeError('parse error') from e
        # print(exc)
        
reraise()

# try:
    # reraise()
# except RuntimeError as e:
    # print(e.__cause__)

