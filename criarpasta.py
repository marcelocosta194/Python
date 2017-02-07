import os
import errno
import sys

#Exemplo só escreve se não existir o arquivo.
#Caso exista não escreve
#flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

#desktop_file = os.path.expanduser("~/Desktop/myfile.txt")

#try:
#    file_handle = os.open(desktop_file, flags)
#except OSError as e:
#    if e.errno == errno.EEXIST:  
#        pass
#    else:  
#        raise
#else:  
#    with os.fdopen(file_handle, 'w') as file_obj:
#        file_obj.write("Look, ma, I'm writing to a new file!")


#-------------------------------------------------------------------------

#Esse excemplo escreve no arquivo
desktop_file = os.path.expanduser("~/Desktop/myfile.txt")
with open(desktop_file, 'w') as f:
    f.write('Some important content2!\n')