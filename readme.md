# Tweets_kmeans_clustering.py-
        ## Variables.
                - 'tweet_path' : The path for the Tweet file
                - 'k' : The number of Clusters (Value k)
                - 'tweets': The main text of the tweets to calculate the similarity.
                - 'length': The total number of tweets in the text file.
                - 'tweet_ids':  the IDs of the Tweets
                - 'centroids_tweets'= The Initial Tweets Centroids(Seeds) Taken Randomly)
        
        ## Functions:
                - tweets_preprocessing: Data Preproceesing for the extraction of thw tweets   
                - jaccard_distance : Calculating Jaccard Distance
                - output_clusters: output in the form of cluster no. and the number of tweets in that cluster.
                - sum_squared_error: computing the sum of squared errors
                - centroid_update: updating the centroids at every iteration
                - kmeans_clustering- k-means clustering implementation from scratch

# Tweets Datasets Used for testing-
        ## foxnewshealth.txt, msnhealthnews.txt, usnewshealth.txt, bbchealth.txt
		## There is no need to change the path for the tweets datasets, just uncomment/comment line numbers: 114, 115, 116
       

# How to run the code:
        ## Run command python Tweets_kmeans_clustering.py on anaconda prompt.
        


