#!/usr/bin/python3
print('Content-type: text/html\n')
import cgi

data=cgi.FieldStorage()
name=data['name'].value
id=data['id'].value


key=open('quiz/'+id+'.txt')
lines=key.readlines()
key=lines[1]
key=key.split('\n')
key=key[0].split('-')

def create_dict(lines):
        data={}
        lines= lines.split('\n')
        for line in lines:
                items=line.split(',')
                if len(items)>1:
                        keys= items[0]
                        data[keys] = items[1:]
        return data

quiz_name= "quiz/"+id+ ".txt"
quiz = open(quiz_name).read()
quiz = create_dict(quiz)

i=1
given=[]
while i<=len(key):
        a=str(i)
        given.append(data['q'+a].value)
        i+=1

i=0
correct=0
wrong=[]
while i<=len(key)-1:
        if given[i]==key[i]:
                correct+=1
        else:
                wrong.append(str(i+1))
        i+=1

score=int(correct/len(key)*100)


file="result/"+str(id)+".txt"
text=str(name)+','+str(score)+","+str(wrong)+"\n"
open(file,'a').write(text)


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
<h2 align=center> You have completed the Quiz! <br> To go back to homepage, you can click on Quizity in the banner above.</h2><br>
<h1 align=center> Your score for this quiz is: """+str(score)+"""%</h1> <br>

<h3 align=center>The following table shows you the questions, correct answers, and your answer.<br> The questions that you have answered incorrectly are shown in red.</h3>
<table border=1 align=center>
<tr>
        <th>Question</th><th>Correct Answer</th><th>Your Answer</th>
</tr>""")

i=1
while i <=len(key):
        a=str(i)
        if key[i-1]==given[i-1]:
                print("<tr><td> " + a+".  "+(quiz[a][0])+"<br>")
                print("A: " + (quiz[a][1]) + "<br>")
                print("B: " + (quiz[a][2]) + "<br>")
                print("C: " + (quiz[a][3]) + "<br>")
                print("D: " + (quiz[a][4]) + "</td> ")
                print("<td align=center>"+key[i-1]+"</td>")
                print("<td align=center>"+given[i-1]+"</td>")
        else:
                print("""<tr style="color:red;" > <td> """ + a +""".  """+(quiz[a][0])+"""<br>""")
                print("A: " + (quiz[a][1]) + "<br>")
                print("B: " + (quiz[a][2]) + "<br>")
                print("C: " + (quiz[a][3]) + "<br>")
                print("D: " + (quiz[a][4]) + "</td> ")
                print("<td align=center>"+key[i-1]+"</td>")
                print("<td align=center>"+given[i-1]+"</td>")

        i+=1

print("""
</table>

</body>
</html>

""")
