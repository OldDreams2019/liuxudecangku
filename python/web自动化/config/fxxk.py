from selenium import webdriver
from time import sleep
from web自动化.data.fx_duqu import du_qu
class fx():
    def web(self):
        dr=webdriver.Firefox()
        dr.get('https://www.fxiaoke.com')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="cssmenu"]/div[5]/a[1]').click()
        sleep(2)
        aa=dr.window_handles
        sleep(2)
        dr.switch_to.window(aa[-1])
        sleep(2)
        dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/ul/li[2]').click()
        sleep(2)
        dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[8]/span[2]').click()
        sleep(2)
        for i in du_qu():
            try:
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/input').send_keys('{}'.format(i[0]))
                    sleep(2)
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys('{}'.format(int(i[1])))
                    sleep(2)
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/input').send_keys('{}'.format(i[2]))
                    sleep(2)
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[5]').click()
                    sleep(5)
                    a=dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/ul[2]/li[1]/a/span[1]').text
                    print(a)

                    if a=='我的工作台':
                        break

            except:
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/input').clear()
                    sleep(1)
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/input').clear()
                    sleep(2)
                    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/input').clear()
                    sleep(2)
        return a
if  __name__=='__main__':
    fx().web()
