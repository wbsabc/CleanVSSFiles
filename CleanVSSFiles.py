import os
import sys
import shutil

DELETE_FLAG = True #True-直接删除 | False-只打印删除文件路径
DELETE_VSSSCC = True
DELETE_SCC = True
DELETE_VSPSCC = True

error_log = ''

def remove_file(path):
    global error_log
    try:
        if DELETE_FLAG:
            os.remove(path)
        print('Delete {0}'.format(path))
    except Exception as e:
        print(str(e))
        error_log = error_log + path + "\n"

def output_log():
    global error_log
    if error_log != '':
        print("\n\nFailed Path:\n")
        print(error_log)

def judge_path(path):
    files = os.listdir(path)
    
    for f in files:
        is_dir = False
        if os.path.isdir(os.path.join(path, f)):
            is_dir = True
        if DELETE_VSSSCC and f.lower().endswith('.vssscc') and not is_dir:
            remove_file(os.path.join(path, f))
            continue
        if DELETE_SCC and f.lower().endswith('.scc') and not is_dir:
            remove_file(os.path.join(path, f))
            continue
        if DELETE_VSPSCC and f.lower().endswith('.vspscc') and not is_dir:
            remove_file(os.path.join(path, f))
            continue
        if is_dir:
            judge_path(os.path.join(path, f))

working_path = sys.argv[1]
if working_path.endswith('"'):
    working_path = working_path.replace('"', '\\')
print('Working Path: {0}\n'.format(working_path))
try:
    judge_path(working_path)
    output_log()
except Exception as e:
    print(str(e))

os.system('pause')
