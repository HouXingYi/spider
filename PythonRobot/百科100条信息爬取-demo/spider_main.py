import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  #初始化url调度器
        self.downloader = html_downloader.HtmlDownloader()  #初始化下载器(请求)
        self.parser = html_parser.HtmlParser()  #初始化html解析器 
        self.outputer = html_outputer.HtmlOutputer()  #初始化html输出器

    def craw(self, root_url):  #开始爬虫
        count = 1
        self.urls.add_new_url(root_url) #添加第一个url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  #获取url
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  #请求并返回

                new_urls, new_data = self.parser.parse(new_url, html_cont)  #解析出子url集合和数据（url，title等）

                self.urls.add_new_urls(new_urls)   #添加新的待爬取的url
                self.outputer.collect_data(new_data)  #输出html页面添加新的数据

                if count == 1000:
                # if count == 2:
                    break

                count = count + 1
            except:
                print('craw failed')

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

