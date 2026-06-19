# # nothing return from function
# def nothing_return():
#     pass
# print(nothing_return())


# # Early rerutn
# def early_return(number =0):
#     if number %2==0:
#         return "Even number"
#     return "Odd number"
# print(early_return(13))

# # return multiple value 
# def return_multiple(type=10,cups=23 , price=100):
#     return type, cups, price

# tea_type, tea_cups, _ = return_multiple()



def tea_details():
    """
    Rendering tea details
    """
    return "Tea details loaded"
print(tea_details.__doc__)
