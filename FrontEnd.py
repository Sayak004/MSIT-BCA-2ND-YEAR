# to open/create a new html file in the write mode
f = open('index.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<style>
body{
    # background-color:magenta;
    background-image:linear-gradient(90deg,cyan,purple);
}
h2{
    font-family:fantasy;
    font-size:48px;
    color:ghostwhite;
    # text-align:center;
    letter-spacing:13px;

}
p{
    font-family:fantasy;
    font-size:25px;
    color:ghostwhite;
    text-align:center;
    letter-spacing:3px;
}
</style>
<body>
<br>
<marquee scrollamount="22">
<h2>Welcome MSIT BCA</h2>
</marquee>
<p>We are learning python programming language</p>

</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()
print("HTML GENERATED")