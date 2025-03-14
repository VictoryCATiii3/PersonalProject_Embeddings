# Personal Embedding Project

## Overview

In this project we made a simple GUI that allows us to enter various phrases and see how their embeddings relate to each other in multidimensional vector space.

## Specifications

In order to generate vector embeddings we will be using all-MiniLM-L6-v2 which we asssume is downloaded and held in a "models" directory which is located next to our PersonalProject_Embeddings directory. However if you wish to modify this code to work with a different embedding model this can be easily done by modifying the **model** variable of the EmbeddingClasses.py file.

## Notes

The all-MiniLM-L6-v2 model defines the model in 384 Dimensional vector space, we then use numpy's dot product and normal vector feature to get the consine similarity of the vectors to each other.
