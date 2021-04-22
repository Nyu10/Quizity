#!/usr/bin/python3
print('Content-type: text/html\n')

import cgi
data=cgi.FieldStorage()

id=data['id'].value
questions=data['questions'].value
pin=data['pin'].value
quiz_name=data['quiz_name'].value

ans=data['ans'].value

open('id.txt','a').write(id+","+pin +"\n")

name="quiz/"+str(id)+".txt"

text=quiz_name+"\n"+str(ans)+"\n"+questions
open(name,'w+').write(text)

print("""
<!DOCTYPE html>
<html>
<head>
        <title> Quizity </title>
        <style>
        header{
                background-image: url("https://d29fhpw069ctt2.cloudfront.net/photo/52205/preview/npreview_1280x1280.jpg");
                padding: 25px;
                text-align: center;
                color: white;
                margin-left: -10px;
                margin-top: -10px;
                margin-bottom: 5px;
                margin-right: -10px;
                font-size:60px;
                font-weight:bold
                }
</style>
</head>
<body style="background-color:#89D0FF;">

<header>
<a href="http://homer.stuy.edu/~dzhang10/quizity.html" style="color:white;text-decoration:none;">QUIZITY </a>
</header <br>

<h1 align=center>Your quiz is now live!</h1>
<h3 align=center>Click on Quizity in the banner above to be directed to the homepage.<br>
To take the test, enter the Quiz ID below and Name in the TAKE Column. </h3>

<h2 align=center style="color:red;">Please write down your Quiz ID and PIN as there will be no other way to get it later. </h2>
<h3 align=center >Your Quiz ID is: """+id+""" <br>Your Quiz PIN is: """+pin+""" </h3>
</body>
</html>
""")