"""
具体规则如下:
定义一个用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额的函数。
1.优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
2.积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)。
"""
def calcul_goods(*args, copon=0, score=0, transit_fee=0):
#计算总金额
    total_price_list = [goods[1]*goods[2] for goods in args]
    total_cost = sum(total_price_list)
#计算优惠券, 积分
    if total_cost >= copon and total_cost >= 5000:
        total_cost -= copon
    if total_cost >= 5000 and score//100 <= total_cost:
        total_cost -= score//100
#计算运费
    total_cost += transit_fee

    return total_cost

cost = calcul_goods(("手机", 5773, 2), ("耳机", 299, 1), copon = 499)
print(cost)