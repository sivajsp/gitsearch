import urllib.request,urllib.parse,urllib.error
import json
import requests
class git_task():
    def maxdict(self,dic):
      #function to find the maximum in dictionary
      temp = [" ",0]
      for i in dic.keys():
        if(dic[i] > temp[1]):
          temp[1] = dic[i]
          temp[0] = i
      return temp
    def get_data(self,city):
        temp = urllib.request.urlopen("https://api.github.com/search/users?q=location:"+city+"&per_page=100&sort=repositories&order=desc")
        data = json.loads(temp.read().decode())
        dev = data["items"][0]["login"]
        str1 = "1.User with most number of the libraries in bangalore:"+dev
        flag = 0
        i = 1
        languages = {} # to store his own and forked repositories
        owner = {}#to store his own repositories
        while(flag==0):
            data  = requests.get("https://api.github.com/users/"+dev+"/repos?per_page=100&page="+str(i)).json()
            for j in range(len(data)):
                if(data[j]["fork"] is False):
                    if(data[j]["language"] in owner):
                        owner[data[j]["language"]] += 1
                    else:
                        owner[data[j]["language"]] = 1
                if(data[j]["language"] in languages):
                    languages[data[j]["language"]] += 1
                else:
                    languages[data[j]["language"]] = 1

            if(len(data)==2):
                info = requests.get("https://api.github.com/rate_limit").json()
                flag = 1
            if(len(data)<100):
                flag = 1
            i += 1
        values = self.maxdict(languages)
        own_values = self.maxdict(owner)

        str2 = "2. "+dev+"'s most preferred language "+values[0]+" total "+values[0]+" repositories are "+str(values[1])

        str3 = "3. "+dev+"'s own repository which aren't forked written in "+own_values[0]+" and total "+own_values[0]+"repositories are "+str(own_values[1])+"\nSo based on this Qualitative value he is "+own_values[0]+" developer"
        str4 = "By considering his repositories count as quantitative value he is "+values[0]+" developer"
        return [str1,str2,str3,str4]
        
