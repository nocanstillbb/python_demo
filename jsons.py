import json
from log import Logger
import fileinput
l = Logger();

print("\n>>>>  json object序列化为json字符串")
jsonobj = { "prop1": 1 , "proper2": "2" }
jsonstr = json.dumps(jsonobj,indent=4);#,separators=(";","=")); #separators 可以设置分隔符,一般用默认
print(jsonstr)

print("\n>>>>  json object写为json文件")
with open("savejson.json",'w') as file:
    json.dump(jsonobj,file,indent=4)



class  hbbclass():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

print("\n>>>>  json.dumps+方法把实例序列化为json字符串")
def encode_json(obj):
    return {"name": obj.name, "age": obj.age}
print(json.dumps(hbbclass("hbb",32),default=encode_json))#传入default一个方法用于转换

print("\n>>>>  json.dumps+lambda把实例序列化为json字符串")
print(json.dumps(hbbclass("hbb",32),default=lambda obj: { "name": obj.name, "age": obj.age } ))#传入default一个方法用于转换



print("\n>>>>  JSONEncoder子类把实例序列化为json字符串")
from json import JSONEncoder
class hbbClass2json(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,hbbclass):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__:True}
print(json.dumps(hbbclass("hbb",32),cls=hbbClass2json))#传入继承自jsonencoder的类
print(hbbClass2json().encode(hbbclass("hbb",32)))# 直接用jsonencode子类的方法
        

jsonstr = hbbClass2json().encode(hbbclass("hbb",32))




print("\n>>>>  反序列化为dict")
jsondic = json.loads(jsonstr);
print(type(jsondic))#结果为dict类型
print(jsondic)



print("\n>>>>  反序列化为实例")
def  decode_json(jsondict):
    if(hbbclass.__name__ in jsondict):
        return hbbclass(name=jsondict["name"],age=jsondict["age"])
    return jsondict

obj = json.loads(jsonstr,object_hook=decode_json)
print(type(obj))
print(obj)