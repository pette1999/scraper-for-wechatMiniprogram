import scraper

def main():
    while True:
        print("1. 美本榜\n2. 国内高中\n3. 海外高中\n4. 申请机构")
        val = input("Which list you want to scrape?: ")
        print("- 2019\n- 2020\n- 2021\n- 2022")
        val2 = input("Which year do you want the data from?: ")
        if (val in ['1', '2', '3', '4'] and val2 in ['2019', '2020', '2021', '2022']):
            break
        else:
            print("Invalid Input.")
    if val == '1':
        print("Start to scrape colleges rankings...")
        scraper.grabColleges()
    elif val == '2':
        print("Start to scrape chinese high schools rankings...")
        scraper.grabChineseHighDetails(val2)
    elif val == '3':
        print("Start to scrape international high schools rankings...")
        scraper.grabInternationalHighDetails(val2)
    elif val == '4':
        print("Start to scrape advisors rankings...")
        scraper.grabAdvisorDetails(val2)

main()