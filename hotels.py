from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import csv

f = open('Hotels.csv', mode='w',newline='')
my_file = csv.writer(f, delimiter=',')
my_file.writerow(['Hotel_Name','Room_Type','Room_Price','Top_Comment','Rating','Total_Reviews','Hotel_Link'])


#put chromedriver version here 
op = webdriver.ChromeOptions()
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
+"AppleWebKit/537.36 (KHTML, like Gecko)"
+"Chrome/110.0.0.0 Safari/537.36")
driver = webdriver.Chrome(executable_path= r"C:\Users\Apple Computer\Downloads\Compressed\chromedriver")
driver.maximize_window()
sleep(3)

def hotels_in_lahore():
        for offset in range(0,200,25):
                
                driver.get(f"https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaLUBiAEBmAEJuAEXyAEM2AEB6AEB-AELiAIBqAIDuAKx8dyfBsACAdICJGFiZWRkMzU4LWQ2NDctNDhlYS1iNTQ4LWYyOWQ0ZmJiMjM3YdgCBuACAQ&sid=7017c706b3059b8e3956a6590dfad9ea&aid=304142&checkin=2023-03-02&lang=en-gb&search_selected=true&ssne_untouched=Lahore&ac_click_type=b&dest_id=-782831&group_adults=2&sb=1&ac_meta=GhA5MjVlMWRlZmUwYjIwMWQ2IAAoATICZW46AmR1QABKAFAA&sb_travel_purpose=leisure&src=index&ss=Dubai%2C+Dubai+Emirate%2C+United+Arab+Emirates&checkout=2023-03-03&no_rooms=1&dest_type=city&offset={offset}")
                sleep(5)
                
                #property link
                l = driver.find_elements(By.XPATH, "//a[@class= 'e13098a59f']")
                links = [link.get_attribute('href') for link in l]
                print(f"there are {len(links)} ads on this page")
                sleep(3)
                #property name
                n = driver.find_elements(By.XPATH, "//div[@class='fcab3ed991 a23c043802']")
                names = [name.text for name in n]
                print(len(names))
                sleep(5)
                #top comment
                c = driver.find_elements(By.XPATH, "//div[@class='b5cd09854e f0d4d6a2f5 e46e88563a']")
                comment = [comments.text for comments in c]
                print(len(comment))
                sleep(5)
                #rating
                r = driver.find_elements(By.XPATH, "//div[@class='b5cd09854e d10a6220b4']")
                rating = [ratings.text for ratings in r]
                print(len(rating))
                sleep(5)
                #number of reviews
                rev = driver.find_elements(By.XPATH, "//div[@class='d8eab2cf7f c90c0a70d3 db63693c62']")
                reviews = [review.text for review in rev]
                print(len(reviews))
                sleep(5)
                #room type
                rt = driver.find_elements(By.XPATH, "//span[@class='df597226dd']")
                rt_list = [room.text for room in rt]
                print(len(rt_list))
                sleep(5)
                #room price
                rp_list = []
                rp = driver.find_elements(By.XPATH, "//span[contains(@class,'fcab3ed991')]")
                for price in rp:
                        rp_list.append(price.text)

                print(len(rp_list))
                sleep(5)
                 
                my_file.writerows(zip(names,rt_list,rp_list,comment,rating,reviews,links)) 
                sleep(5)
                
                # next_page = driver.find_element(By.XPATH, "//div[@class = 'f32a99c8d1 f78c3700d2']")
                # if next_page:
                #         next_page.click()
                #         sleep(10)
                #         print("Going to Next page...")
                #         hotels_in_lahore()
        
hotels_in_lahore() 
       
driver.quit()
print('closed')