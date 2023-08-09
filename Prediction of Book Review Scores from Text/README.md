# Prediction of Book Review Scores from Text

# Project: 
Using a massive Amazon book review dataset, I create a random forest classifier that can predict numerical book review scores from textual features 
such as reviews and review summaries, while also employing numerical review helpfulness scores. The model achieves a significant and notable degree of accuracy. I employ the TextBlob module to assist me with my natural language processing work, and I make extensive use of its sentiment analysis functionality. The data distributions are visualized via barcharts, whereas the accuracy of the model is assessed via confusion matrices.

# How to Use:
Due to the massive size of the file that I used, I am unable to include it here, however the data can be downloaded from this link: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews. 
There are two files present, and the one to download is the Books_rating.csv file. Once that is downloaded, simply put the file in the working directory of the notebook and run the notebook. However, this 
notebook does require a lot of memory to run, so much so that I had to run it in stages. It may be the case that you can run it in one sitting, though it will be a very lengthy process.

# Data:
The data used for this project is approximately three million Amazon book reviews uploaded to Kaggle by Mohamed Bekheet and available here: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews (Bekheet, M., 2022). The data was collected by R. He, and J. McAuley in their work Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering (R. He, J. McAuley, 2016), and by J. McAuley, C. Targett, J. Shi, A. van den Hengel (J. McAuley, et al., 2015) in their work Image-based recommendations on styles and substitutes, and by Mohamed Bekheet himself through the Google Books API. 

# License:
My work itself is free to use, and the license for the data I acquired from Kaggle is a CC0: Public Domain license. Please cite all appropriate persons if using their data.

# References:
Bekheet, M. (2022, Sept (updated)). Amazon Books Reviews. Kaggle. https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews, accessed on 06/25/2023. 

R. He, J. McAuley (2016). WWW.  Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering.

J. McAuley, C. Targett, J. Shi, A. van den Hengel (2015). SIGIR. Image-based recommendations on styles and substitutes.


