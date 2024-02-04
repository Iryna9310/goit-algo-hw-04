def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as salary_file:   # open file to read
            total = 0
            lines_number = 0
            for line in salary_file.readlines(): 
                x=line.split(",")
                total += int(x[1]) # total sum calculation
                lines_number +=1   # number of lines calculation
            average = total // lines_number
        return (total, average) # results return
    except FileNotFoundError:
        return ("Txt file is not found") # error message
 
total, average = total_salary("D:\General\GoIT\Projects\HW_04_ISIN\Salary.txt") #pass
print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") #results print

