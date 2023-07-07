Data Analyst Task

According to the given task and Data, 
The JSON data appears to be from MongoDb which is NoSQL, as the data has Document type of fields. 
We are trying to convert it into Relational Database , and I have used MySQL Dialect here to do that. In that case, to convert Document type fields to relational models, I defined few more tables to show the relationship between the entities. 
To establish one to many relationship between Receipts and Brands, I have created a new table using the document type attribute rewardsReceiptItemList. And similarly, as CPG is a document type, I have created another table to establish the relationship of CPG with Brands table.

1.	 Added the ER diagram model to the repo.



2.	Solved the first SQL query, and added the SQL file to the repo.










3.	The data quality issues I found in the give data are, 
In Users Data, there are so many duplicate entries:
This means that in the Users Data table or dataset, there are multiple rows or records that have the same data which creates data inconsistency and other problems. 
 
In Brands Table:
The Brands Table contains a column called "topBrand" which has a Boolean data type. Boolean values can be either true or false, representing a binary choice. However, in some cases, the "topBrand" value is null, which means that the value is missing or unknown for those particular cases. 

Moreover, Receipts and Brands tables contains a column called "brandCode”. In some cases, the "brandCode" value is null. This occurs when there is a product with a corresponding barcode available in the Brands Table, but the brand code itself is not provided or missing for that particular product. It's important to ensure data consistency and completeness, so having null values in the "brandCode" column when there is a valid barcode in the Brands Table may indicate a data issue or inconsistency that needs to be addressed.

Added the code into the repo.




4.	Subject: Data Quality Issues and other concerns in our Business Data


Hi Team,

Hope you are doing well.


From the Dataset , looks like it is a MongoDB (NoSQL) dataset, and Ihave designed a Relational ER model for the given data applying normalization techniques. 
During my data validation , I have found few data discrepencies in the Data provided, that made it challenging for me to segregate the tables and push the bulk data into relational tables. 
 I wanted to discuss some data quality issues and few other concerns i have found in the DataSet provided. By comparing and examining different datasets and performing data quality checks, I was able to identify the presence of duplicate entries and missing values in relevant columns.

In our Users Data, I have identified numerous duplicate entries, where multiple records contain the same information. These duplicates could impact the data consistency and accuracy . Additionally, in our Brands Table, the "topBrand" column occasionally contains null values, indicating missing or unknown information. 
Similarly, in the receipts table, the "brandCode" column has null values when a product barcode exists in the Brands Table. These inconsistencies could affect the reliability of our data.

To address the duplicate entries, I propose implementing a deduplication process that identifies and removes the duplicates from the Users Data. This will help ensure that each user's information is represented accurately without any redundancy.
 For the null values in the "topBrand" column, we need to investigate the root cause. It may involve working with the team responsible for updating the Brands Table and implementing data validation measures to prevent null values in the future. S


Moreover, In real time or production scenario, as our data grows and the volume of users and transactions increases, we should anticipate potential performance and scaling concerns. I propose implementing appropriate indexing strategies, optimizing queries, and periodically reviewing the data infrastructure to ensure it can handle the increasing load efficiently.

I would appreciate your guidance and input in resolving the data quality issues and exploring the optimization opportunities. Please let me know if we can schedule a meeting to discuss this further. 
Thank you for your attention to this matter.

Best regards,

Divya.
