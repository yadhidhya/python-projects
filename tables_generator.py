'''To run this code successfully, save it in a folder and create a subfolder named "tables" within the same folder.
When you execute the code, it will automatically generate 20 multiplication tables,
each saved in a separate file inside the "tables" folder.'''



def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/tables_{n}.txt","w")as f:
        f.write(table)


for i in range(2,21):
    generateTable(i)
