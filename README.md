# Insurance Image Search

This demo showcases the functionalities and features of the Insurance Image Search application. It leverages MongoDB's Vector Search capabilities to perform similarity searches on insurance-related images. By embedding and comparing image vectors, this demo enables users to efficiently search for visually similar images, streamlining processes in the insurance industry.

## Where MongoDB Shines?

- **Vector Storage and Similarity Search:** MongoDB’s flexible schema and [Atlas Vector Search](https://www.mongodb.com/products/platform/atlas-vector-search) capabilities make it ideal for storing image embeddings and running efficient similarity comparisons. In this demo, the embeddings of car crash images are seamlessly stored and queried to find visually similar images, enabling faster claims assessments and decision-making.

- **Rich Query Capabilities:** MongoDB combines vector search with traditional database queries, allowing structured fields (e.g., claim costs, dates, car models) to be queried alongside unstructured data. This hybrid search model streamlines claim cost estimation by enabling comprehensive searches within a single database.

- **Scalability and Performance:** MongoDB’s distributed architecture ensures the ability to scale horizontally, making it easy to handle large datasets of image embeddings and metadata, ensuring lightning-fast searches and high availability.

- **Ease of Integration for AI Workflows:** MongoDB pairs seamlessly with AI/ML use cases by acting as the backbone for storing and analyzing embeddings. This enables smooth integration of pre-trained ML models with real-time or batch similarity searches.

Learn more about MongoDB [here](https://www.mongodb.com/docs/manual/).

## Tech Stack

### Frontend
- **Jupyter Notebooks** are used to create interactive data exploration and visualization tools in this demo, providing an environment for running code and displaying results inline. This setup is ideal for iterative development and analysis.

### Backend
- **Database**: MongoDB Atlas a fully managed cloud database service, is chosen for its ease of use, scalability, and ability to efficiently handle and query JSON-like documentary data. Its built-in vector search capabilities enable fast and accurate similarity searches on image embeddings.

- **Language**: Python utilized for its robust ecosystem of libraries suited for machine learning and data processing tasks.

## Prerequisites

Before setting up the Insurance Image Search demo, ensure that you have the following prerequisites installed and configured on your system:

- [Python 3.10 or above](https://www.python.org/downloads/)
- [MongoDB Atlas Cluster](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/) 

## Creating Search Index

To optimize your data retrieval times and enable efficient search operations, you might need to create an index, particularly if using MongoDB Atlas Search.

Setup a Search Index:
1. Navigate to your MongoDB Atlas Cluster.
2. Go to the "Collections" tab and select the appropriate collection.
3. Open the "Search" tab and click on "Create Search Index".
4. Use the Following Index Definition:

Copy and paste the JSON document below into the index configuration field to define an efficient search configuration for your collection:
```json
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "embedding": {
        "dimensions": 1000,
        "similarity": "cosine",
        "type": "knnVector"
      }
    }
  }
}
```

## Adding Environment Variables

To connect your Jupyter Notebook to your MongoDB cluster, you'll need to update the uri variable with the correct connection string for your cluster.

### Steps to Update the Connection URI:
1. Locate Your Connection String:
Log in to MongoDB Atlas and navigate to your cluster. Find the connection string provided for your cluster.

2. Modify the URI in Your Notebook:
Replace the placeholder text in the uri variable with your actual connection details. Ensure you update the username, password, and cluster name as per your MongoDB Atlas configuration.

```
uri = "mongodb+srv://<username>:<password>@<clustername>.n0kts.mongodb.net/?retryWrites=true&w=majority"
```

# Example

Here's an example of a query of an image found online

![](test.jpg)

And its output

![](top_5.png)
