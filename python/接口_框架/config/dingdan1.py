import requests
from 接口_框架.data.dingdan_duqu import shuju

class dingdan():
    def cha_mixi(self,num):

        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch"

        payload = "{\r\n \"pageNum\":\"%s\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}"%(num)
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
            'cache-control': "no-cache",
            'Postman-Token': "cb9857a88de51876e5166a61b86993dd"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return response.json()
if __name__=='__main__':
     for i in shuju():
         dingdan().cha_mixi(i)