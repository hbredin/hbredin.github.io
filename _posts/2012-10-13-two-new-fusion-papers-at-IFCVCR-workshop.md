---
layout: post
title: "Two new papers dealing with multimodal fusion"
tagline: "ECCV 2012 / IFCVCR workshop"
description: "ECCV 2012 / IFCVCR workshop"
category: 
- publications
tags: 
- multimodal fusion
---
{% include JB/setup %}


**Hierarchical Late Fusion for Concept Detection in Videos**  
*Tiberius Strat, Alexandre Benoit, Hervé Bredin, Georges Quénot, Patrick Lambert.*  
ECCV 2012, Workshop on Information Fusion in Computer Vision for Concept Recognition | October 13, 2012 | Firenze, Italy.  

We deal with the issue of combining dozens of classifiers into a better one, for concept detection in videos. We compare three fusion approaches that share a common structure: they all start with a classifier clustering stage, continue with an intra-cluster fusion and end with an inter-cluster fusion. The main difference between them comes from the first stage. The first approach relies on a priori knowledge about the internals of each classifier (low-level descriptors and classification algorithm) to group the set of available classifiers by similarity. The second and third approaches obtain classifier similarity measures directly from their output and group them using agglomerative clustering for the second approach and community detection for the third one.


**Fusion of Speech, Faces and Text for Person Identification in TV Broadcast**  
*Hervé Bredin, Johann Poignant, Makarand Tapaswi, Guillaume Fortier, Viet Bac Le, Thibault Napoleon, Hua Gao, Claude Barras, Sophie Rosset, Laurent Besacier, Jakob Verbeek, Georges Quénot, Frédéric Jurie, Hazim Kemal Ekenel.*  
ECCV 2012, Workshop on Information Fusion in Computer Vision for Concept Recognition | October 13, 2012 | Firenze, Italy.  

The REPERE challenge is a project aiming at the evaluation of systems for supervised and unsupervised multimodal recognition of people in TV broadcast. In this paper, we describe, evaluate and discuss QCompere consortium submissions to the 2012 REPERE evaluation campaign dry-run. Speaker identification (and face recognition) can be greatly improved when combined with name detection through video optical character recognition. Moreover, we show that unsupervised multimodal person recognition systems can achieve performance nearly as good as supervised monomodal ones (with several hundreds of identity models).
