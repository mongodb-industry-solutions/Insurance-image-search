# Insurance-image-search

The python notebook included in this repository contains a basic script that lets the user perform similarity search using [Atlas Vector Search](https://www.mongodb.com/products/platform/atlas-vector-search).
The steps outlined in the code are the following:

1. Define an image embedder based on the pytorch version of squeezenet
2. Download and save to file the public "car damage" dataset. The dataset contains images of car damages. Make you you move the folder from your downloads into the same folder as your GitHub repo.
3. Connect to MongoDB Atlas. Replace the code with your username, password and cluster.
4. Create the Search index in Atlas following the instructions of [this](https://www.mongodb.com/developer/products/atlas/building-generative-ai-applications-vector-search-open-source-models/?hideMenu=1) tutorial (Step 4) and using the following configuration

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

6. Get image embeddings and load them to Atlas
7. Type "crashed windshield" or anything related to car accidents into Google Image search and save one of the images into the car_damage folder with the name test.jpg.
8. Run an image similarity query

Here's an example of a query of an image found online

![](test.jpg)

And its output

![](top_5.png)
