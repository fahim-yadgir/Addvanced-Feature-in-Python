def match(status):
    match status:
        case 200:
            return "ok"
        
        case 404:
            return "Not found"
        
        case 500:
            return "Internal server error"
        
        case _:
            return "unknown status"
        
n = int(input("Enter a number : "))
print(match(n))