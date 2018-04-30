## Summary

Author: Yi Li

This notebook uses PCA to do dimension reduction on 400 face images (each one has 10304 pixels) to find the top k eigenfaces. After compressing images (dimension reduction), I find the most similar face image of a given face image by calculating the euclidian distance between each pair of the given image and the others in the database.
