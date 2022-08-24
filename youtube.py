from bs4 import BeautifulSoup
import requests
import re
search_term = input("What product do you want to search for? ")
#import tkinter as Tk

from tkinter import *
#price_range = input('/')

screen = Tk()
root = screen
html_text = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=comics&_sacat=0&LH_TitleDesc=0&_odkw=python+apps&_osacat=0').text
soup = BeautifulSoup(html_text, 'lxml')
comics = soup.find_all('li', class_ = 's-item s-item__pl-on-bottom s-item--watch-at-corner')
for comic in comics:
    new = comic.find('span', class_='SECONDARY_INFO')
    Title  = comic.find('h3', class_ = 's-item__title').text.replace('','')
    Title_2 = str(Title)
    price = comic.find('span', class_ = 's-item__price').text


#    items = Title
#    for item in items:
#        item = Title.find(text=re.compile(search_term))
#        print(item)
    #price_2 = str(price)

    #if price_range not in price:

   # link = comic.target.['href']





    print(f"The comic title:{Title.strip()}")
    print(f"Price: {price.strip()}")
   # print(link)

  #  print(f'''
#The comic title: { Title}
#Price: {price}

 #   ----------------------------------------------------------------
  #  ''')
    #print(link)



Titles = f"The comic title:{Title.strip()}"

root.geometry( "1000x1000")
root.config(bg= "white")

# creating frame
my_frame = Frame(root, bg= "white")
my_frame.pack(pady= 10)
text = Text(screen)
#for Title in Titles:
text.insert(INSERT, f'${Titles}')

#text.insert(END, " f'${Title_2}')
text.pack()
#bit_label.grid(row=0, column=1, padx= 20, sticky= "s")
#bit_label.config(text=f'${Title_2}')

root.mainloop()

#canvas = tk.Canvas(root, width = 600, height= 300)
#canvas.grid(columnspan=3)
#root = tk.Tk()



#root.mainloop()
#Display = comic.find_all(my_frame, text = re.compile(f'${Title}')
#Display = tk.Label(root,text = f'${Title}' )
#Display.grid(columnspan=3, column=0, row =0)
#from tkinter import *
#screen = Tk()
#screen.geometry('200x200')
#text = Text(screen)
#text.insert(INSERT, "{Title}")
#text.insert(END, " and I am blue")


#screen.mainloop()
