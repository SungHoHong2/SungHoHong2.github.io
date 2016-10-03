---
published: true
title: Learning Bootstrap
layout: post
category: programming
permalink: /programming_kr/html_5_3
---

### Container Class

Bootstraps container class will responsively add margins, center, and wrap the content
<br> the div container automatically locates on the center
<br> the margins grow when the overall width increases

| class name |  detail   |
| -- | -- |
| container |  margins are added and maintain the div in the center |
| container-fluid | there are no margins |


### Wire Framing Design

Bootstrap gives 12 columns to work with
From the example below

- Title spans 12 columns
- Lead and image both have 6 columns each
- Bottom data have 4 columns each
- if the columns are used for making empty spaces, use col-md-offset-1

```html

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Blasting off Bootstrap</title>

  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>

</head>
<body>

<div class="container">

    <!-- The title page makes up 12 Colums  -->
    <div class="row">
        <div class = "col-md-12">
            <h1>Blasting off with bootsrap</h1>
        </div>
    </div>

    <!-- Divide the column into two  -->
    <div class="row">
        <div class="col-md-6">
            <h2>THe fasted way to space </h2>
            <p>Make your way to space in the comfort of your own rocket, elevator or transporter</p>
            <button>Take a tour</button>
            <button>Book tickets now</button>
        </div>
        <div class = "col-md-6">
            <img src = "image/frisk1.jpg"/>
        </div>
    </div>

    <!-- Divide into 3 columns -->
    <div class="row">
        <div class="col-md-4">
            <h3>book today</h3>
            <p>etcfas afsdfadsf sdfdsafasdfsadf asdfsadfsadfas dsafasdfsd</p>
        </div>
        <div class="col-md-4">
            <h3>Go Anywhere</h3>
            <p>etcfas afsdfadsf sdfdsafasdfsadf asdfsadfsadfas dsafasdfsd</p>
        </div>
        <div class="col-md-4">
            <h3>RocketBus&reg</h3>
            <p>etcfas afsdfadsf sdfdsafasdfsadf asdfsadfsadfas dsafasdfsd</p>
        </div>
    </div>
</div>

</body>
</html>

```

### Adjusting Smaller Resolutions

| Grid Size | Grid Class | Offset Class | Screen size |
| -- | -- | -- | -- |
| Extra Small |  .co-xs-* | .col-xs-offset-* | 0px + |
| Small |  .co-sm-* | .col-sm-offset-* | 768px + |
| Medium | .co-md-* | .col-md-offset-* | 992px + |
| Large | .col-lg-* | col-lg-offset-* | 1200px+ |     


```html

<!-- hide the image in some sizes -->
<div class = "col-md-6 hidden-sm hidden-xs">
    <img src = "image/frisk1.jpg"/>
</div>

<!-- show image in certain sizes -->
<div class = "col-md-6 visible-sm visible-xs">
    <img src = "image/maria1.jpg"/>
</div>

<div class="clearfix"></div>
<div class="row">
    <div class="col-sm-4 col-xs-10 col-xs-offset-1 col-sm-offset-0">
        <h3>book today</h3>
        <p>etcfas afsdfadsf sdfdsafasdfsadf asdfsadfsadfas dsafasdfsd</p>
    </div>
    <div class="col-md-4 col-sm-4 col-xs-6">
        <h3>Go Anywhere</h3>
        <p>etcfas afsdfadsf sdfdsafasdfsadf asdfsadfsadfas dsafasdfsd</p>
    </div>
    <div class="col-md-4 col-sm-4 col-xs-6">
        <h3>RocketBus&reg</h3>
        <p>etcfas afsdfadsf sdfdsafasdfsadf asdfsadfsadfas dsafasdfsd</p>
    </div>
</div>

```

### Addons

- well class give element a gray background and a rounded gray border
- button class designs the buttons

``` html

<div class = 'rows well'></div>
<button class='btn btn-lg'>button</button>

```

### Navigation
