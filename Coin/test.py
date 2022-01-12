import pyupbit

access = "ZHzEZMrzgVXsPbTjJnSGM8GUgY5UMST3K1ua8D5y"          # 본인 값으로 변경
secret = "x6Zqr3ykxvxuTxgJIDHBix4nKAQqYBAbdJpsUPR9"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-SNT"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

