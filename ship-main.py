# -*- coding:utf8 -*- 
import requests
import json
import time
if __name__ == "__main__":
    while(True):
        time.sleep(0.5)

        url = 'http://www.shipxy.com/Ship/Index'
        post_mmsi_url='http://searchv3.shipxy.com/shipdata/search3.ashx?f=auto&kw'

        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Cookie':'FD857C2AF68165D4=zznpZ2lrIkTYPmc7S4/Wlt2ii2OW5WJ0xIIInNU2gl/S36yr5WUp8i/BDBBc8pjV; _elane_maptype=MT_TIANDITU; Hm_lvt_adc1d4b64be85a31d37dd5e88526cc47=1622095836; tc_TC=; _elane_shipfilter_type=%u8D27%u8239%2C%u96C6%u88C5%u7BB1%u8239%2C%u6CB9%u8F6E%2C%u5F15%u822A%u8239%2C%u62D6%u8F6E%2C%u62D6%u5F15%2C%u6E14%u8239%2C%u6355%u635E%2C%u5BA2%u8239%2C%u641C%u6551%u8239%2C%u6E2F%u53E3%u4F9B%u5E94%u8239%2C%u88C5%u6709%u9632%u6C61%u88C5%u7F6E%u548C%u8BBE%u5907%u7684%u8239%u8236%2C%u6267%u6CD5%u8247%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u533B%u7597%u8239%2C%u7B26%u540818%u53F7%u51B3%u8BAE%28Mob-83%29%u7684%u8239%u8236%2C%u62D6%u5F15%u5E76%u4E14%u8239%u957F%3E200m%u6216%u8239%u5BBD%3E25m%2C%u758F%u6D5A%u6216%u6C34%u4E0B%u4F5C%u4E1A%2C%u6F5C%u6C34%u4F5C%u4E1A%2C%u53C2%u4E0E%u519B%u4E8B%u884C%u52A8%2C%u5E06%u8239%u822A%u884C%2C%u5A31%u4E50%u8239%2C%u5730%u6548%u5E94%u8239%2C%u9AD8%u901F%u8239%2C%u5176%u4ED6%u7C7B%u578B%u7684%u8239%u8236%2C%u5176%u4ED6; _filter_flag=-1; _elane_shipfilter_length=0%2C40%2C41%2C80%2C81%2C120%2C121%2C160%2C161%2C240%2C241%2C320%2C321%2C9999; _elane_shipfilter_sog=0%2C1; _elane_shipfilter_one=2; _elane_shipfilter_country=0%2C1%2C2; _elane_shipfilter_olength=; tc_QX=; shipxy_v3_history_serch=s%u2606OOCL%20POLAND%u2606477182200%u2606100%u2606IMO%uFF1A9622588%7Cs%u2606YUEYINGDEHUO2668%u2606413901954%u260670%u2606MMSI%uFF1A413901954; ASP.NET_SessionId=lhhqbqnp2g2feexfzuxya4h4; Hm_lpvt_adc1d4b64be85a31d37dd5e88526cc47=1622101471; Shipxy_VerificationCode=dfc24891-3a80-47b1-aa94-af2d074d9af3; .UserAuth2=CE6380BCB284336E3C0BF0D07D54E015B67CA8ACF9D3D7DA6A05E8121C594389D19F2AD3B3B3EC718DEC92EB2A0C623E41B6A98AEACBB26126EB3719348F3EAC030EF337BEFCAFEFFD1B2B03BEB4DF8DE4C3857D3EA86D1F60D40D3B76A2BD28D9FF837E747C9433631EF918F1F51F39B93DCF50474C38B8409A9BC3E8968AD0CD46B035; SERVERID=ce54c768aca7be22386d8a7ce24ecdae|1622101560|1622099534'
        }

        #寝室兄弟的性命和IMO号
        ship_list = [
            {
            'name':"test1",
            'shipNum':9622588
            },
            {
            'name':"test2",
            'shipNum':9416628
            },
            {
            'name':"test3",
            'shipNum':9868259
            }

        ]

        all_lat_lon =[]


        for ship in ship_list:

            data={
            'kw':ship['shipNum']
            }

            # 请求mmsi号
            ship_mmsi_get = requests.post(url=post_mmsi_url,data=data,headers=headers).json()
            ship_mmsi_get = ship_mmsi_get['ship'][0]['m']
            mmsi_data={
                'mmsi':ship_mmsi_get
            }

        
            respone =requests.post(url='http://www.shipxy.com/ship/GetShip',data=mmsi_data, headers=headers).json()

            return_obj ={
                'lon':  respone['data'][0]['lon'],
                'lat':  respone['data'][0]['lat']
            }

            lon =str(return_obj['lon'])
            lat = str(return_obj['lat'])
    
            lon_pre = lon[0:len(lon)-6]
            lat_pre = lat[0:len(lat)-6]
    
            lon_last_6 = lon[len(lon)-6:len(lon)]
            lat_last_6 = lat[len(lat)-6:len(lat)]

            lat_lon = {
                'name':ship['name'],
                'lat':lat_pre+"."+lat_last_6,
                'lon':lon_pre+"."+lon_last_6
            }

            all_lat_lon.append(lat_lon)


        all_lat_lon = json.dumps(all_lat_lon)
        with open('./lat_lon.json','w') as fp:
            fp.write(all_lat_lon)

    
