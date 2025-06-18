import csv
max_sales=0
index=0
best_book=''
# Open the CSV file in 'read' mode with UTF-8 encoding
with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)
  #skip the first line of the file
  file.readline()
  for row in csv_reader:
    print(row)
    sales = float(row[4])
    if sales > max_sales:
      max_sales = sales
      best_book = row



#creates a new CSV file
output_file_path = 'bestseller_info.csv'
with open(output_file_path, 'w', newline='') as output_file:
  csv_writer = csv.writer(output_file)
  
  # Write header
  csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
  
  # Write best-selling book info
  csv_writer.writerow([best_book[0], best_book[1], best_book[4]])

# Bonus: Print confirmation message
print('Bestselling info written to', output_file_path)
