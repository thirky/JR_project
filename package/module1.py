#
 # @Date: 2024-04-11 13:48:01
 # @Author: thirky
 # @Description: 
 #
import re
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    site_id=["TA440309003V10A"]
    site_mate=" 【"
    SITE=site_mate+site_id[0]
    page = context.new_page()
    page.goto("http://www.jrie.com.cn/")
    page.get_by_role("textbox", name="租户").fill("jinrong")
    page.get_by_role("textbox", name="用户名").fill("admin")
    page.get_by_role("textbox", name="密码").fill("jinrong1101")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("数据报表").click()
    page.get_by_role("link", name="  历史曲线").click()
    page.get_by_text("soc曲线(顺德)").click()
    page.get_by_title("新建曲线").click()
    page.get_by_role("button", name="添加数据项").click()
    time.sleep(4)
    page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill("电池节能控制器")
    page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter")
    time.sleep(3)
    page.get_by_role("treeitem", name=SITE).get_by_role("group").nth(1).click()
    time.sleep(3)
    page.get_by_role("treeitem", name=" 剩余电量").locator("span").nth(2).click()
    time.sleep(3)
    page.get_by_role("button", name="确定").click()
    page.get_by_role("textbox", name="请选择项目").click()
    page.get_by_role("listitem").filter(has_text="立胜能源").click()
    page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(ad) 
    page.get_by_role("button", name="保存").click()   
    time.sleep(3)
    # ---------------------
    context.close()
    browser.close()