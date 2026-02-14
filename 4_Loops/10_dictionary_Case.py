users = [ # 0 1 2 
    {"id":1,'total':100,'coupon':'P20'}, # 0 
    {"id":2,'total':150,'coupon':'F50'},
    {"id":3,'total':80,'coupon':'FLAT50'}
]

discounts = {
    'P20' : (0.2,0), # percent valus , fixed Value
    'F50' : (0.5,0),
    'FLAT50' : (0,50)
}

for user in users:
    percent , fixed = discounts.get(user['coupon'],(0,0))
    discount = user['total'] *percent + fixed
    new_payable =user['total'] - discount
    print(f"{user['id']} get {discount} taka discount & have to pay {new_payable}")
