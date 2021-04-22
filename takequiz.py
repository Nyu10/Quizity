#!/usr/bin/python
print ("Content-type: text/html\n")
import cgi

data = cgi.FieldStorage()
quiz_id=data["id"].value


def create_dict(lines):
        data={}
        lines= lines.split('\n')
        for line in lines:
                items=line.split(',')
                if len(items)>1:
                        keys= items[0]
                        data[keys] = items[1:]
        return data

info=open("id.txt").read()
info=create_dict(info)

if quiz_id not in info:
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
                </header>
                <br><br>
                <h1 align="center" style="color:red;">ERROR: Information provided is not correct!</h1>
                <h2 align="center" style="color:red;"> Sorry, but the Quiz ID that you have provided is incorrect. <br>
                Please click on Quizity on the banner to be redirected to the homepage to try again. </h2>
                </body>
                </html>
                """)

else:
        id = "quiz/"+data["id"].value + ".txt"
        name = data["name"].value

        quiz = open(id).read()
        quiz = create_dict(quiz)


        quiz_name=open(id).read()
        quiz_name=quiz_name.split('\n')
        quiz_name=quiz_name[0]


        print ("""
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
</header>
<h2 align=center>Quiz: """+quiz_name+"""</h2>

<h3 align=center> Student Name:  """)

        print (name + "</h3><hr> ")
        print ("""
<table align=center><tr><td>
<form action = "check.py" method = "POST">
""")

        i=1
        while i<=len(quiz):
                a=str(i)
                print ('<p style="font-weight:bold;">'  + a+ ".   "+(quiz[a][0]) + "</p>")
                print ('<p style="padding-left:50px;">' +" A: "+ (quiz[a][1]) + "<br> B: " + (quiz[a][2]) + "<br>C: " + (quiz[a][3]) + "<br>D: " + (quiz[a][4]) +"</p>")
                print ("""
                <select style="margin-left: 45px;" name = "q"""+a+"""">
                <option value = "A"> A </option>
                <option value = "B"> B </option>
                <option value = "C"> C </option>
                <option value = "D"> D </option>
                </select> <br><hr>
                """)
                i+=1

        print ("""<br>
<input type="hidden" name="id" value="""+quiz_id+""">
<input type="hidden" name="name" value="""+name+""">
<input type="submit" value="Submit"><br>
        </form>

</td></tr><table>
        </body>
        </html>
""")
