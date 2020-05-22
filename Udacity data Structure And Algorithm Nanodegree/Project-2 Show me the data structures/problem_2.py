import os


def findFiles(suff, path, file=[]):
    # Function to find all files  under a directory (and all directories beneath it) that end with ".c"

    local = suff  # Storing suffix into a local variabl
    if path:
        local = suff + '/' + path
    for i in os.listdir(local):
        local1 = local + '/' + i

        if os.path.isfile(local1) and local1.endswith(".c"):
            # Checking for file ends with ".c"
            file.append(local1)


        elif os.path.isdir(local1):
            file = findFiles(local, i, file)
    # Returning back the list
    return file


a=findFiles('.', 'testdir')
print(*a,sep='\n')

b=findFiles('.', '')

print(*b,sep='\n')


