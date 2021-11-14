# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymssql
from itemadapter import ItemAdapter

def DBinit():
    try:
        ##连接数据库 user用户名password密码database数据库名
        con = pymssql.connect(host='localhost', user='lzx', password='lzx', database='lzx_')
        cursor = con.cursor()
        ##删除表
        cursor.execute('drop table stock')
        con.commit()
    except Exception as ex:
        print(ex)
    try:
        ##创建表
        cursor.execute(
            "create table stock (id varchar(20),bStockNo varchar(20),bName varchar(20),bLatestquo varchar(20),"
            "bFluctuation varchar(20),bRiseandfall varchar(20),bTurnovernum varchar(20),bTurnoveprice varchar(20)"
            ",bAmplitude varchar(20),bHighest varchar(20),bLowest varchar(20),bToday varchar(20),bYesterday varchar(20))")
        ##提交并关闭
        con.commit()
        con.close()
    except Exception as ex:
        print(ex)
DBinit()
class DongfangSpiderPipeline:
    def process_item(self, item, spider):
        try:
            # 链接数据库
            self.con = pymssql.connect(host='localhost', user='lzx', password='lzx', database='lzx_')
            self.cursor = self.con.cursor()
            ##插入数据
            self.cursor.execute(
                "INSERT INTO stock(id ,bStockNo ,bName ,bLatestquo ,bFluctuation "
                ",bRiseandfall ,bTurnovernum ,bTurnoveprice "
                ",bAmplitude ,bHighest ,bLowest ,bToday ,bYesterday ) "
                "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %
                ( item['id'],item['bStockNo'],item['bName'],item['bLatestquo'],
                  item['bFluctuation'],item['bRiseandfall'],item['bTurnovernum'],
                  item['bTurnoveprice'],item['bAmplitude'],item['bHighest'],
                  item['bLowest'],item['bToday'],item['bYesterday']))
            ##提交
            self.con.commit()
            self.con.close()
            print("_____________________________")
        except Exception as ex:
            print(ex)
        return item
