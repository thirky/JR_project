from playwright.sync_api import sync_playwright
import time

class PlaywrightActions:
    """操作层：包含浏览器初始化和基础操作"""

    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            channel="msedge",
            headless=headless
        )
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
    
    def goto_jrie(self):
        """导航到固定网址"""
        self.page.goto("http://www.jrie.com.cn/")
        return self.page
    
    def close(self):
        """关闭浏览器资源"""
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    @staticmethod
    def add_data(page, site_id: str, device_name: str, data_name: str):
        time.sleep(1)
        #清空上一次勾选状态
        page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill("")          
        page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter") 
        time.sleep(1)
        #选框输入设备名并且刷新列表
        page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill(device_name)
        page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter")
        #等待设备出现并展开
        page.get_by_role("treeitem", name=site_id).get_by_role("group").nth(1).wait_for()
        page.get_by_role("treeitem", name=site_id).get_by_role("group").nth(1).click()  
        #等待数据项出现并勾选       
        page.get_by_role("treeitem", name=data_name).locator("span").nth(2).wait_for()
        page.get_by_role("treeitem", name=data_name).locator("span").nth(2).click() 
        page.get_by_role("button", name="确定").click()
