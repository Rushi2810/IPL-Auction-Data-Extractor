
## IPL Auction Data Extractor (using Beautiful Soup)

## Description:

This Python script extracts team information, specifically from the IPL auction website using Beautiful Soup for web scraping. It then saves the extracted data to an Excel file.

## How to Use

### 1. Install Dependencies:

```bash
  pip install pandas requests beautifulsoup4
```
### 2. Clone the Repository:
```bash
  git clone https://github.com/Rushi2810/IPL-Auction-Data-Extractor.git
```
### 3. Run the script:
```bash
  python main.py  # Replace "main.py" with your actual script name if different
```

## Screenshot
The screenshot showcases the main interface of the IPL auction website, displaying team names, remaining funding, oversea player, and total player.

![App Screenshot]("E:\Web Scraping\Tata IPL Auction 2024\pics\website_ss.png")


## Output

The script generates an Excel file named "Auction_Info.xlsx" that includes team names, team budgets, and the number of overseas and total players for each team.


## Additional Note


This code utilizes BeautifulSoup and pandas to scrape and extract team information, particularly focusing on Oversea Players, from the IPL auction website. It assumes a specific HTML structure and provides a flexible approach for data extraction. However, it's essential to periodically review and adjust the code to accommodate any changes in the website's structure or content.

Contributions are always welcome!


