---
date: '2011-10-17 10:00:12'
layout: post
title: Introducing PyAFE toolkit
categories:
tags: audio fingerprinting, evaluation, release, PyAFE, python
---

**PyAFE** stands for **Py**thon **A**udio **F**ingerprinting **E**valuation.

It is a **Python** toolkit that I developed for the _Evaluation_ work-package of the [Quaero](http://quaero.org) project. It is designed as a modular piece of software, in ordre to be easilly extended in the future:
    
 * two modules provides the necessary functions to **parse** groundtruth and detection XML files.
 * the core module includes the actual implementation of **audio fingerprinting score** metrics. Computation of the number of correct detections, misses and false alarms is obviously also available.


It is freely available as **open-source** software, part of a larger framework dealing with audio fingerprinting described in the (just published) article:

<blockquote>
<a href="/download/pdfs/Ramona2011.pdf">A Public Audio Identification Evaluation Framework for Broadcast Monitoring</a><br/>
Mathieu Ramona, Sébastien Fenet, Raphaël Blouet, Hervé Bredin, Thomas Fillon, Geoffroy Peeters
</blockquote>



PyAFE can be downloaded from the official website at [pyafe.niderb.fr](http://pyafe.niderb.fr).
