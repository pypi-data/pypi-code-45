import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
dblist = myclient.list_database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")
collist = mydb.list_collection_names()

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)

myquery = {"name": {"$regex": "^R"}}
newvalues = {"$set": {"alexa": "123"}}
mycol.update_one(myquery, newvalues)
# x = mycol.update_many(myquery, newvalues) # 修改所有

# myquery = {"name": "RUNOOB"}
# mycol.delete_one(myquery)  # 删除单个
# mycol.delete_many({})  # 删除所有
# mycol.drop()  # 删除一个集合

for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)
myquery = {"name": {"$regex": "^R"}}  # name 字段中第一个字母为 "R"
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# mydoc = mycol.find().sort("alexa")  # 升序
mydoc = mycol.find().sort("alexa", -1)  # 降序
for x in mydoc:
    print(x)
