---
layout: page
title: "MSc Internship - Unsupervised person identification"
description: ""
group: "students"
tags: 
- intership
---
{% include JB/setup %}

## Identification faiblement ou non supervisée du locuteur dans les séries TV

Du fait de nombreuses campagnes « Speaker Recognition Evaluation » (SRE) organisées par NIST depuis 1996 et d’initiatives plus récentes telles que ESTER, ETAPE et REPERE, de nombreuses études ont été consacrées à la reconnaissance du locuteur dans des conversations téléphoniques ou les journaux radio- et télé-diffusés. La grande majorité de ces travaux modélise ce problème comme un problème d’apprentissage supervisé où, à partir d’un corpus d’apprentissage annoté manuellement en locuteurs (« qui parle quand? »), un modèle acoustique est entrainé pour chacun des locuteurs. 

**Parole préparée vs. parole spontanée.** Alors que la parole est préparée (voire lue) dans les journaux télévisées — avec de longs tours de parole —,  les interactions entre les personnages des séries télévisées sont plus spontanées et entraînent des tours de parole beaucoup plus courts.
Le premier objectif du stage est donc d’adapter aux séries télévisées un système existant d’identification supervisée du locuteur prévue pour les journaux radio- et télé-diffusés.

**Identification supervisée vs. faiblement supervisée vs. non-supervisée.** Un deuxième axe de recherche concerne l’identification du locuteur par des méthodes d’apprentissage faiblement voire non supervisée [Bredin 2014]. Le corpus de test envisagé pour ce stage contient environ 200 épisodes de la séries BBC EastEnders. Pour chacun d’eux, la liste des personnages réellement présents dans l’épisode est disponible et constitue une annotation faible et ambigüe du contenu. On s’inspirera des travaux existants en reconnaissance des visages [Cour 2009] pour parvenir à tirer profit de ces annotations  ambigües et potentiellement bruitées. De même, les transcriptions manuelles des dialogues sont disponibles pour la totalité des épisodes. Ces dialogues constituent une source intéressante pour identifier de façon non supervisée les locuteurs par propagation des noms prononcées aux tours de parole des personnages nommés [Poignant 2012].

**Du document à la collection.** Un première étape de segmentation et regroupement des tours de parole en locuteurs (speaker diarization) semble indispensable pour parvenir à l’identification non supervisée des locuteurs. Classiquement, ce regroupement est obtenu à l’échelle du document (e.g. émission par émission). Or, dans le cadre des séries télévisées, un même personnage peut être présent dans plusieurs épisodes (voire tous les épisodes) et il faudra adapter les outils existant au LIMSI [Tran 2011] capables de traiter une collection entière. 

### Durée et lieux du stage

5 à 6 mois au LIMSI/CNRS à Orsay.

### Contact

Hervé Bredin - Chercheur CNRS au LIMSI - bredin__at__limsi.fr

### Références

[Cour 2009] Timothee Cour, Benjamin Sapp, Chris Jordan, Ben Taskar. Learning from Ambiguously Labeled Images. CVPR 2009. 

[Tran 2011] Viet-Anh Tran, Viet Bac Le, Claude Barras, Lori Lamel. Comparing Multi-Stage Approaches for Cross-Show Speaker Diarization. INTERSPEECH 2011.

[Poignant 2012] Johann Poignant, Hervé Bredin, Viet Bac Le, Laurent Besacier, Claude Barras, Georges Quénot. Unsupervised Speaker Identification using Overlaid Texts in TV Broadcast. INTERSPEECH 2012.

[Bredin 2014] Hervé Bredin, Anindya Roy, Viet-Bac Le, Claude Barras. Person Instance Graphs for Mono-, Cross- and Multi-Modal Person Recognition in Multimedia Data. Application to Speaker Identification in TV Broadcast. En révision — International Journal of Multimedia Information Retrieval.
