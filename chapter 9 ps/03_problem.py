def generatTable(n):
    table=""
    for i in range(1, 11):
        table +=f"{n} * {i}={n*i}\n"

    with open(f"tables/table{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generatTable =(i) # Calls the function with i as an argument







