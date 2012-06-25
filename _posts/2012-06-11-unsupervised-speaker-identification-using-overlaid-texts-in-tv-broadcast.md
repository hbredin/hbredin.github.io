---
layout: post
title: "Unsupervised Speaker Identification using Overlaid Texts in TV Broadcast"
tagline: InterSpeech 2012
description: "Interspeech 2012"
category: 
- publications
tags: 
- reproducible_research
---
{% include JB/setup %}

This is the *"reproducible results"* webpage for the paper:

**Unsupervised Speaker Identification using Overlaid Texts in TV Broadcast**  
*Johann Poignant, Hervé Bredin, Viet Bac Le, Laurent Besacier, Claude Barras and Georges Quénot.*  
InterSpeech 2012 | September 9-13, 2012 | Porland, Oregon.

----

All the necessary material (source code and data) to reproduce the results reported in Tables 3 to 6 will be available for download here when the data is officially and freely distributed by the organizers of the [REPERE challenge](http://www.defi-repere.fr/) (ETA: January/February 2013).

<div class="alert alert-block alert-error">
  <a class="close" data-dismiss="alert" href="#">×</a>
  <h4 class="alert-heading">Warning!</h4>
  The archive below contains <strong>everything but the groundtruth annotation</strong> (and the script is therefore not fully functional).
	
	Please <strong>drop me an email</strong> if you'd like me to send you an update when the groundtruth annotation is available.
</div>

Download [interspeech2012.tar.gz](/download/interspeech2012.tar.gz).

----

**Expected output of the script**

	=============================================================================
	  Unsupervised Speaker Identification using Overlaid Texts in TV Broadcast
	-----------------------------------------------------------------------------
	                Johann Poignant, Hervé Bredin, Viet Bac Le, 
	            Laurent Besacier, Claude Barras and Georges Quénot.
	=============================================================================

	Tables 3 & 4: |#####################################################|
	+-----------+-------------+-------+-----------+--------+------------+
	|  Speakers | Propagation |  EGER | Precision | Recall | F1-Measure |
	+-----------+-------------+-------+-----------+--------+------------+
	|    All    |      M1     | 0.444 |   0.805   | 0.582  |   0.675    |
	|    All    |      M2     | 0.419 |   0.821   | 0.607  |   0.698    |
	|    All    |      M3     | 0.387 |   0.777   | 0.639  |   0.702    |
	| No anchor |      M1     | 0.317 |   0.883   | 0.720  |   0.793    |
	| No anchor |      M2     | 0.288 |   0.903   | 0.749  |   0.819    |
	| No anchor |      M3     | 0.284 |   0.892   | 0.753  |   0.817    |
	+-----------+-------------+-------+-----------+--------+------------+
	Table 3: Name propagation performance, full cond.

	+-----------+-------------+-------+-----------+--------+------------+
	|  Speakers | Propagation |  EGER | Precision | Recall | F1-Measure |
	+-----------+-------------+-------+-----------+--------+------------+
	|    All    |     SID     | 0.488 |   0.601   | 0.551  |   0.575    |
	|    All    |      M3     | 0.387 |   0.777   | 0.639  |   0.702    |
	|    All    |   M3 + SID  | 0.272 |   0.779   | 0.770  |   0.775    |
	| No anchor |     SID     | 0.612 |   0.470   | 0.444  |   0.457    |
	| No anchor |      M3     | 0.284 |   0.892   | 0.753  |   0.817    |
	| No anchor |   M3 + SID  | 0.227 |   0.807   | 0.834  |   0.820    |
	+-----------+-------------+-------+-----------+--------+------------+
	Table 4: Supervised (SID) vs. unsupervised (M3) speaker
	identification and their combination (M3+SID), full cond.

	Table 5: |#########################################################|
	+-----------+------------+-------+-----------+--------+------------+
	|  Speakers | Condition  |  EGER | Precision | Recall | F1-Measure |
	+-----------+------------+-------+-----------+--------+------------+
	|    All    |  Standard  | 0.467 |   0.820   | 0.556  |   0.663    |
	|    All    | Full video | 0.387 |   0.777   | 0.639  |   0.702    |
	| No anchor |  Standard  | 0.309 |   0.885   | 0.724  |   0.797    |
	| No anchor | Full video | 0.284 |   0.892   | 0.753  |   0.817    |
	+-----------+------------+-------+-----------+--------+------------+
	Table 5: Effect of condition on M3 performance.

	Table 6: |##########################################################|
	+-----------+-------------+-------+-----------+--------+------------+
	|     SD    | Propagation |  EGER | Precision | Recall | F1-Measure |
	+-----------+-------------+-------+-----------+--------+------------+
	|  Perfect  |   Perfect   | 0.235 |   1.000   | 0.765  |   0.867    |
	|  Perfect  |      M1     | 0.236 |   0.980   | 0.764  |   0.858    |
	| Automatic |      M1     | 0.330 |   0.891   | 0.703  |   0.786    |
	| Automatic |      M2     | 0.303 |   0.910   | 0.731  |   0.810    |
	| Automatic |      M3     | 0.309 |   0.885   | 0.724  |   0.797    |
	+-----------+-------------+-------+-----------+--------+------------+
	Table 6: Effect of speaker diarization (SD) and name
	propagation errors (standard condition, without anchors).