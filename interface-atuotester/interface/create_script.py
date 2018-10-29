#encoding=utf-8
from utils.db_handler import DB
from utils.static_final import *

def new_file(apiInfo, api_case_list):
    print apiInfo
    # 新建脚本文件
    with open(SCRIPT_PATH + "\\" + apiInfo[1] +  "_test.py", "w") as fp:
        fp.write(code_head + "\n")
        if apiInfo[5] == 1:
            # 表示需要连接数据库
            fp.write(class_head_db %(apiInfo[1].title(), apiInfo[0], apiInfo[2]))
        else:
            fp.write(class_head %(apiInfo[1].title(),apiInfo[0],apiInfo[2]))
        for idx, case in enumerate(api_case_list, 1):
            param_code = ""
            if case[3]:
                # 写入获取依赖数据的方法
                param_code = '''payload = self.dbd.param_complete(%s, %s)''' %(eval(case[2]), eval(case[3]))
            else:
                param_code = '''payload = %s''' %case[2]
            store_code = ""
            if case[6]:
                # 写入存储依赖数据的方法"
                store_code = '''self.dbd.store_data(%s, %s, %s, %s, %s)''' %(int(case[0]), int(case[1]), case[6], case[2] if case[2] else None, "result")
            if case[7]:
                store_code += check_code %case[7]
            if apiInfo[3] == "post":
                fp.write(post_code %((apiInfo[1] + "_" + str(idx)), str(idx), param_code, store_code))
            elif apiInfo[3] == "get":
                fp.write(get_code %((apiInfo[1] + "_" + str(idx)), str(idx), param_code, store_code))
        if apiInfo[5] == 1:
            fp.write(class_end_db)
        fp.write("\n" + code_end)
        fp.close()

def create_script():
    db = DB()
    # 从数据库获取需要执行的api列表
    apiList = db.get_api_list()
    for api in apiList:
        # 更加api_id获取该接口的测试用例
        api_case_list = db.get_api_case(api[0])
        new_file(api[1:7], api_case_list)


if __name__ == '__main__':
    create_script()