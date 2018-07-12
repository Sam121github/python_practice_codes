from urllib import request

goog_url = "http://query1.finance.yahoo.com/v7/finance/download/CSV?period1=1528450902&period2=1531042902&interval=1d&events=history&crumb=eZucwGqp94q"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)

    lines= csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')

    for x in lines:
        fx.write(x+ '\n')
    fx.close()

download_stock_data(goog_url)

