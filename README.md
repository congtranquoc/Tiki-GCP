# Tiki Google cloud platform
This repository contains the implementation details and step to synchronize all Tiki product data to Google cloud platform's Data Warehouse Bigquery.
## Description
The primary goal of this project is to synchronize the entire Tiki product data to a Data Warehouse, specifically Google Cloud’s BigQuery. The project involves the following steps:

1. Setting up Compute Engine and MongoDB:

Create a Compute Engine instance and install MongoDB.
Restore the complete Tiki product data from a local MongoDB instance to the MongoDB instance on the VM.

2. Creating Data Backup:

Perform a full synchronization of all products stored in the MongoDB database to Google Cloud Storage as a backup.

3. Designing Data Warehouse – BigQuery:

Architect the structure and schema in BigQuery to accommodate the entire Tiki product dataset.

4. Creating Data Mart:

Develop a data mart that focuses on sellers and the products they are selling. This data mart will be utilized by the Data Analysis (DA) team.

5. Connecting to Data Studio:

  ii. Establish a connection between BigQuery and Data Studio.
  iii. Create a basic dashboard to showcase the following insights:
  
    - Total number of products sold across major categories.
    
    - Distribution of products from Chinese brands across major categories.
    
    - Correlation between product ratings and prices.
    
    - Top 10 sellers with the highest number of products listed on Tiki, along with the quantity of products for each seller.

## Implementation Steps
1. Set up a Compute Engine instance with MongoDB installed.
2. Restore Tiki product data from a local MongoDB instance to the MongoDB on the VM.
3. Perform a full data synchronization to Google Cloud Storage for backup purposes.
4. Design the schema and structure for the Data Warehouse in BigQuery.
5. Develop the data mart for sellers and their products.
6. connect BigQuery to Data Studio and create a dashboard with the specified insights.
For detailed instructions and code examples, please refer to the code files in this repository.

## Note
This project is focused on synchronizing Tiki product data to Google Cloud’s Data Warehouse using BigQuery and visualizing insights through Data Studio dashboards. It involves various technical aspects, including Compute Engine setup, MongoDB management, ETL processes, and data visualization.


