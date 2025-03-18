from flask import Flask, render_template
from scraper import get_techcrunch_news
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    news = get_techcrunch_news()
    today = datetime.today().strftime("%Y-%m-%d")  
    return render_template("index.html", news=news, today=today)


def scheduled_job():
    print(f"執行爬蟲: {datetime.now()}")


scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_job, "cron", hour=8, minute=0)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
