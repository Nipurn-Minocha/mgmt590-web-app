# mgmt590-web-app

Link to acces the app:
   https://webapp1-flmmaqbd2a-uc.a.run.app/
   
This webapp can help the user to get answer through their questions given a context . This also 
provides additional facility of showing list of models available and their ability to add or delete 
a model. User can get their answer just by providing question and context. Additionaly, he/she can 
upload a file with question and answer and get all the answers in a nice tabular format displayed.

![image](https://user-images.githubusercontent.com/54888893/120767859-9cadec00-c4e9-11eb-8f28-ffbfc8d0070a.png)

On the background, user is connected to the streamlit webapp which could be connected to restapi server
and database but here our webapp is connected to restapi which in turn is connected to the database to make 
it stateless. 

---

## Screenshots

![image](https://user-images.githubusercontent.com/54888893/120764612-530fd200-c4e6-11eb-8682-093836c2467e.png)

By default distilled BERT is added in our model. User can manually enter any model from hugging face transformers library to his list of available models.

![image](https://user-images.githubusercontent.com/54888893/120764954-b39f0f00-c4e6-11eb-815a-122ff6493ef9.png)

List of all models is shown in above pic.

![image](https://user-images.githubusercontent.com/54888893/120765251-024ca900-c4e7-11eb-9fba-62976b3a6701.png)

You can select from the list above and delete the model which you don't want

![image](https://user-images.githubusercontent.com/54888893/120765428-332cde00-c4e7-11eb-89de-1180d08372f8.png)

Now we see that only 1 model is present. Lets do some QnA now.

![image](https://user-images.githubusercontent.com/54888893/120765852-a171a080-c4e7-11eb-8e16-3c98d3fa0ec3.png)

You can also upload list of question and context in csv format to get answers on a go !!!!

![image](https://user-images.githubusercontent.com/54888893/120766173-f7dedf00-c4e7-11eb-9488-22447c66a2dc.png)

---

# Build App locally

## Windows Installation

1.	Download Docker.
2.	Double-click InstallDocker.msi to run the installer.
3.	Follow the Install Wizard: accept the license, authorize the 
4.	installer, and proceed with the install.
5.	Click Finish to launch Docker.
6.	Docker starts automatically.
7.	Docker loads a “Welcome” window giving you tips and access.
8.	to the Docker documentation.


## Mac Installation
1.	Double-click Docker.dmg to open the installer, then drag the 
2.	Docker icon to the Application folder.
3.	Double-click Docker.app in the Application folder to start Docker.
4.	Click the Docker menu to see Preferences and other options
5.	Select About Docker to verify that you have the latest version



# Creating a Docker File
## Step 1
Create a file called Docker File and edit it using vim. Please note that the name of the file has to be "Dockerfile" with "D" as capital.
## Step 2
Build your Docker File using the following instructions.
```
FROM ubuntu 
MAINTAINER demousr@gmail.com 
RUN apt-get update 
RUN apt-get install –y nginx 
CMD [“echo”,”Image created”] 
```
## Step 3
Save the file
## Step 4
The Docker file can be built by the following command
## Syntax:
```
docker build  -t ImageName:TagName dir
```
Options

1.	-t − is to mention a tag to the image

2.	ImageName − This is the name you want to give to your image.

3.	TagName − This is the tag you want to give to your image.

4.	Dir − The directory where the Docker File is present.

# Adding files to the Docker Container
For copying the files from the host to the docker container :

1. First, set the path in your localhost to where the file is 
   stored.

2. Next set the path in your docker container to where you want 
   to store the file inside your docker container.

3. Then copy the file which you want to store in your docker 
   container with the help of CP command. 

ex:
```
 sudo docker cp /home/(name)/(folder_name)/(file_name)  (container_id):/(to_the_place_you_want_the_file_to_be)
```

