---
date: '2011-02-10 16:27:31'
layout: post
slug: jobdependencygrap
status: publish
title: Visualizing SGE Job Dependency Graph
wordpress_id: '509'
categories:
- Code
tags:
- release
- sge
---

I use Sun Grid Engine a lot and often need to submit a job that depends on the output of other jobs. _qsub_ option _--hold\_jid_ does just that: it tells the scheduler not to process a job until another job is completed.

Therefore, I use it. **A LOT**.

Sometimes, it even gets difficult to know which job is waiting for which job to complete.
Here comes a simple script I wrote, that happens to be very helpful!

The [JobDependencyGraph-1.1](/download/JobDependencyGraph-1.1.tgz) script allows to get a graphical representation of the jobs you submitted to a Sun Grid Engine (nodes), along with their _--hold\_jid_ dependencies (edges).

![Job dependency graph](/images/JobDependencyGraph.png "Job dependency graph")

Each node is a job (ID and name). Greenish nodes are running jobs. Edges are _--hold\_jid_ dependencies.

It was tested with [GE](http://wikis.sun.com/display/GridEngine/Home) 6.2u4 and [Graphviz](http://www.graphviz.org/) dot version 2.6. You might need to modify it slightly to match your _qstat_ output format if you use a different version.

I thought of writing this script after reading [this blog post](http://chihungchan.blogspot.com/2007/07/sge-grid-job-dependency.html), where Chi Hung Chan basically does the opposite of this script (i.e. converts a graph into a collection of qsub calls).

Hope it's useful!
