---
published: true
title: HTML 초급 2일차
layout: post
category: programming
permalink: /programming_kr/html_5
---

``` css

/* 배경 이미지 위치 */
div{
  width : 100%;
  height: 505px;
  border : 1px solid black;
  background-image : url('frisk1.jpg');
  background-repeat : no-repeat;
  background-position: center center;
}


/* 테두리를 결정하는 요소 */
div{ border-width: 3px 4px 5px 6px /* 상 우 하 좌 */  }

div.border{
  border-color: red;
  border-style: solid double dotted dashed;
}


/* 리스트 앞 bullet 이미지 지정 */
ul{
  list-style-image: url('images/mic.png');
  list-style-position: inside;
}

/* COL GROUP */
table{
  border-collapse: collapse;
}

tr, th, td {
  border : 1px solid black;
  padding : 5px 10px;
}

th{
  background-color: grey;
  color : white
}

table > colgroup > col.col-1{
  color : blue;
  background-color : blue;
}

table > colgroup > col.col-3{
  border-right-style : double;
  border-width: 5px;
  border-color: gray;
}

/* 화면 표시 방법  */
div { display : inline }
div { display : inline-block }
div { display : none }
div { overflow : hidden }


/* Position */
div{ position: static, relative, fixed, absolute }

div{
    display : inline-block;
    margin : 0 auto;
    top: 50%;
    transform : translateY(-50%);
    position: relative;
}

```

<br>

### Sass

CSS 전처리기, CSS문법이 과거에 나왔기 떄문에 개발자들에게 가독성이 있는 구조로 작성한 후 CSS를 해석하는 처리기

```html

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="form-sass.min.css"/>

</head>
<body>
   <form action="">
      <h3>회원가입</h3>
      <fieldset>
          <legend>기본정보</legend>
          <div class="form-control"><label>id </label><input placeholder="아이디를 입력하세요" type="text"></div>
          <div class="form-control"><label>password</label> <input type="password"></div>
          <div class="form-control"><label>email</label> <input type="email"></div>
      </fieldset>

      <fieldset class="second_field">
        <legend>선택입력</legend>
        <div class="form-control"><label>나이</label><input type="text"></div>
        <div class="form-control"><label>주소</label><input type="text"></div>
        <div class="form-control"><label>자기소개</label><textarea name="" id="" cols="60" rows="10" placeholder="자기소개"></textarea></div>
      </fieldset>
      <button class="btn-join"type="submit">회원가입</button>
   </form>
</body>
</html>

```


```css

body
  margin: 20px
  font-size: 13px
  color: #333

input, textarea
  border-color: #ccc
  border-width: 1px
  border-style: solid

h3
  text-align: center
  margin-bottom: 0px

fieldset
  margin-bottom: 20px
  border-width: 1px

  .form-control
    margin-bottom: 5px

    label
      display: inline-block
      width: 100px
      vertical-align: top

button.btn-join
  width: 100%
  height: 30px
  border: none
  background: #666
  color: white
  cursor: pointer

```
<br>

### Bootstrap 기본

```html




```
