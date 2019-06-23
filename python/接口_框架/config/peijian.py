import requests
class peijian():
    def mingxi(self):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail"

        payload = "{\r\n \"partOrderItemId\": 3108\r\n}"
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderPartDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "795e06be-72df-48d8-bb4c-c400c6ed3c28,f9d549bf-59fa-46b4-ae2d-4accf9897841",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=c909d3541a63a46b75f314a4e94828c0; dapp.sgm.com:qa:=c909d3541a63a46b75f314a4e94828c0; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "30",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return response.json()
if __name__=='__main__':
    peijian().mingxi()