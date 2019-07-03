import pymysql
from config import config

def get_coon():
    coon = pymysql.connect(host=config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           password=config.db_password,
                           db=config.db,
                           charset='utf8')
    return coon

def db_query(sql):
    config.logging.debug(sql)
    # print(sql)
    c = get_coon()#调用上面的连接
    cur=c.cursor()#建立游标
    cur.execute(sql)
    r=cur.fetchall()
    config.logging.debug(r)
    # print(r)
    cur.close()
    c.close()
    return r

def db_change(sql):  #修改数据库时，如果sql出错了可以回滚
    # print(sql)
    try:
        c=get_coon()
        cur=c.cursor()
        cur.execute(sql)
        c.commit()#提交修改
    except Exception as e:
        config.logging.error(repr(e))   #打印错误信息
        e.rollback() # 回滚修改
    finally:
        cur.close()
        c.close()


#查询退租时间
def check_updatesurrendertime(contract_id):
    time = db_query("select surrender_time from contract where contract_id='%d'" % contract_id)
    # "".join(time)
    return time

#查询合同周期
def check_contractcycle(contract_id):
    contract_cycle=db_query("select contract_cycle from contract where contract_id='%d'" % contract_id)
    return contract_cycle

#查询甲方信息数据
def check_landlord(apartment_id):
    landlord=db_query("select apartment_id,landlord_type,landlord_title,card_type,card_name from records_landlord_info where apartment_id='%d'" % apartment_id)
    return landlord

#查询权证信息数据
def check_ownership(apartment_id):
    ownership=db_query("select address,cert_no,owner_name,owner_type from records_ownership_info where apartment_id='%d'" % apartment_id)
    return ownership

#查询权证id
def check_ownershipId(apartment_id):
    ownershipId=db_query("select ownership_id from records_ownership_info where apartment_id='%d'" % apartment_id)
    return ownershipId

#查询权证信息是否存在
def check_ownership_exist(apartment_id):
    r = db_query("select * from records_ownership_info where apartment_id='%d'" % apartment_id)
    if r:
        return True
    return False

#删除权证信息
def delete_ownership(apartment_id):
    db_change("delete from records_ownership_info where apartment_id='%d'" % apartment_id)


if __name__=='__main__':
    # print(check_updatesurrendertime(10))
    # print(check_contractcycle(10)[0][0])
    # print(check_landlord(18))
    print(check_ownership(17))
    print(check_ownershipId(17))


