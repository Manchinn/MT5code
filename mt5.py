from iqoptionapi.stable_api import edsg_MT5

mt5 = edsg_MT5(9999065859,"MetaQuotes-Demo","N@PkGmX6")
connect_ok = mt5.edsg_login_connect_mt5()

if connect_ok == True:
    print("Login Ok")
else:
    print("Not Login")
    quit()

