# MSDS 498 Data Engineering Capstone Project <br />
Project Team: Janna Weng, Alex Newell, John Gentry, Scott Kaufman, Joel Riesen, Ching Pan

## Project Overview

Kicking off the project in Week 1 our team was focused on finding a technology that we believed would be a disruptor in the field of AI & ML. One technology that we found intriguing was prediction models due to their wide applicability across multiple industries.  We ultimately settled on prediction models as our technology to explore for the project, because we believe that as AI & ML systems mature in the coming decade, prediction models will become ingrained in every aspect of our daily lives.  Prediction models are already capable of predicting large weather events, such as excessive drought and fire seasons, as well as financial distriss - prediction models are becoming an increasingly utilized method for businesses to predict outcomes and mitigate risk.  
<br />
Our team decided to build a model that could produce a score(prediction) indicating if a customer would be likely to default on a loan, based on specific characteristics of the individual customers.
<br />
## Architecture Overview <br />
To complete our project, we used a combination of different AWS services that allowed us to run, train and publish our results to a production web environment. In addition to AWS SageMaker Studio, we used AWS Lambda and API gateway services that allowed us to connect the application to our training data, and generate results that could immediately be published to our web environment, hosted by AWS.  The AWS AppRunner service allowed us to complete that final step of publishing our prediction results to our hosted web service. Additionally, using Postman the team can monitor API usage within the App, helping to test the AppRunner web service as well as the local service using the Rest API.  
<br />
Architecture Diagram: 

![MLOps drawio_v2](https://user-images.githubusercontent.com/18123748/142734692-ec53b8d0-acc8-45ec-bf03-5eb558e21932.png)


<br />

## Installation & Required Packages

Required Packages
<br />
- Flask
- pandas
- numpy
- boto3
- tabulate
- gensim
- requests
<br />

To use this project, first clone the repo on your device using the command below:

git init
<br />

git clone https://github.com/jgentry10/MSDS498_GroupProject

<br />

## Assignment Instructions & Requirements:

Your team will make a “bet” on a technique or technology in the free resources you have been exposed to.  Maybe you want to demo step-by-step how to train a Tensorflow model on a TPU on GCP, or how to train an RNN model using AWS Sagemaker.  Pick something you think will “move the needle” in the next two years. Alumni of the program are counting on you to give them a demo of what skills they need to invest in.  Soon, you will be alumni and will be hoping other students will show you a demo of something that you can learn from in the coming years when you graduate.

Deliverables:
1. Github project with source code and README.md explaining the project your group works on.  The README.md should be of professional quality and use a business writing style.
1. Five-minute final demo video showing how it works.  
 - This demo video should be submitted into group discussion for the week it is due.  This will allow other students to learn from each other and exchange ideas.
 - The demo needs to be very technical and show exactly how to accomplish a task, i.e. you need to teach someone step by step.  (Think about a cooking show where a chef demonstrates how to make chocolate chip cookies.  This needs to be at the same level of detail).

(Optional, but recommended:)
1. Publish source code the Northwestern Data Engineering Capstone Github Organization
1. Publish your demo to Northwestern Data Engineering Capstone YouTube channel and your own channel. The video should be at least 1080p with 16:9 aspect ratio.
1. Create a post with a link to source code and video and share via Linkedin.  Add the following hashtags: #northwestern #dataengineering #capstone

---

