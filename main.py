import requests

url_adress = input("Url을 입력해주세요 : ")
if url_adress.startswith("https://"):
    res = requests.get(url_adress)
    if res.status_code == requests.codes.ok:
        print(f"사이트가 정상입니다. 응답코드 : {res.status_code}")
    
    else:
        print(f"사이트가 비정상입니다. 응답코드 : {res.status_code}")

else:
    print("Url을 정확하게 입력해주세요!")
