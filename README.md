# Tiki - Google Cloud Platform Data Synchronization

> This repository serves as a comprehensive guide for synchronizing Tiki's product data with Google Cloud Platform's Data Warehouse using BigQuery.

## Overview

The main objective of this project is to seamlessly synchronize Tiki's entire product data into Google Cloud's BigQuery, enabling effective data analysis and insights. The project involves several key steps:

1. **Setting up Compute Engine and MongoDB**:
   - Create a Compute Engine instance and install MongoDB.
   - Restore Tiki's product data from a local MongoDB instance to the MongoDB on the virtual machine.

2. **Creating Data Backup**:
   - Perform a complete synchronization of all products from MongoDB to Google Cloud Storage as a backup.

3. **Designing BigQuery Data Warehouse**:
   - Architect the schema and structure within BigQuery to accommodate Tiki's product dataset.

4. **Developing Data Mart**:
   - Construct a data mart focused on sellers and their products, intended for the Data Analysis (DA) team.

5. **Connecting to Data Studio**:
   - Establish a connection between BigQuery and Data Studio.
   - Create a dashboard displaying key insights:
     - Total products sold across major categories.
     - Distribution of products from Chinese brands across categories.
     - Correlation between product ratings and prices.
     - Top 10 sellers and their listed products' quantities.

## Implementation Steps

Follow these steps to successfully execute the project:

1. **Setting up Compute Engine and MongoDB**:
   - Configure a Compute Engine instance and install MongoDB.
   
2. **Restoring Data**:
   - Migrate Tiki's product data from a local MongoDB instance to the MongoDB on the Compute Engine VM.

3. **Data Synchronization**:
   - Synchronize data to Google Cloud Storage for robust backup.

4. **Designing BigQuery Schema**:
   - Plan and implement an effective schema in BigQuery for Tiki's product data.

5. **Developing Data Mart**:
   - Build a specialized data mart centered around sellers and their products.

6. **Creating Data Studio Dashboard**:
   - Establish a seamless connection between BigQuery and Data Studio.
   - Design a dashboard with insightful visualizations.

For detailed instructions and code examples, refer to the provided code files.

## Important Note

This project focuses on synchronizing Tiki's product data with Google Cloud's Data Warehouse using BigQuery. It encompasses various technical aspects such as Compute Engine setup, MongoDB management, ETL processes, and data visualization. The project aims to empower data analysis and facilitate informed decision-making.
