
def format_description_text(description, total_len = None):

    if total_len == None:
        max = 130
    else:
        max = 275 - total_len  

    print(max)    

    if len(description) > max:
        if len(description.split('.')[0]) > max or len(description.split('?')[0]) > max or len(description.split('!')[0]) > max:
            return description[:max] + '...' 
        return description.split('.')[0] or description.split('?')[0] or description.split('!')[0]
    else:
         return description