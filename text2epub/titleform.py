import os 

def titleform():
    g=os.walk('./')
    for path,dir_list,file_list in g:  
        for file_name in file_list: 
            if os.path.splitext(file_name)[1]=='.txt':
                title=file_name.split('_')[2].split('.')[-2]
                data=[]
                with open(file_name, "r",encoding='UTF-8') as f:
                    data = f.readlines()
                with open(file_name,"w",encoding='utf-8') as f:
                    f.write(title+'\n')
                    for line in data:
                        f.write(line)

if __name__=="__main__":
    titleform()