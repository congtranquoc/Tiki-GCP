# Tiki - Google Cloud Platform Data Synchronization

> This repository serves as a comprehensive guide for synchronizing Tiki's product data with Google Cloud Platform's Data Warehouse using BigQuery.

## Overview

The main objective of this project is to seamlessly synchronize Tiki's entire product data into Google Cloud's BigQuery, enabling effective data analysis and insights. The project involves several key steps:

1. **Setting up Compute Engine and MongoDB**:
   - Create a Compute Engine instance and install MongoDB.
   ```bash
     gcloud compute instances create tiki-instance \
    --zone=asia-east2-a \
    --image-family=ubuntu-2004-lts \
    --boot-disk-size=100GB \
    --machine-type=e2-medium \
    --tags=http-server,https-server,mongodb-server
   ```
   ```bash
      # firewall-rules HTTP
      gcloud compute firewall-rules create allow-http \
          --direction=INGRESS \
          --priority=1000 \
          --network=default \
          --action=ALLOW \
          --rules=tcp:80 \
          --source-ranges=0.0.0.0/0 \
          --target-tags=http-server
   ```
   ```bash
      # firewall-rules HTTPs
      gcloud compute firewall-rules create allow-https \
          --direction=INGRESS \
          --priority=1000 \
          --network=default \
          --action=ALLOW \
          --rules=tcp:443 \
          --source-ranges=0.0.0.0/0 \
          --target-tags=https-server
   ```
   ```bash
      # firewall-rules Mongodb
      gcloud compute firewall-rules create allow-mongodb \
          --direction=INGRESS \
          --priority=1000 \
          --network=default \
          --action=ALLOW \
          --rules=tcp:27017 \
          --source-ranges=0.0.0.0/0 \
          --target-tags=mongodb-server
     ```

   - Execute compute
   ```bash
      gcloud compute ssh tiki-instance --zone=asia-east2-a
   ```
   - Install mongodb to VM:
       - Install and Update the `gnupg` utility.
         ```bash
            sudo apt-get install gnupg
         ```
       - Import the public MongoDB GPG signing key.
         ```bash
         wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
         ```
       - Add details about the official MongoDB repository to the list of Ubuntu packages.
         ```bash
         echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
         ```
       - Update the list of packages using `apt`.
         ```bash
         sudo apt-get update
         ```
       - Install the latest release of MongoDB.
         ```bash
         sudo apt-get install -y mongodb-org
         ```
       - Reload the systemctl daemon.
         ```bash
         sudo systemctl daemon-reload
         ```
       - Start the mongod process using `systemctl start`.
         ```bash
         sudo systemctl start mongod
         ```
       - Use `systemctl status` to ensure the MongoDB service is active.
         ```bash
         sudo systemctl status mongod
         ```
       - To configure Ubuntu to launch MongoDB at system boot time, enter the following command.
         ```bash
         sudo systemctl enable mongod
         ```
      - Install MongoDB Database Tools.
        ```bash
        wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.7.3.deb
        sudo apt install ./mongodb-database-tools-*-100.7.3.deb
        ```
   - Restore Tiki's product data from a local MongoDB instance to the MongoDB on the virtual machine.
     - Transfer json from local to VM via Gcloud
     ```bash
     gcloud compute scp tiki-products.bson quoccong-workspace@tiki-instance:/home/username --zone=asia-east2-a
     ```
     - Restore data to mongodb
     ```bash
     mongorestore --db=tiki-products --collection=products /home/username/tiki-products.bson
     ```
     - After restore data to mongodb, We trying to import data from db and upload to Bucket
     ```bash
        #export db to json
        mongoexport --collection=products --db=tiki-products --out=export-db.json

        #Remove the object id since Bigquery do not accect special characters.
        jq 'del(._id)' export-db.json > tiki_without_id.json

        #Upload json file to bucket which has been created.(Must to login)
        gcloud compute scp /home/username/tiki_without_id.json gs://tiki-bucket
     ```

3. **Creating Data Backup**:
   - Perform a complete synchronization of all products from MongoDB to Google Cloud Storage as a backup.

4. **Designing BigQuery Data Warehouse**:
   - Architect the schema and structure within BigQuery to accommodate Tiki's product dataset.

5. **Developing Data Mart**:
   - Construct a data mart focused on sellers and their products, intended for the Data Analysis (DA) team.

6. **Connecting to Data Studio**:
   - Establish a connection between BigQuery and Data Studio.
   - Create a dashboard displaying key insights:
     - Total products sold across major categories.
       ![alt](https://github.com/congtranquoc/Tiki-GCP/blob/57fd9e6fb04f062370eac0b8cf2a5f9adb577cb3/images/top-categories.PNG)
  
     - Total china products has been sold:
       ![alt](https://github.com/congtranquoc/Tiki-GCP/blob/2c243b39e5603ce5443a6ea5f3b6b3df69a3a08f/images/top-china-products.PNG)
            
     - Distribution of products from Chinese brands across categories.
       ![alt](https://github.com/congtranquoc/Tiki-GCP/blob/2c243b39e5603ce5443a6ea5f3b6b3df69a3a08f/images/distribution.PNG)
       
     - Correlation between product ratings and prices.
     - Top 10 sellers and their listed products' quantities.
       ![alt](https://github.com/congtranquoc/Tiki-GCP/blob/2c243b39e5603ce5443a6ea5f3b6b3df69a3a08f/images/top-sellers.PNG)




## Implementation Steps

Follow these steps to successfully execute the project:

1. **Setting up Compute Engine and MongoDB**:
   Configure a Compute Engine instance and install MongoDB.
   
2. **Restoring Data**:
   Migrate Tiki's product data from a local MongoDB instance to the MongoDB on the Compute Engine VM.

3. **Data Synchronization**:
   Synchronize data to Google Cloud Storage for robust backup.

4. **Designing BigQuery Schema**:
   Plan and implement an effective schema in BigQuery for Tiki's product data.

5. **Developing Data Mart**:
   Build a specialized data mart centered around sellers and their products.

6. **Creating Data Studio Dashboard**:
   Establish a seamless connection between BigQuery and Data Studio.
   Design a dashboard with insightful visualizations.

For detailed instructions and code examples, refer to the provided code files.

## Important Note

This project focuses on synchronizing Tiki's product data with Google Cloud's Data Warehouse using BigQuery. It encompasses various technical aspects such as Compute Engine setup, MongoDB management, ETL processes, and data visualization. The project aims to empower data analysis and facilitate informed decision-making.
