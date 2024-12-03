# Final Project: Article Summarizer
_Complete the tasks in the Python Notebook in this repository. Make sure to add and push the pkl or text file of your scraped html (this is specified in the notebook)_

Rubric
+ (Question 1) Article html stored in separate file that is committed and pushed:                            1 pt
+ (Question 2) Polarity score printed with an appropriate label:     1 pt
+ (Question 2) Number of sentences printed:  1 pt
+ (Question 3) Correct (or equivalent in the case of multiple tokens with same frequency) tokens printed:    1 pt
+ (Question 4) Correct (or equivalent in the case of multiple lemmas with same frequency) lemmas printed:    1 pt
+ (Question 5) Histogram shown with appropriate labelling: 1 pt
+ (Question 6) Histogram shown with appropriate labelling: 1 pt
+ (Question 7) Cutoff score seems appropriate given histograms: 2 pts (1/score)
+ (Question 8) Summary contains a shortened version of the article (less than half the number of sentences): 1 pt
+ (Question 8) Summary sentences are in the same order as they appeared in the original article: 1 pt
+ (Question 9) Polarity score printed with an appropriate label: 1 pt
+ (Question 9) Number of sentences printed: 1 pt
+ (Question 10) Summary contains a shortened version of the article (less than half the number of sentences): 1 pt
+ (Question 10) Summary sentences are in the same order as they appeared in the original article: 1 pt
+ (Question 11) Polarity score printed with an appropriate label: 1 pt
+ (Question 11) Number of sentences printed: 1 pt
+ (Question 12) Thoughtful answer based on reported polarity scores: 1 pt
+ (Question 13) Thoughtful answer based on summaries: 1 pt
_____________________________________________________________________________________________________

# Jason A. Ballard

**Enterprise Data and AI Officer | Data Literacy Advocate | Educator in Professional Military Education**

Welcome! I'm Jason A. Ballard, an experienced data and AI integration leader currently serving as a Data and AI Officer for the US Army Combined Arms Center at Fort Leavenworth Kansas. My work bridges data science, AI strategy, and higher education, focusing on transforming decision-making through data literacy and innovation.

I invite you to explore my [GitHub repository](https://github.com/JBtallgrass), where I share insights, tools, and resources geared toward data literacy and advanced analytics in educational contexts. My projects emphasize practical solutions, open collaboration, and a commitment to enhancing data accessibility across teams.

## Key Areas of Focus
- **Data Strategy & Governance**: Developing frameworks that promote data-driven decision-making and cross-departmental data sharing.
- **AI & Analytics**: Leveraging data analytics and GenAI to unlock insights and drive transformational initiatives within Army University.
- **Data Literacy & Education**: Equipping leaders and students with data literacy skills critical for today's complex, data-rich environments.

Please don't hesitate to connect, collaborate, or contact me if our interests align. Let's make data-driven transformation a reality together.

## Linkedin: [Jason A. Ballard](https://linkedin.com/in/ballardjasona/) 

# Project Title: Module 7

[HTML File:]()

## Project Overview
This is an academic project supporting the Masters of Science in Data Analytics program at Northwest Missouri State University [NWMSU](https://www.nwmissouri.edu/academics/graduate/masters/data-analytics.htm)
The project supports the Web Mining and Natural Language Processing course requirements.

## Learning Objectives:
At the end of this module, students will be able to:

1. Build on core course concepts though the final project. (CO1, CO2, CO3, CO4, CO5, CO6)

## Table of Contents
- [Overview](#project-overview)
- [Instructions](#Instructions)
- [Questions](#Questions)
- [Commentary](#Commentary)
- [Requirements](#Requirements)
- [Installation](#installation)


## Instructions

Chose a topic that interests me- Fly fishing in the Ozarks of Missouri and Arkansas. 
Here is my article I will use [Fly Fishing the Ozarks] (https://intotheozarks.com/fly-fishing-in-the-ozarks/) for the following project.

##### Work this way until all tasks have been completed. 

## Questions
+ (Question 1) Article HTML stored in a separate file that is committed and pushed: 1 pt

+ (Question 2.1) Polarity score printed with an appropriate label: 1 pt.

+ (Question 2.2) Number of sentences printed: 1 pt.

+ (Question 3) Correct (or equivalent in the case of multiple tokens with the same frequency) tokens printed: 1 pt.

+ (Question 4) Correct (or equivalent for multiple lemmas with the same frequency) lemmas printed: 1 pt.

+ (Question 5) Histogram shown with appropriate labeling: 1 pt.

+ (Question 6) Histogram shown with appropriate labeling: 1 pt.

+ (Question 7) Cutoff score seems appropriate given histograms: 2 pts (1/score)

+ (Question 8.1) Summary contains a shortened version of the article (less than half the number of sentences): 1 pt.

+ (Question 8.2) Summary sentences are in the same order as in the original article: 1 pt.

+ (Question 9.1) Polarity score printed with an appropriate label: 1 pt.

+ (Question 9.2) Number of sentences printed: 1 pt.

+ (Question 10.1) Summary contains a shortened version of the article (less than half the number of sentences): 1 pt.

+ (Question 10.2) Summary sentences are in the same order as they appeared in the original article: 1 pt.

+ (Question 11.1) Polarity score printed with an appropriate label: 1 pt.

+ (Question 11.2) Number of sentences printed: 1 pt.

+ (Question 12) Thoughtful answer based on reported polarity scores: 1 pt.

+ (Question 13) Thoughtful answer based on summaries: 1 pt.


## Commentary


## For Future Analysis

## Requirements
a. Markdown introduction with name and clickable link is required

b. Markdown Section Headings for each Question are required

c. Execute your code before exporting HTML and pushing notebooks (See FAQ for help.)

d. Unexecuted code is not eligible for credit


### IMPORTANT: 

**ChatGPT 4o**  for coding, markdown language, and errors and **Grammarly** for editing and refine/validate my initial assessments.

### Installation of SpaCy: 
```bash
python -m venv .env
.env\Scripts\activate
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
### Dependencies utilized
```bash
# Required dependencies
import requests
import json
import pickle
from textblob import TextBlob
from spacytextblob import spacytextblob
import spacy
# Addtional Dependencies 
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
```
### Special thanks to: https://course.spacy.io/en/ 

### Additional analysis (experimentation with GenAI and foundations concepts)

### Data Visualizations

**Comments:** 

#### Word Cloud

**Comments:** 

#### Scatter Plot

**Comments:** 

#### Heat Map

**Comments:** 
