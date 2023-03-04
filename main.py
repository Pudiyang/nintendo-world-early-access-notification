import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
# Email configuration
sender_email = 'pudiyang@gmail.com'
receiver_email = ['pudiyang@gmail.com', 'zhouyue.sabrina@gmail.com']
sender_password = 'viudxznpuyswpfbl'
message = 'Subject: TEST - Nintendo Alarm - EA tickets are available for 03/14/2023'

def send_alarm():
    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(sender_email, sender_password)
        session.sendmail(sender_email, receiver_email, message)
        session.quit()
        print("ALARM SENT")


if __name__ == '__main__':
    url = "https://store.universalstudioshollywood.com/PurchaseTickets.aspx?Ref=Lite&View=CAT2"
    cookie_string = "at_check=true; _fbp=fb.1.1677869738812.1375863154; _gid=GA1.2.1229111014.1677869739; AMCVS_A8AB776A5245B4220A490D44%40AdobeOrg=1; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22d6c1f5d2-1498-4e50-9c7d-a37365ca44c7%22; _svsid=b55edd82649e99d350988743a0d0d619; QuantumMetricEnabled=false; s_vi=[CS]v1|32012155337CE9DC-6000041A0587644A[CE]; s_ecid=MCMID%7C09333336245999591743917258371478073111; _gcl_au=1.1.1281783258.1677869739; _scid=e549b1e9-e874-4e0f-9801-8efbfb16e771; _sctr=1|1677830400000; _ga=GA1.3.769617101.1677869739; _gid=GA1.3.1229111014.1677869739; usprivacy=1YNN; bbi_eVar77=USH: NC - CAT2 Offer Marketing Site - Cal Redesign (Production) - Experience A; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Mar+03+2023+18%3A24%3A19+GMT-0800+(Pacific+Standard+Time)&version=6.24.0&isIABGlobal=false&hosts=&consentId=0b92261e-906f-4a42-a3be-5e1c49c52b00&interactionCount=1&landingPath=NotLandingPage&groups=15%3A1%2C12%3A1%2C10%3A1%2C14%3A1%2C9%3A1%2CSPD_BG%3A1%2Cdummy%3A1%2C11%3A1%2C13%3A1&AwaitingReconsent=false; RSApps_SessionId=2i2fkx3brot2hikb5xi0np0c; AMCV_A8AB776A5245B4220A490D44%40AdobeOrg=359503849%7CMCIDTS%7C19420%7CMCMID%7C09333336245999591743917258371478073111%7CMCAAMLH-1678510742%7C9%7CMCAAMB-1678510742%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1677913142s%7CNONE%7CMCAID%7C32012155337CE9DC-6000041A0587644A%7CvVersion%7C5.0.1; s_vnc365=1709441942823%26vn%3D3; s_ivc=true; s_inv=7790; s_dur=1677905942843; s_sq=%5B%5BB%5D%5D; RSApps_SessionInfo=SameSite=Lax&X-Mobile=D&X-Forwarded-For=98.33.96.15&TimeOut-Warning=780&Last-Update=131578056; encrypted_store_cookie=!lfnf0Tq/1PG/hn0hZfT0UCxv7e9x2fvXf0V+oy31U++382mS8ZRINQHcRUv/vrbIZvZ+GLRBIqUeubXLlEi7uJfVvMjnDDA81m9pppE2a8OjkX7XjFOEHQuSHaGdsBSxknP55PcQapYwdEH45w4c1AR8TfFFmqw=; mbox=PC#485cc7f9bbb1487ab6af47d6db710fd3.35_0#1741152457|session#cce40196f5db448cb9f073cbde9bc7bd#1677909517; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Mar+03+2023+21%3A27%3A36+GMT-0800+(Pacific+Standard+Time)&version=6.24.0&isIABGlobal=false&hosts=&consentId=0b92261e-906f-4a42-a3be-5e1c49c52b00&interactionCount=1&landingPath=NotLandingPage&groups=15%3A1%2C12%3A1%2C10%3A1%2C14%3A1%2C9%3A1%2CSPD_BG%3A1%2Cdummy%3A1%2C11%3A1%2C13%3A1&AwaitingReconsent=false; _uetsid=fd26c0f0b9f411edb44c77319e5f78d8; _uetvid=fd26ce90b9f411edb0c71d1bc66195b1; _tq_id.TV-09457254-1.91ae=132aa9a870146146.1677869939.0.1677907657..; f5avr1992732420aaaaaaaaaaaaaaaa_cspm_=GLGGIFFKBALKFABINDDIKNHPPDEDPNADOOLDGHCGJGOBCPMCOHFIFGDAFIJNMCBKPDHCILNLIJFJNGBOHFDACJOBAMFACFEOEAIABPPLPNOIAENCILKFHGJHOPALABDC; gpv_pn=ots%7Cselect%20ticket%7Cepa; _ga=GA1.1.769617101.1677869739; _ga_L1GX2V9CMK=GS1.1.1677907657.3.0.1677907657.60.0.0; s_sess=%20s_cm%3Dwww.google.comReferring%2520Sitesundefined%3B%20s_cc%3Dtrue%3B%20s_cmtb%3D1%3B; s_pers=%20s_tbm30%3D1%7C1680463539178%3B; s_tslv=1677907739136; s_nr30=1677907739137-Repeat"

    while True:
        cookies_dict = {}
        for cookie in cookie_string.split(";"):
            key_value = cookie.split("=", 1)
            if len(key_value) == 2:
                key, value = [s.strip() for s in key_value]
                cookies_dict[key] = value
        response = requests.get(url, cookies=cookies_dict)
        soup = BeautifulSoup(response.content, 'html.parser')
        input_elem = soup.find('input', {'id': 'EZRezCalendarDatePriceList'})
        value = input_elem['value']
        my_dict = eval(value)
        if my_dict['03/14/2023']['Sold'] == "N":
            send_alarm()
            break
        else:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{now}:  {my_dict['03/14/2023']['Sold']}")
        time.sleep(120)
