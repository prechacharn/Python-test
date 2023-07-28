def weird_division(n, d):
    if (n == 0 and d == 0) or (d == 0):
        return 1
    return n / d 


df = pd.read_csv('some_data.csv')

#Get list of columns in the dataframe
#The first column is the id of buyer, the rest are the metrics.
cols_name = df.columns.values[1:]
target_value = [3.5,25] 
target_value_dict = dict(zip(cols_name,target_value))


tolerance = [0.01,0.01]
tolerance_dict = dict(zip(cols_name,tolerance))


#set up while loop to random sample until getting within tolerance
i = 0
chosen_average_result_dict = dict(zip(cols_name,np.zeros(cols_name.size)))
therest_difference_dict = dict(zip(cols_name,np.zeros(cols_name.size)))

while True:

    #Initialize parameters
    check = 0

    #obtain random sampling
    df["allocation"] = np.random.choice(["chosen","the rest"], p=[0.05, 0.95], size=df.shape[0])
    #obtain test statistics
    
    for key in cols_name:
        chosen_average_result_dict[key] = df[df["allocation"] == "chosen"][key].mean()
        therest_average_result_dict[key] = df[df["allocation"] == "the rest"][key].mean()


        #Calculate percentage different between each metric of chosen group and the rest
        chosen_difference_dict[key] = abs(weird_division(chosen_average_result_dict[key],target_value_dict[key]) -1)
        therest_difference_dict[key] = abs(weird_division(chosen_average_result_dict[key],target_value_dict[key]) -1)
       
        #If fail then add value to check
        if chosen_difference_dict[key] > tolerance_dict[key] or therest_difference_dict[key] > tolerance_dict[key]:
            check = check + 1

#################### My Answer ########################

#######################################################



    #If check is 0 then pass
    if check == 0: break

    print(i)
    i = i+1


    
#print final percentage different
for key, value in chosen_difference_dict.items():
    print('chosen  ----' + key + ' absolute percentage error: ' + "{:.2%}".format(value))
for key, value in therest_difference_dict.items():
    print('The rest  ----' + key + ' absolute percentage error: ' + "{:.2%}".format(value))