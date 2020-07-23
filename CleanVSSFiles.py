import os
import sys
import shutil

DELETE_FLAG = True #True-直接删除 | False-只打印删除文件路径
DELETE_VSSSCC = True
DELETE_SCC = True
DELETE_VSPSCC = True

def judge_path(path):
    files = os.listdir(path)
    
    for f in files:
        is_dir = False
        if os.path.isdir(os.path.join(path, f)):
            is_dir = True
        if DELETE_VSSSCC and f.lower().endswith('.vssscc') and not is_dir:
            if DELETE_FLAG:
                os.remove(os.path.join(path, f))
            print('Delete {0}'.format(os.path.join(path, f)))
            continue
        if DELETE_SCC and f.lower().endswith('.scc') and not is_dir:
            if DELETE_FLAG:
                os.remove(os.path.join(path, f))
            print('Delete {0}'.format(os.path.join(path, f)))
            continue
        if DELETE_VSPSCC and f.lower().endswith('.vspscc') and not is_dir:
            if DELETE_FLAG:
                os.remove(os.path.join(path, f))
            print('Delete {0}'.format(os.path.join(path, f)))
            continue
        if is_dir:
            judge_path(os.path.join(path, f))
        
print('Working Path: {0}'.format(sys.argv[1]))
try:
    judge_path(sys.argv[1])
except Exception as e:
    print(str(e))

os.system('pause')
