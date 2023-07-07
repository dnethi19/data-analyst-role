import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='myschema')

# Duplicate entries in Users Data
duplicate_query = '''
SELECT *
FROM Users
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM Users
    GROUP BY user_id -- Replace 'user_id' with the actual primary key column name
);
'''
duplicate_entries = conn.execute(duplicate_query).fetchall()

# Null boolean values in the 'topBrand' column
null_top_brand_query = '''
SELECT *
FROM Brands
WHERE topBrand IS NULL;
'''
null_top_brand_values = conn.execute(null_top_brand_query).fetchall()

# Null 'brandCode' when barcode is available in the Receipts table
null_brand_code_query = '''
SELECT *
FROM Receipts
WHERE barcode IS NOT NULL AND brandCode IS NULL;
'''
null_brand_code_values = conn.execute(null_brand_code_query).fetchall()

# Print the results
print("Duplicate entries in Users Data:")
for row in duplicate_entries:
    print(row)

print("Null boolean values in the 'topBrand' column:")
for row in null_top_brand_values:
    print(row)

print("Null 'brandCode' when barcode is available in the Receipts table:")
for row in null_brand_code_values:
    print(row)

# Close the database connection
conn.close()
