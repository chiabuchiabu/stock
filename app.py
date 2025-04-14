from flask import Flask,render_template,request
import yfinance as yf

app=Flask(__name__)

@app.route('/')
def home():

    symbol=request.args.get("symbol","AAPL")
    try:
        aapl=yf.Ticker(symbol)
        name=aapl.info.get("shortName")
        income = aapl.income_stmt.T["Net Income"].head(3)
        labels = income.index.strftime("%Y-%m").tolist()
        values = income.tolist()
        labels.reverse()
        values.reverse()

        return render_template('index.html',labels=labels,values=values,name=name)

    except Exception as e:
        error_message = f"取得資料時發生錯誤(輸入錯誤公司名)"
        return render_template('index.html', labels=[], values=[], name="-----", error=error_message)
