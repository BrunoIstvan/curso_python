import csv

# **************************************************
# LENDO TODAS AS LINHAS
# **************************************************
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)


# **************************************************
# LENDO TODAS AS LINHAS MAS USANDO O ENUMERATE PARA RECUPERAR O NÚMERO DA LINHA
# **************************************************
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data

# **************************************************
# LENDO TODAS AS LINHAS, PULANDO A PRIMEIRA
# **************************************************
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the first row
    next(csv_reader)

    # show the data
    for line in csv_reader:
        print(line)

# **************************************************
# CALCULANDO A SOMA TOTAL DAS AREAS DOS PAISES
# **************************************************
total_area = 0

# calculate the total area of all countries

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the header
    next(csv_reader)

    # calculate total
    for line in csv_reader:
        total_area += float(line[1])

print(total_area)

# **************************************************
# USANDO DICTREADER
# **************************************************
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    # skip the header
    next(csv_reader)
    # show the data
    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km2")


# **************************************************
# USANDO DICTREADER COM COLUNAS NOMEADAS
# **************************************************
fieldnames = ['country_name', 'area', 'code2', 'code3']

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")






# **************************************************
# ESCREVENDO NUM CSV 
# **************************************************
# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# csv data
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

