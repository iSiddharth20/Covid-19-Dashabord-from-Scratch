#!/usr/bin/python3

# Importing Data into the program
from DataDivide import data_complete,data_sum
from DataSource import last_update

str1 = """<!DOCTYPE html>
<html style="background-color: #000000;">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Dashboard</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,700&amp;display=swap">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=ABeeZee">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Muli">
    <link rel="stylesheet" href="assets/css/Bootstrap-DataTables.css">
    <link rel="stylesheet" href="assets/css/Data-Table-1.css">
    <link rel="stylesheet" href="assets/css/Data-Table.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.15/css/dataTables.bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/css/LinkedIn-like-Profile-Box.css">
    <link rel="stylesheet" href="assets/css/Navigation-Clean.css">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="stylesheet" href="assets/fonts/fontawesome-all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
</head>

<body class="text-dark flex-shrink-1 flex-fill justify-content-center align-items-center align-content-center align-self-center flex-wrap">
    <nav class="navbar navbar-light navbar-expand-md navigation-clean" style="height: 22px;background-color: rgb(26,27,30);">
        <div class="container"><a class="navbar-brand" href="index.html" style="color: #f2f5f8;font-size: 25px;height: 45px;font-family: Elite Danger;">Covid-19 India Dashboard</a><button data-toggle="collapse" class="navbar-toggler" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                            <div
                                class="collapse navbar-collapse" id="navcol-1">
                                <ul class="nav navbar-nav ml-auto">
                                    <li class="nav-item" role="presentation"></li>
                                    <li class="nav-item" role="presentation"><a class="nav-link" data-bs-hover-animate="pulse" href="https://www.kaggle.com/isiddharth/covid19-india-dataset" style="color: #f2f5f8;font-size: 25px;height: 40px;font-family: Elite Danger;">Open Source Dataset</a></li>
                                    <li
                                        class="nav-item" role="presentation"><a class="nav-link" data-bs-hover-animate="pulse" href="about.html" style="color: #f2f5f8;font-size: 25px;height: 40px;font-family: Elite Danger;">About Developers</a></li>
                                </ul>
                            </div>
        </div>
    </nav><img class="img-fluid bg-dark d-inline-flex flex-grow-1 flex-shrink-1 flex-fill align-items-center align-content-center align-self-center flex-wrap visible" src="assets/img/LandingBG.png" />
    <div class="container">
<br><br>
          """
str2 = """ 
<br><br> 
</div>
        <h3 class="text-center"> Last Update :
"""
part1 = str1 + data_sum + str2 + last_update

str1 = """ 
        </h3>
        <h4 class="text-center">
        Data Source :
        <a href = "https://www.mohfw.gov.in/"> 
        Ministry of Health and Family Welfare 
        </a>
        </h4> 
        <br><br>
    <div class="container">

          """

str2 = """ 
</div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/bs-init.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js"></script>
    <script src="assets/js/Bootstrap-DataTables.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.js"></script>
    <br><br>
</body>
</html>"""

part2 = str1 + data_complete + str2

full_webpage = part1 + part2

# Saving the HTML Code to HTML File
path = '../'
filename = 'index.html'
f = open(path+filename, "w")
f.write(full_webpage)
f.close()