from scrapy.http.response.html import HtmlResponse

from selenium import webdriver

import time
class DongfangSpiderSpiderMiddleware:

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


sum=0##设置一个标记，来确定当前爬取的是第几个页面
class DongfangSpiderDownloaderMiddleware:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):
        global sum
        sum += 1
        self.driver.get(request.url)##输入爬虫文件request的url
        time.sleep(2)##等待加载时间
        url = self.driver.current_url
        ##找到输入跳转页面数值框
        input=self.driver.find_element_by_xpath(
            "/html/body/div[@class='page-wrapper']/div[@id='page-body']/div[@id='body-main']/div[@id='table_wrapper']/div[@class='listview full']/div[@class='dataTables_wrapper']/div[@id='main-table_paginate']/input[@class='paginate_input']")
        ##找到确定跳转按钮
        submit=self.driver.find_element_by_xpath(
            "/html/body/div[@class='page-wrapper']/div[@id='page-body']/div[@id='body-main']/div[@id='table_wrapper']/div[@class='listview full']/div[@class='dataTables_wrapper']/div[@id='main-table_paginate']/a[@class='paginte_go']")
        input.clear()
        ##输入当前的爬取页面
        input.send_keys(sum)
        #确认提交
        submit.click()
        ##等待页面加载
        time.sleep(2)
        ##当sum达到4，即爬取完一个板块的前四页，重置sum为0
        if sum==4:
            sum-=4
        ##获取网页信息
        source = self.driver.page_source
        response = HtmlResponse(url=url, body=source, encoding='utf-8')
        #提交截取的页面信息给爬虫文件
        return response
