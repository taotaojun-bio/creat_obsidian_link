from pathlib import Path
import os



def list_all(directory,base_path):
    for dirpath, dirnames, filenames in os.walk(directory):
        # 跳过名为'.obsidian'和'图床'的目录，可自行增加忽略的文件夹
        if '.obsidian' in dirnames:
            dirnames.remove('.obsidian')
        if '图床' in dirnames:
            dirnames.remove('图床')

        #防止链接文件保存的地址也被读取
        folder_name = Path(base_path).name
        if folder_name.endswith('/'):
            folder_name = folder_name.rstrip('/')
        if folder_name in dirnames:
            dirnames.remove(folder_name)


        base_dir_name = os.path.basename(dirpath)
        if base_dir_name=="Obsidian Vault":
            continue
        with open(base_path+base_dir_name+".md", 'w', encoding='utf-8') as file:
            for dirname in dirnames:
                file.write(f"[[{dirname}]]")
            for filename in filenames:
                file.write(f"[[{filename}]]")





if __name__=="__main__":
    directory=input('请输入obsidian笔记根目录，留空则默认软件位置：')
    if directory=="":
        directory =os.getcwd()
    base_path=input('请输入链接文件存储路径，留空则默认链接页：')    
    if base_path=="":
        base_path=directory+"/链接页/"
    else:
        if base_path[-1]!='/':
            base_path=base_path+'/'
        base_path=directory+"/"+base_path
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    list_all(directory,base_path)