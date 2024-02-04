def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as cats_info:  #open file 
            cats_list=[]
            for line in cats_info.readlines():
                x = line.split(",")
                dict = {"id": x[0], "name": x[1], "age": x[2].strip()}
                cats_list.append(dict)
        return cats_list
    except FileNotFoundError:
        return ("Txt file is not found")  


print (get_cats_info("D:\General\GoIT\Projects\HW_04_ISIN\Cats.txt")) 
