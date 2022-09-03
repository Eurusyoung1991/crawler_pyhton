from selenium import webdriver
import time
ch_options = webdriver.ChromeOptions()
ch_options.add_argument("--headless")
ch_options.add_argument("--no-sandbox")
ch_options.add_argument("--disable-gpu")
ch_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=ch_options)
driver.implicitly_wait(20) # 隐性等待，最长等20秒
#把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)

for i in range(0,3):
    # 下滑到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 转换iframe，再找到查看更多，点击
    driver.switch_to_frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
    
    # if i% 10 ==1 :
    #     temp = driver.find_element_by_css_selector("div.more-wrapper")
    #     next_button = temp.find_element_by_css_selector('button[data-page="next"]')
    #     time.sleep(15)
    #     driver.execute_script("arguments[0].click();", next_button)
        
    # else:
    # temp = driver.find_element_by_css_selector("div.more-wrapper")
    page_button = driver.find_element_by_css_selector('button[data-page="%d"]' %(i+1))
    time.sleep(15)
    driver.execute_script("arguments[0].click();", page_button)
        
    print("第%g页评论" % int(i+1))
    
    comments = driver.find_elements_by_css_selector("div.reply-content")
    for each in comments:
        reply = each.find_element_by_tag_name("p")
        print(reply.text.encode("gbk","ignore").decode("gbk","ignore"))
    
    driver.switch_to.default_content()