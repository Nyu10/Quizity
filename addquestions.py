#!/usr/bin/python3
print ("Content-type: text/html\n")
import cgi
data=cgi.FieldStorage()
i = data['number'].value
quiz_name=data["quiz_name"].value
counter = 1
pin=data['pin'].value
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
</header>""")

print("""<h1 align="center">Quiz Name:""" +str(quiz_name)+ """ </h1>
<h2 align="center" style="color:red;">Attention: Do not use apostrophes, quotes, or commas when entering questions or the answer choices! </h2>
<br>
 <form action="savequestions.py" method = "POST" >
        <input type="hidden" name = "number" value ='""")

print (str(i) + "'>")
print (""" <input type="hidden" name="pin" value='"""+str(pin)+"""'>""")
print (""" <input type="hidden" name="quiz_name" value='"""+str(quiz_name)+"""'>
<table align=center>
<tr><td>
""")

while counter <= int(i):
        print (str(counter)+'.   '+""" QUESTION:  <input type="text" size="150" name = 'q"""  + str(counter)+ """'><p style="padding-left: 86px;">
                          A: <input type="text" size="80" name = 'a""" + str(counter) + """'> <br>
                          B: <input type="text" size="80" name = 'b""" + str(counter) + """'> <br>
                          C: <input type="text" size="80" name = 'c""" + str(counter) + """'> <br>
                          D: <input type="text" size="80" name = 'd""" + str(counter) + """'></p>
                          <p style="padding-left:70px;"> Correct Answer:        <select name = "answer"""+str(counter)+"""">
                                <option value = "A"> A </option>
                                <option value = "B"> B </option>
                                <option value = "C"> C </option>
                                <option value = "D"> D </option>
                                </select><br><hr>
""")
        counter += 1
print ("""<input type="submit" value="Submit"><br>
        </form>
</td></tr>
</table>
        </body>
        </html>
""")