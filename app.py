import re, time, os
from flask import Flask, request,render_template
import requests
import json

app = Flask(__name__)


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
      
      response = requests.get(url,params=heyy, headers=headers)
      temp=response.json()
      print(type(temp.get("dob")),type(passw))
      if ((str(temp.get("dob"))== passw) and (str(temp.get("rollNo"))== str(rollnum))):
         print("haleluya")
         tempor=temp.get("data")
         key=list(tempor.keys())
         return render_template("essay.html",key=key,temp=tempor)
      else:
         return render_template("invalid.html")
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
