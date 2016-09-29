---
published: true
title: HTML 초급 2일차
layout: post
category: programming
permalink: /programming_kr/html_5
---

### Bootstrap 활용 과제

bootstrap의 주어진 기능만을 최대한 활용해서 작성한 레이아웃

#### index.html

```html

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="css/index.min.css">
</head>
<body>

<!-- 상단의 네비게이션 (메뉴바) -->
<nav class="navbar navbar-default navbar-no-margin">
    <!-- 넹비게이션 바의 내용 -->
    <div class="container-fluid">

        <!-- 상호명 아이콘 -->
         <div class="navbar-header">
           <a href="" class="navbar-brand">
             <img src="images/logo.png">
           </a>
         </div>


        <!-- 네비게이션 정보를 오른쪽 정렬로 설정해준다 -->
        <ul class="nav navbar-nav navbar-right">
          <li><a href="">방 검색</a></li>
          <li><a href="">관심목록</a></li>
          <li><a href="">방등록</a></li>
          <li><a></a></li>
          <li><a href="">공인중개사 가입</a></li>
          <li><a href="">회원가입 및 로그인</a></li>
        </ul>
    </div>
</nav>

<!-- 본문 -->
<!-- 상단 이미지 -->
<div class="index-content">

  <div class="jumbotron index-image-container">
    <div class="caption-container">
        <p class="caption-top">850만 며이 선택한 대표 부동산 앱</p>
        <p class="caption-bottom">우리, 살고 싶은 데서 살자</p>
    </div>
  </div>
</div>
</body>
</html>

```

<br>

#### Sass 파일

```css

// 배경화면 이미지 경로 설정
// DIV 태그의 고정높이 설정
// 배경화면의 위치를 가운데 그리고 top은 0px로 고정
// 배경화면 반복 없음
// 배경화면 기본 색을 검은색으로 표시, 이미지가 없는 위치에는 검은색으로 표현
// 위치는 상대적 -> 절대적이면 표시가 안 됨

.index-content
  .index-image-container
    background-image: url(../images/index-bg.jpg)
    height: 678px
    background-position:  50% top
    background-repeat: no-repeat
    background-color: black
    position: relative

// 상단의 Navbar와 하단의 이미지에 틈이 발견되어서 틈을 제거

.navbar-no-margin
  margin-bottom: 0px

//폰트 색을 하얀색으로 설정
//위치를 절대값으로 설정
//배경이 가운데로 설정되어 있기 때문에 글씨 중심도 가운데로 설정
//상단 위치는 고정값 설정
//글씨들의 위치가 오른쪽 정렬로 설정
//글씨들이 가운데를 중심으로 -420 마진값으로 알맞은 위치로 찾아감

.caption-container
  color: white
  position: absolute
  left: 50%
  top: 160px
  text-align: right
  margin-left: -420px

// 글씨 묶음 중 상단 글씨의 크기와 문구 줄 간격 설정

  .caption-top
    font-size: 22px
    margin-bottom: 0px

// 글씨 묶음 중 하단 글씨의 크기 설정

  .caption-bottom
    font-size: 36px

```





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
