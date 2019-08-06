# FORUM IS HOSTED ON - :rocket:
[ASKJUET.PYTHONANYWHERE.COM](http://askjuet.pythonanywhere.com)
:+1: :metal: :tada:
## Requirements
* Django 	 = 2.2.3

* Python 	 = 3.6

* Crispy Forms = 1.7.2
### Caution - 
* This project was previously tested on Django 2.0.5 but due to sql migration bug of that version, we have officially shifted to Django 2.2.3 make sure you update django version in your machine

***

## About Project
We, the Pantomath, have tried creating a project to solve the real-life problem of our faculty members of conveying information to the students. If any teacher wanted to convey any message to any batch then they first had to tell it to the Class Representative (CR) and then the CR would further convey it to the batch students. In this process there is a lot of information gap that leads to wrong analysis of the information. So, with our little knowledge about Web Development we tried to create one stop for students and faculty members that would let teachers directly post about anything and the students could get the information directly from here. The post would include: 
	
**TITLE**	: Title of the Post (Required)

**CONTENT**	: All information about the post (Required)

**DATE**	: Date and time of the post 

**URL**		: To provide any link to website (Optional)

**DOCS**	: To provide any study material (Optional)

***

# Description of Project

## Introduction Page
The very first page that comes up is the introduction page. Here you can select wheather you are a faculty member or student. You can select either of the option and continue accordingly. If you are a faculty meneber then you will be directed to the login page where you can **SignIn** and provide the content to the students by filling up the form.

<img src="images/2.png" width="500" >

## Home Page
Once you click on the faculty button a form will appear where you can signin using your id and password which is provided in the file named **id-pass.txt**. Once you are signed in the home page will appear where  there are different options like:  

* Menu : On clicking on this buttton you will be redirected to the inroduction page where you have to again select wheather you want to login as faculty member or continue as student. If you again click on faculty button then a prompt box appears where you can directly select wheather you want to write a post, go to the home page or directly move to the forum.
<img src="images/3_1.png" width="500">

* Notice: This button will direct you the main form of the post. Here the faculty members can fill up the form accordingly and post it. The content will be posted on the home page and an email would also be sent to the registered email ids. 

<img src="images/1.png" width="500" > <img src="images/4_1.png" width="500" > <br/>

**NOTE**: If you want to add your own email id you can do it by simply writing your email in space highlighted.

<img src="images/4_2.png" width="500">

* Forum : We will be explaining the forum feature later on.

* About : Lastly if you want to contact us you can use our GitHub and LinkdIn id. 

##  Detailed Post Features
Whenever a faculty uploads a  new post, he can view the post by simply clicking on it. A new tab will be opened and a detailed description of the post will be shown here. The faculty member can also perform update and delete operarions on the post by just simply clicking on the buttons provided on the top right corner. A point to be noted here is that the admin who has uploded the post can only perform any changes to the post, in any other admin account the option of update and delete will not be shown. Once any changes are made in the post it will directly visible on the home page. 

<img src="images/5_1.png" width="500">
