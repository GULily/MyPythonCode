#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:55:28 2017

@author: yili
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


## convert the first image to a vector
img1 = Image.open('TEST_Image.pgm').convert('L')
plt.imshow(img1, cmap = plt.get_cmap("gray"))

imagearray1 = np.array(img1)
original_shape = imagearray1.shape
flat1 = imagearray1.ravel()
facevector1 = np.matrix(flat1)
print(facevector1.shape)

## reverse: convert an image-vector back into a .jpg image.
f = plt.figure()
plt.imshow(facevector1.reshape(original_shape), cmap = plt.get_cmap("gray"))
plt.show()
f.savefig("FaceBackTest.jpg")



## place all the vectorized images into one matrix
paths = [] # store all paths
facematrix = np.zeros([400, 10304])
count = 0
for i in range(1,41):
    for j in range(1,11):
        fullpath='FACESdata/s'+str(i)+'/'+str(j)+'.pgm'
        paths.append(fullpath)
        img=Image.open(fullpath).convert('L')
        imagearray = np.array(img)
        # flatten the imagearray into 1-dim
        flat = imagearray.ravel()
        # convert it to a matrix
        facevector = np.matrix(flat)
        facematrix[count,:] = facevector
        count += 1 
        
print(count)
#print(facematrix.shape)
#print(facematrix)

## transpose so that each column is an image
facematrix_t=np.transpose(facematrix)
#print(facematrix_t.shape)

# the mean of all of the columns
mean = np.mean(facematrix_t, axis=1)
#print(mean.shape)
#print(mean)
f = plt.figure()
plt.imshow(mean.reshape(original_shape), cmap = plt.get_cmap("gray"))
plt.show()
f.savefig("mean_face.jpg")



## substract the mean of all of the columns to get a normalized matrix
Norm_Face_Matrix = facematrix_t - mean.reshape([10304,1])
#print(Norm_Face_Matrix.shape)
print(Norm_Face_Matrix)


## get the reduced covariance matrix based on Turk and Pentland:
Norm_Face_Matrix_t = np.transpose(Norm_Face_Matrix)
CovMatrix = np.matmul(Norm_Face_Matrix_t, Norm_Face_Matrix)
#print(CovMatrix.shape)

## get eigenvalues and eigenvectors
eig_vals, eig_vecs = np.linalg.eig(CovMatrix)

## sort eigenvalues and eigenvectors
idx = eig_vals.argsort()[::-1]
eig_vals = eig_vals[idx]     
eig_vecs = eig_vecs[:, idx]
#print(eig_vals)
#print(eig_vecs[:,0:5])


## choose top k eigenvectors
k = int(input("Input k: "))
while k < 1 or k > 50:
    print('k should between 1-50. Try again.')
    k = int(input("Input k: "))

print(k)
eigenface_matrix = np.matmul(Norm_Face_Matrix, eig_vecs[:,0:k])
eigenface_matrix = np.real(eigenface_matrix)
print(eigenface_matrix)

f = plt.figure()
for i in range(k):
    plt.imshow(eigenface_matrix[:,i].reshape(original_shape), cmap = plt.get_cmap("gray"))
    plt.show()
    f.savefig("writeup/first5/eigenface"+str(i)+".jpg")



## Test 1
test = Image.open('writeup/test1/TEST_Image.pgm').convert('L')
plt.imshow(test, cmap = plt.get_cmap("gray"))
plt.show()

test_face = np.array(test).ravel() - mean.ravel()
#print(test_face)

## Transpose the eigenface matrix and then multiply it by the test face vector.
test_k_values = np.matmul(np.transpose(eigenface_matrix), np.transpose(test_face))

## Do this same exact process with all of the faces in the database (normalized).
v = np.zeros([400, k]) # values for each face in the database
dist = [0 for i in range(400)] # distance between the test face and each face in the database

for i in range(400):
    temp = np.matmul(np.transpose(eigenface_matrix), Norm_Face_Matrix[:,i])
    v[i,:] = np.transpose(temp)
    dist[i] = np.sum(np.square(v[i,:] - np.transpose(test_k_values)))

## Find the image with the smallest Euclidean distance
num_file = dist.index(min(dist))
print("Find Closest File Number: ", num_file, "\tDistance: ", min(dist))
result = Image.open(paths[num_file]).convert('L')
f = plt.figure()
plt.imshow(result, cmap = plt.get_cmap("gray"))
plt.show()
f.savefig("writeup/test1/PREDICTED_Image.jpg")



## Test 2
test = Image.open('writeup/test2/TEST_Image.pgm').convert('L')
plt.imshow(test, cmap = plt.get_cmap("gray"))
plt.show()

test_face = np.array(test).ravel() - mean.ravel()
#print(test_face)

## Transpose the eigenface matrix and then multiply it by the test face vector.
test_k_values = np.matmul(np.transpose(eigenface_matrix), np.transpose(test_face))

## Do this same exact process with all of the faces in the database (normalized).
v = np.zeros([400, k]) # values for each face in the database
dist = [0 for i in range(400)] # distance between the test face and each face in the database

for i in range(400):
    temp = np.matmul(np.transpose(eigenface_matrix), Norm_Face_Matrix[:,i])
    v[i,:] = np.transpose(temp)
    dist[i] = np.sum(np.square(v[i,:] - np.transpose(test_k_values)))

## Find the image with the smallest Euclidean distance
#num_file = dist.index(min(dist))
num_file = dist.index(sorted(dist)[1])
print("Find Closest File Number: ", num_file, "\tDistance: ", sorted(dist)[1])
result = Image.open(paths[num_file]).convert('L')
f = plt.figure()
plt.imshow(result, cmap = plt.get_cmap("gray"))
plt.show()
f.savefig("writeup/test2/PREDICTED_Image.jpg")