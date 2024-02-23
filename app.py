import re, time, os
from flask import Flask, request,render_template
import requests
import json

app = Flask(__name__)
def drivdownurl(txt):
    #print(txt)
    if re.findall("drive",txt):
      #print("Yes, its Google one !")
      pass
    else:
      #print("Not A Google")
      return txt
#Check if the string has any a, r, or n characters:
    x = re.sub("file[/]d[/]","uc?id=", txt)
    x = re.sub("[/]view[?]usp[=]sharing","&export=download", x)

    #print(x)
    return txt
   

@app.route('/',methods=['GET','POST'])
def index():
   
   print("hii")
   if request.method == "POST":
      rollnum,passw=request.args.get("rno"),request.args.get("pass")
      print(rollnum)
      print(passw)
      url = os.getenv("db_url") 
      #payload = json.dumps( {"rollNo": "xyz","dob": "26012003","data":{ "DEC23":"HSJSJWJWJ","WJWJ":"WHWH"}} )
      heyy={"q":json.dumps({"rollNo": f"{rollnum}"})}
      print(heyy)
      
      headers = {
    'content-type': "application/json",
    'x-apikey': os.getenv("x_apikey") ,
    'cache-control': "no-cache"
    }
      try:
         response = requests.get(url,params=heyy, headers=headers)
         sto=response.json()[0]
         print(sto)
         print(type(sto.get("dob")),type(passw))
      except:
         return [ false, "Login with Valid Details"]
         
      if ((str(sto.get("dob"))== str(passw) ) and (str(sto.get("rollNo"))== str(rollnum))):
         print("haleluya")
         gamedict=sto.get("data")
         gameid=list(gamedict.keys())




         t=f"""<table>
<tr><th rowspan="2" style="width:40px">S.no</th><th rowspan="2">Game ID/Date</th><th colspan="2">Certificates</th></tr>
<tr><th>View</th><th>Download</th></tr>"""
          i=1
          for id in gameid:
              t+=f"<tr><td>{i}</td><td>{id}</td><td><a href=\"{gamedict.get(id)}\" style=\"color:white\" >
<i class=\"openeye\"><svg class=\"openeye\" xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\" fill=\"none\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M15 12c0 1.654-1.346 3-3 3s-3-1.346-3-3 1.346-3 3-3 3 1.346 3 3zm9-.449s-4.252 8.449-11.985 8.449c-7.18 0-12.015-8.449-12.015-8.449s4.446-7.551 12.015-7.551c7.694 0 11.985 7.551 11.985 7.551zm-7 .449c0-2.757-2.243-5-5-5s-5 2.243-5 5 2.243 5 5 5 5-2.243 5-5z\"/></svg></i>
<i class =\"closeeye\"><svg class=\"closeeye\" width=\"24\" height=\"24\" xmlns=\"http://www.w3.org/2000/svg\" fill-rule=\"evenodd\" clip-rule=\"evenodd\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" fill=\"#fff\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M8.137 15.147c-.71-.857-1.146-1.947-1.146-3.147 0-2.76 2.241-5 5-5 1.201 0 2.291.435 3.148 1.145l1.897-1.897c-1.441-.738-3.122-1.248-5.035-1.248-6.115 0-10.025 5.355-10.842 6.584.529.834 2.379 3.527 5.113 5.428l1.865-1.865zm6.294-6.294c-.673-.53-1.515-.853-2.44-.853-2.207 0-4 1.792-4 4 0 .923.324 1.765.854 2.439l5.586-5.586zm7.56-6.146l-19.292 19.293-.708-.707 3.548-3.548c-2.298-1.612-4.234-3.885-5.548-6.169 2.418-4.103 6.943-7.576 12.01-7.576 2.065 0 4.021.566 5.782 1.501l3.501-3.501.707.707zm-2.465 3.879l-.734.734c2.236 1.619 3.628 3.604 4.061 4.274-.739 1.303-4.546 7.406-10.852 7.406-1.425 0-2.749-.368-3.951-.938l-.748.748c1.475.742 3.057 1.19 4.699 1.19 5.274 0 9.758-4.006 11.999-8.436-1.087-1.891-2.63-3.637-4.474-4.978zm-3.535 5.414c0-.554-.113-1.082-.317-1.562l.734-.734c.361.69.583 1.464.583 2.296 0 2.759-2.24 5-5 5-.832 0-1.604-.223-2.295-.583l.734-.735c.48.204 1.007.318 1.561.318 2.208 0 4-1.792 4-4z\"/></svg></i>
</a></td>
<td>
<a href=\"{drivdownurl(gamedict.get(id))}\" style=\"color:white\" ><svg xmlns=\"http://www.w3.org/2000/svg\" class=\"icon icon-tabler icon-tabler-download\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" stroke-width=\"2\" stroke=\"currentColor\" fill=\"none\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path stroke=\"none\" d=\"M0 0h24v24H0z\" fill=\"none\"/><path d=\"M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2\" /><path d=\"M7 11l5 5l5 -5\" /><path d=\"M12 4l0 12\" /></svg>
</a>
</td></tr>"

          i+=1
          t+="</table> "
          redata.append(t)
          return [true , redata]
      else:
         return [ false, "Invalid Credentials "]
   else:
      return "<html><title>Welcome</title><body><h1>Happy day</h1></body></html>"


def main(abc):
   url = os.getenv("db_url")
   #payload = json.dumps( {"rollNo": abc ,"dob": "26012003","data":{ "DEC23":"HSJSJWJWJ","WJWJ":"WHWH"}} )
   headers = {
    'content-type': "application/json",
    'x-apikey': os.getenv("x_apikey"),
    'cache-control': "no-cache"
    }
   heyy={"q":json.dumps({"rollNo": f"{abc}"})}
   print(heyy)
   #time.sleep(4)
   response = requests.get(url,params=heyy,headers=headers)
   print(response)
   temp=response.json()[0].get("data")
   #print(temp)
   key=temp.keys()
   p=""
   for i in key:
      p=f"<tr>{i}</tr><tr>{temp[i]}</tr>"
      #print(i,"\t", temp[i])

   #pastedf rom APP
   p=f"""<html><h1>HODOHD</h1><table>
   <tr><th>Company</th>
   <th>Contact</th>
   <th>Country</th>
  </tr>
  <tr>
    <td>{rollnum}</td>
    <td>{passw}</td>
    <td>Germany</td>
  </tr>"""
   print(key)
   
   for i in key:
      p+=f"<tr><td>{key.index(i)+1}</td><td>{i}</td><td>{temp[i]}</td></tr>"
   p+=f"""</table></html>"""
   return p




#if __name__ == '__main__':
#   app.run(debug = True)
#   main("xyz")
