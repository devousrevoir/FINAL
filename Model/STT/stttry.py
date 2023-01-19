 #-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "d7e110fa-f855-4312-bc91-7d5976adf541"
audioFilePath = "C:/Users/82106/Downloads/hello.wav"
languageCode = "korean"
   
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
   
requestJson = {    
    "argument": {
        "language_code": languageCode,
        "audio": audioContents
      }
  }
   
http = urllib3.PoolManager()
response = http.request(
      "POST",
      openApiURL,
      headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey},
      body=json.dumps(requestJson)
  )
   
print("[responseCode] " + str(response.status))
print("[responBody]")
print("===== 결과 확인 ====")
print(str(response.data,"utf-8"))
                                      