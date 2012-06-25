---
date: '2012-01-04 09:14:21'
layout: post
title: 'Community-driven Hierarchical Fusion of Numerous Classifiers  Application to Video Semantic Indexing'
tagline: ICASSP 2012
category: publications
tags: 
- graph-based approach
- multimodal fusion
- video indexing
---

This is a paper to be presented at [the 37th International Conference on Acoustics, Speech, and Signal Processing (ICASSP)](http://www.icassp2012.org/) in Kyoto, Japan (March 25 - 30, 2012)

We deal with the issue of combining dozens of classifiers into a better one.

Our first contribution is the introduction of the notion of communities of classifiers. We build a complete graph with one node per classifier and edges weighted by a measure of similarity between connected classifiers. The resulting community structure is uncovered from this graph using the state-of-the-art Louvain algorithm.

Our second contribution is a hierarchical fusion approach driven by these communities. First, intra-community fusion results in one classifier per community. Then, inter-community fusion takes advantage of their complementarity to achieve much better classification performance.

Application to the combination of 90 classifiers in the framework of TRECVid 2010 Semantic Indexing task shows a 30% increase in performance relative to a baseline flat fusion.
