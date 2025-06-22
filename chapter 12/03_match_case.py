# def http_status(status): 
#     match status: 
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"
        
# print(http_status(400))

# ###             NEW
# def rahul(hii):
#     match hii:
#         case 400:
#             return "can you more"
#         case 500:
#             return "this is not enough"
#         case 499: 
#             return "this is enough"

# print(rahul(500))

# ###             NEW

# def hii(Hello):
#     match Hello:
#         case "Rahul":
#             return "Rahul Ninawe"
#         case "Sager":
#             return "Sager Tetu"
#         case "Harish":
#             return "Harish Nimje"
#         case "pratik":
#             return "Pratik Bhakete"
        
# print(hii("Rahul"))
# print(hii("Sager"))
# print(hii("Harish"))
# print(hii("pratik"))

def patik(bhakate):
    match bhakate:
        case 1:
            return "they all function are present"
            
        
        case 2:
            return "they all function are not present"
        
print(patik(1))
print(patik(2))