# coding:utf-8

from selenium import webdriver
from time import sleep

url = 'https://movie.douban.com/typerank?type_name=%E6%81%90%E6%80%96&type=20&interval_id=100:90&action='
bro = webdriver.PhantomJS(executable_path='./phantomjs')

bro.get(url=url)
sleep(1)
# 截屏
bro.save_screenshot('./2.png')
# 编写js代码，让滚轮滑动到底部
js = 'window.scrollTo(0,document.body.scrollHeight)'
# 让浏览器执行js代码
bro.execute_script(js)
sleep(1)
# 只想完成后再次截屏
bro.save_screenshot('./3.png')
# 滚动后加载页面,page_source获取加载数据后的页面
page_text = bro.page_source

print(page_text)
