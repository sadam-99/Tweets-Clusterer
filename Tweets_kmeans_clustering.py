# Tweets K-means CLustering Code written By:
            # SHIVAM GUPTA (NET ID: SXG190040)
            # BHAVYA SREE BOMBAY (NET ID- BXB180036)

import re 
import numpy as np
import copy
import math
import sys
import random

# Data Preproceesing for the extraction of thw tweets
def tweets_preprocessing(tweet_path):
    tweets = []
    # with open(tweet_path, encoding="utf8") as f:
    with open(tweet_path) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        for t in lines:
            tw = t.split('|')[2].split('http://')[0]
            tw = re.sub('@|#', '', tw)
            tw = tw.lower()
            tweets.append(tw)
            
    return tweets

# Calculating Jaccard Distance
def jaccard_distance(x,y):
    intersection = list(set(x) & set(y))
    Inters = len(intersection)
    Union = list(set(x) | set(y))
    Un = len(Union)
    overlap = (float(Inters) / Un)
    return round(1 - overlap , 4)

# output in the form of cluster no. and the number of tweets in that cluster.
def output_clusters(cluster_no,k,tweet_id):
    cluster_id=[]
    print("Cluster Number : Number of Tweets")
    for i in range(k):
        cluster_id.append([j for j, c in enumerate(cluster_no) if c == i])	
        tw_no=[y for y in cluster_id[i]]
#         print("The number of tweets in cluster number in", i+1)
        print(i+1, ":",len([tweet_id[y] for y in tw_no]))


#computing the sum of squared errors           
def sum_squared_error(centroids, tweet_text, k, l):
    sum_sq_error=0
    for i in range(k):
        for j in range(len(tweet_text)):
            sum_sq_error = sum_sq_error + math.pow(jaccard_distance(tweet_text[j],centroids[i]),2)
    print(sum_sq_error)


# updating the centroids at every iteration
def centroid_update(tweet_id, cluster,tweet_text,l,k):
    ind=[]
    upd_centweet_id=[]
    updated_tweet_centroid=[]
    for i in range(k):
        ind.append([j for j, clus in enumerate(cluster) if clus == i])
        cl=ind[i]
     
        # cl gives the indices of the elements of every cluster k

        if (len(cl) != 0):
            tweet=[tweet_text[s] for s in cl]
            similarity_dist =[ [jaccard_distance(tweet[i],tweet[j]) for j in range(len(cl))] for i in range(len(cl))]
            
            total_similarity=[sum(i) for i in similarity_dist]
            # index of the point closer to all the other points	
            upd_centweet_id.append( cl[(total_similarity.index(min(total_similarity)))]) 
    updated_tweet_centroid=[tweet_id[x] for x in upd_centweet_id]
    return updated_tweet_centroid




# k-means clustering implementation from scratch
def kmeans_clustering(tweet_id, centroids,tweet_text,l,k):
    count=0
    for iter in range(50):
        count=count+1
        cluster_id=[]
        cou = 0
        for i in range(l):
            cou += 1
#             print(cou)
            dist=[jaccard_distance(tweet_text[i].split(' '), centroids[j].split(' ')) for j in range(k)]
            dist_id= dist.index(min(dist))
            cluster_id.append(dist_id)
#             print(cluster_id)
 
        centroids_new = centroid_update(tweet_id, cluster_id,tweet_text,l,k)
        print("Updated Centroids after iteration no. ", iter + 1)
        print(centroids_new) 
        cen=[tweet_text.index(item) for item in centroids]
        if (cen == centroids_new):
            print("Kmeans clustering converged after iteration no. = {} for the value of k = {}".format(iter + 1, k))
            break
        centroids_id = copy.deepcopy(centroids_new)
        centroids = []
        for tweet_index in centroids_id:
            centroids.append(tweet_text[tweet_index])
#         print(centroids)

        output_clusters(cluster_id,k,tweet_id)
        print("Sum of square Error after iteration no.", iter + 1)
        sum_squared_error(centroids,tweet_text,k,l)
	
	
if __name__ == '__main__':
    tweet_path = r"tweets datasets\foxnewshealth.txt"
    # tweet_path = r"tweets datasets\usnewshealth.txt"
    # tweet_path = r"tweets datasets\msnhealthnews.txt"
    k = 5
    tweets = tweets_preprocessing(tweet_path)
    length = len(tweets)
    tweet_ids = []
    for i in range(len(tweets)):
        tweet_ids.append(i)
    # tweet_ids
    centroids_tweets = random.sample(tweets, k)
    # centroids_tweets
    # Running the k-means clustering on the tweets
    kmeans_clustering(tweet_ids, centroids_tweets,tweets,length, k)
