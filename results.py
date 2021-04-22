#!/usr/bin/python3
print ("Content-type: text/html\n")

import cgi
data=cgi.FieldStorage()

id=data['id'].value
pin=data['pin'].value


info=open('id.txt').read()

def create_dict(lines):
        data={}
        lines= lines.split('\n')
        for line in lines:
                items=line.split(',')
                if len(items)>1:
                        keys= items[0]
                        data[keys] = items[1:]
        return data

import statistics
def average(x):
        sum = 0
        for y in x:
                sum += float(y)
        return sum/(len(x))

def mode(n):
        new = {}
        for x in n:
                if x in new:
                        new[x] += 1
                else:
                        new[x] = 1
        most = n[0]
        for x in new:
                if new[x] > new[most]:
                        most = x
        maxfreq=new[most]
        new.pop(most)
        for x in new:
                if maxfreq == new[x]:
                        return "Multiple Modes"
        return most


info=create_dict(info)

if id not in info:
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
                <h2 align="center" style="color:red;"> Sorry, but the Quiz ID and/or Quiz Pin that you provided is incorrect. <br>
                Please click on Quizity on the banner to be redirected to the homepage to try again. </h2>
                </body>
                </html>
                """)
elif info[id][0]!=pin:
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
                <h2 align="center" style="color:red;"> Sorry, but the Quiz ID and/or Quiz Pin that you provided is incorrect. <br>
                Please click on Quizity on the banner to be redirected to the homepage to try again. </h2>
                </body>
                </html>
                """)


else:
        quiz_name=open("quiz/"+id+".txt").read()
        quiz_name=quiz_name.split('\n')
        quiz_name=quiz_name[0]


        list=open("result/"+id+".txt").read()
        d={}
        list=list.split('\n')
        for item in list:
                if len(item)>1:
                        item=item.split(',')
                        d[item[0]]=item[1]
        grade={}
        for key in sorted(d.keys()):
                grade[key]=d[key]


        g=[]
        students=[]
        for item in list:
                if len(item)>0:
                        item=item.split(',')
                        g.append(float(item[1]))
                        students.append(item[0])




        list=g
        students=sorted(students)

        stats="""
<table border = 1>
<tr>
        <th> Statistics </th>
        <th> Value </th>
</tr>
<tr>
        <td> Mean </td>
        <td> """ +  str(average(list)) + """ </td>
</tr>
<tr>
        <td> Standard Deviation </td>
        <td> """ +  str(statistics.pstdev(list)) + """ </td>
</tr>
<tr>
        <td> Mode </td>
        <td> """ +  str(mode(list)) + """ </td>
</tr>
<tr>
        <td> High </td>
        <td> """ +  str(max(list)) + """ </td>
</tr>
<tr>
        <td> Low </td>
        <td> """ +  str(min(list)) + """ </td>
</tr>
<tr>
        <td> Range </td>
        <td> """ +  str(max(list) - min(list)) + """ </td>
</tr>
<tr>
        <td> Median </td>
        <td> """ +  str(statistics.median(list)) + """ </td>
</tr>

</table>"""


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
<br>
<table align="center">
<tr>
        <th width="400" >QUIZ INFORMATION </th> <th width="400">QUIZ SCORE INFORMATION </th>
</tr>
<tr>
        <td valign="top" align="center" >Quiz Name:  """+quiz_name+"""<br> Completed Quiz :"""+str(len(g))+"""  </td><td align=center>"""+stats+""" </td>
</tr>
</table>
<br>
<br>
<table align="center" border=1>

<tr>
        <th>Student Name</th><th>Grade</th>
</tr>
""")

i=0
while i <len(list):
        print("""
        <tr> <td>"""+students[i]+""" </td><td>"""+str(list[i])+"""</td>
        </tr>""")
        i+=1

print("""
</table>
</html>
""")
