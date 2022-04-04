import scraper

def main():
    while True:
        print("1. 美本榜\n2. 国内高中\n3. 海外高中\n4. 申请机构")
        val = input("which list you want to scrape?: ")
        if(val in ['1','2','3','4']):
            break
        else:
            print("Invalid Input. Please enter number 1,2,3 or 4.")
    if val == '1':
        print("Start to scrape colleges rankings...")
        scraper.grabColleges()
    elif val == '2':
        print("Start to scrape chinese high schools rankings...")
        scraper.grabChinaHighSchools()
    elif val == '3':
        print("Start to scrape international high schools rankings...")
        scraper.grabInternationalHighSchools()
    elif val == '4':
        print("Start to scrape advisors rankings...")
        scraper.grabAdvisors()

main()