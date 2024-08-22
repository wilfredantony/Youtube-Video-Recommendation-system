# Youtube-Video-Recommendation-system
The project's aim is to build an small application which replicates the youtube recommendation system.
The following steps can be done to achieve the application
  ##EXTRACION
      >The data can be extracted from the youtube itself.
      >First get the api key from the Google cloud console.
      >Then extract the video by genres(I took only five genres).
  ##AWS
      >Create an s3 bucket in the AWS to store the data.
      >Create a database in the AWS and connect it.
          -After creating a Database take the endpoint as it is the host.
      >Configure AWS CLI to connect to the AWS from local vs code.
          -Access ID
          -Secret Access key
          -Location
          -File type.
  ##PREPROCESSING OF DATA
       >As we collected based on genre now take every video and append it to the list.
       >As we are going to seperate by the tags we only take the tags.
             -Use Lemmatization to get the root words.
             -Remove the stopwords.
             -Convert non hashable types to strings.
             -Drop the duplicates.  
             -Upload the data to S3 bucket.
  ##MODEL TRAINING
       >Here I have clustered the based on the genres that I have extracted.
       >Use TfidfVectorizer to change the data of the selected column to numerical matrix.
       >Apply Principle Component Analysis(PCA) for dimensionality reduction for visualization.
       >Then cluster the data using KMeans clustering.
       >After model training save the data to Database and save teh models as a pickle file.
  ##STREAMLIT APPLICATION
       >Create a connection to the AWS database.
       >Load the models which are in the form of pickle files.
       >Design a search bar where if a word is given then it would undergo the model training.
       >Then if it matches the cluster it will give the results.
  ##Finally deploy the app using amazon EC2
