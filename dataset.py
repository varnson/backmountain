
import os

DSPATH='/data/test/ds'

class DataSet(object):
    def create_dataset(self, name):
        if(not name): 
            return "ds name error"
        if(not os.path.isdir(DSPATH)):
            return "ds path error"
        if(os.path.isdir(DSPATH+"/"+name)):
            return "ds "+name+" already exist"
        os.mkdir(DSPATH+"/"+name)

        return name

    def list_dataset(self):
        if(not os.path.isdir(DSPATH)):
            return "ds path error"
        dslist=os.listdir(DSPATH)
        return dslist

    def info_dataset(self, name):
        if(not name): 
            return "ds name error"
        if(not os.path.isdir(DSPATH)):
            return "ds path error"
        if(not os.path.isdir(DSPATH+"/"+name)):
            return "ds "+name+" not exist"
        if(not os.path.isfile(DSPATH+"/"+name+"/ds.json")):
            return "ds "+name+": def not exist"
        file = open(DSPATH+"/"+name+"/ds.json", 'r') 
        text=""
        try:
            text = file.read()  # 结果为str类型
        finally:
            file.close()
        return text

    def add_data(self, name, data):
        if(not name): 
            return "ds name error"
        if(not os.path.isdir(DSPATH)):
            return "ds path error"
        if(not os.path.isdir(DSPATH+"/"+name)):
            return "ds "+name+" not exist"
        file = open(DSPATH+"/"+name+"/data.json", 'a')
        count=file.write(data)
        file.write(os.linesep)
        file.close()

        return count


dataset = DataSet()
