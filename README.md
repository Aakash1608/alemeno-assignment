# Backend and Frontend for Strip Color Detection

### Description

---

Welcome to my project! This repo consists of a Backend written in Django and a frontend to test the backend written in React. The backend has the Endpoint and logic to extract color from urine strip provided by the user.

### Installation

1. Setting up python virtual environment

   ```
   python3 -m venv <environment_name>
   ```
2. Clone the repo
3. Change into the root of the project directory

   ```
   cd alemeno_assignment
   ```
4. Activate the virtual environment and Install the requirements.txt file

   ```
   source ../<environment_name>/bin/activate
   pip install -r requirement.txt
   ```
5. Run the backend Server

   ```
   python manage.py runserver
   ```
6. For Frontend set up - change into frontend directory => install the packages => run the frontend script

   ```
   cd frontend
   npm i 
   npm run dev
   ```
7. To check the API using Postman. Send a post request to [http://127.0.0.1:8000/api/strip/](http://127.0.0.1:8000/api/strip/) and put the image with the key of 'image'.

---

### How does the Image processing works?

The following approach is based upon a certain format of image. To see a demo of image visit [image link](https://drive.google.com/file/d/1Kqd7ibor1kLZAeq8OO0mIPseXYzyXRCf/view?usp=sharing).

Following are the steps followed to process the image -

1. We crop the extra part of strip (the bottom part).

2. We detect the part of image that contains the colored strips the using edge detection.

3. Now we have narrowed down the search region, we divide the image into 10 part containing the different sub strips.

4. Using a open-cv function we extract the colour from the images

To see the code for the above explaination go in strip_detection directory and open utils.py file.
