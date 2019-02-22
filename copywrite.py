import requests, os
from bs4 import BeautifulSoup
           
                 
def copywrite(url):

    res=requests.get(url) 
    soup=BeautifulSoup(res.content, "html.parser")
    n_list=soup.find_all("div", id="lyrics")
    
    

    with open ("sample.txt","w") as f:
     for n in n_list:
         f.write (n.get_text())
         
         
 




if __name__ == "__main__":
    url="https://www.songtexte.com/songtext/freddie-mercury/bohemian-rhapsody-23982857.html"
    
    print copywrite(url)
    
    
    
