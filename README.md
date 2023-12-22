1. Clone the repository to your computer
2. download h5 model here https://drive.google.com/file/d/14i4fYDo_Sa6_ZU6gU86kyEiy_HPcddo7/view?usp=sharing
3. This code uses Google cloud Storage, so you must have your own gcs bucket with the name "waste-classifi-bucket", create a folder in the bucket called "predict". and you must also have a credentials file, change the file name to "ch2-pr636-credentials.json"
4. after that , you install all dependencies by opening the terminal then typing pip install -r requirements.txt
5. if all already done ,  run the application by typing python main.py
6.by default the server will run on localhost with port 5000, then open in the browser http://localhost:5000/, for the initial display
7.http://localhost:5000/check, to check the bucket, if successful it will appear OK
8. http://localhost:5000/predict, for uploading waste images.
