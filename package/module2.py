#
 # @Date: 2024-04-11 13:48:01
 # @Author: thirky
 # @Description: 充放电情况，添加深圳36站点
 #
import re
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    site_id=[
        "TA440309001V10A","TA440309002V10A","TA440309003V10A","TA440309004V10A",
        "TA440309005V10A","TA440309006V10A","TA440309007V10A","TA440309008V10A",
        "TA440309009V10A","TA440309010V10A","TA440309011V10A","TA440309012V10A",
        "TA440309013V10A","TA440309014V10A","TA440309015V10A","TA440309016V10A",
        "TA440309017V10A","TA440309018V10A","TA440309019V10A","TA440309020V10A",
        "TA440309021V10A","TA440309022V10A","TA440309023V10A","TA440309024V10A",
        "TA440309025V10A","TA440309026V10A","TA440309027V10A","TA440309028V10A",
        "TA440309029V10A","TA440309030V10A","TA440309031V10A","TA440309032V10A",
        "TA440309033V10A","TA440309034V10A","TA440309035V10A","TA440309036V10A",
    ]
    site_name=[
        "河背二(M)"     ,"大水坑六(D)"  ,"水斗新村"     ,"清湖西(D)",
        "水坑塘前(D)"   ,"伍屋二(D)"    ,"观音布(M)"    ,"贤合村二(M)",
        "木坪岗(M)"     ,"罗屋围村(T)"  ,"大浪万景(M)"  ,"牛湖三(M)",
        "龙兴新村(D)"   ,"悦兴悦民(M)"  ,"三合一(D)"    ,"观天裕新(D)",
        "樟企桂花(D)"   ,"松仔园(M)"    ,"布龙横朗(D)"  ,"水斗富豪(D)",
        "伍屋(D)"       ,"安良八村(D)"  ,"白泥坑(D)"    ,"龙胜(M)",
        "碧岭工业(M)"   ,"碧岭新沙(M)"  ,"创意(D)"      ,"大康二(M)",
        "大康下中(M)"   ,"旱塘村(M)"    ,"六工工业(M)"  ,"六约惠源(D)",
        "平湖辅歧(D)"   ,"埔吓(T)"      ,"贤合村(D)"    ,"新南水门(D)"
    ]
    group_name="站点负载曲线(深圳)"
    equipment="电池节能控制器"
    data_part=""
    data=" "+"负载电流"
    page = context.new_page()
    page.goto("http://www.jrie.com.cn/")
    page.get_by_role("textbox", name="租户").fill("jinrong")
    page.get_by_role("textbox", name="用户名").fill("szgdj")
    page.get_by_role("textbox", name="密码").fill("123456")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("数据报表").click()
    page.get_by_role("link", name="  历史曲线").click()
    for i in range(len(site_id)):
        SITE=" 【"+site_id[i]
        page.get_by_text(group_name).click()
        page.get_by_title("新建曲线").click()
        page.get_by_role("button", name="添加数据项").click()
        time.sleep(2)
        page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill(equipment)
        page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter")
        time.sleep(1)
        if i==0:
            SITE=" 【"+site_id[i]
            page.get_by_role("treeitem", name=SITE).get_by_role("group").nth(1).click()
            time.sleep(1)
            page.get_by_role("treeitem", name=data).locator("span").nth(2).click()
            time.sleep(1)
            page.get_by_role("button", name="确定").click()
            page.get_by_role("textbox", name="请选择项目").click()
            page.get_by_role("listitem").filter(has_text="深圳铁塔").click()
            page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
            # page.get_by_role("textbox", name="请选择算法").click()
            # page.get_by_text("相减").click() 
            page.get_by_role("button", name="保存").click()   
            time.sleep(1)
        elif i>0:
            SITE=" 【"+site_id[i-1]
            page.get_by_role("treeitem", name=SITE).get_by_role("group").nth(1).click()
            time.sleep(1)
            page.get_by_role("treeitem", name=data).locator("span").nth(2).click()
            time.sleep(1)
            page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill("")
            page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter")
            time.sleep(1)
            page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill(equipment)
            page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter")
            time.sleep(1)
            SITE=" 【"+site_id[i]
            page.get_by_role("treeitem", name=SITE).get_by_role("group").nth(1).click()
            time.sleep(1)
            page.get_by_role("treeitem", name=data).locator("span").nth(2).click()
            time.sleep(1)
            page.get_by_role("button", name="确定").click()
            page.get_by_role("textbox", name="请选择项目").click()
            page.get_by_role("listitem").filter(has_text="深圳铁塔").click()
            page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
            # page.get_by_role("textbox", name="请选择算法").click()
            # page.get_by_text("相减").click() 
            page.get_by_role("button", name="保存").click()   
            time.sleep(1)
    # ---------------------
    context.close()
    browser.close()