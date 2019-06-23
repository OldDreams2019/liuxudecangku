import requests
from 接口_框架.data.FP_duqu import du_qu

class FPcx():
      def cha_xun(self,num):
            url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderElectricInvoice"

            payload = "{\n    \"orderNo\": \"%s\"\n}"%(num)
            headers = {
                'Content-Type': "application/json",
                'x-dealer-code': "2100001",
                'x-position-code': "D_PO_1028",
                'x-resource-code': "pol4s_partOrder_orderElectricInvoice",
                'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                'x-user-code': "dhxc1u",
                'x-access-token': "f80cb343412ed62cc8e2f7ba08fd8fd8",
                'User-Agent': "PostmanRuntime/7.15.0",
                'Accept': "*/*",
                'Cache-Control': "no-cache",
                'Postman-Token': "24f0a7b2-c68e-4a6b-b1d1-064275a98e6e,93d6b02f-d1d7-4a25-8f89-a5e3ff7e3175",
                'Host': "mobileqa.dms.saic-gm.com",
                'cookie': "dapp.sgm.com:qa:=f80cb343412ed62cc8e2f7ba08fd8fd8; dapp.sgm.com:qa:=f80cb343412ed62cc8e2f7ba08fd8fd8; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
                'accept-encoding': "gzip, deflate",
                'content-length': "38",
                'Connection': "keep-alive",
                'cache-control': "no-cache"
                }

            response = requests.request("POST", url, data=payload, headers=headers)

            print(response.text)
            return response.json()
if __name__=='__main__':
    # FPcx().cha_xun(i)
      for i in du_qu():
          print(i)
          print(i[0])
          FPcx().cha_xun(i[0])
