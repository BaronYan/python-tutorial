name = '公司名' # 公司名
stock_price = 100 # 股票价格
stock_code = '000001' # 股票代码
stock_price_daily_growth_factor = 0.01 # 日增长率
growth_days = 10 # 增长天数

message = f"经过 {growth_days} 后，股价将达到{(stock_price * (1 + stock_price_daily_growth_factor) ** growth_days):.2f}元。"

print(message)