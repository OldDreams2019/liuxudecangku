import requests

class shouye():
    def z_tai(self):

        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage"

        header = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderHomePage",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "1f7c6b0b-66d5-4ba7-b4cd-31fea45c886d,77fd083a-4beb-47b2-8088-cf85c6dff79c",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=45729e0e8d5bc30df68c5567cb654724; dapp.sgm.com:qa:=45729e0e8d5bc30df68c5567cb654724; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, headers=header)

        print(response.text)
        # return response.json()
if __name__=='__main__':
     shouye().z_tai()