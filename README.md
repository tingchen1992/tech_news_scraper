#  TechCrunch News Scraper  
> 一個自動爬取 TechCrunch 最新新聞並展示在網頁上的 Flask 專案  

![Screenshot](./screenshots/homepage.png)  

---

## 專案簡介  
這是一個使用 **Python** 建立的新聞爬蟲專案，透過 Flask 來建構網頁，並使用 `feedparser` 來自動抓取 **TechCrunch** 的最新新聞。每天早上 8 點自動更新新聞，並且展示在網頁上。  

---

## 功能說明  
爬取 TechCrunch 的最新新聞  
每天早上 8 點自動更新新聞  
支援點擊新聞標題，直接跳轉到原始文章   

---

## 技術與工具  
- Python 3.10+  
- Flask  
- feedparser  
- APScheduler  
- HTML + CSS  

---

## 安裝步驟  

### 1️⃣ clone這個專案  
bash  

git clone https://github.com/tingchen1992/tech_news_scraper.git  

cd tech_news_scraper

### 2️⃣ 建立虛擬環境並安裝依賴 
`python -m venv venv`  

`source venv/bin/activate  `  

`pip install -r requirements.txt`

### 3️⃣ 啟動伺服器
`python app.py`

在瀏覽器中開啟：
http://127.0.0.1:5000

### 每日自動更新
專案使用 APScheduler，每天早上 8:00 自動更新 TechCrunch 最新新聞。

