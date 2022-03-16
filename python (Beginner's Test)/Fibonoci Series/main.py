store_series = [0,1] 
counter = 0

fibonoci_len = eval(input("Enter the range for fibonuci series: "))

while counter < fibonoci_len:
        con_res = store_series[-1] + store_series[-2]
        store_series.append(con_res)
        counter += 1
        
print(store_series)