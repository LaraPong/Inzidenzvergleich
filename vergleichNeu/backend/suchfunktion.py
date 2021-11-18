Staedte={
    "Hamburg" :1000,
    "Berlin":3000,
    "Lübeck":4000,
    "Neumünster":5000,
    }
#TODO dict in parameter
list = []

def main_search(query,query2):
   list =[]
   for key, value in Staedte.items():
       if query  in key:
           list.append(query)
           list.append(value)
       if  query2  in key:
           list.append(query2)
           list.append(value)
           print(list)
   return(list)

