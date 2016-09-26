---
published: true
title: HTML 초급 1일차
layout: post
category: programming_kr
permalink: /programming_kr/html_5
---

### HTML의 기본구조

```html

  <!DOCTYPE html>
  <html>
    <head>
      <meta charset = "UTF-8">                                <!-- 웹페이지의 인코딩 방식 -->
      <meta http-equiv= "X-UA-Compatible" content= 'ie=edge'> <!-- IE 랜더링 방식을 최신으로 -->
      <link rel = "stylesheet" href= "style.css"></link>  
      <script src = "script.js" charset="utf-8"></script>
      <title> 제목 입력하는 부분 </title>      
    </head>
    <body>
       <!--  주석 입력하는 부분  -->
    </body>
  </html>

```
<br>

###  블록과 인라인

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset = 'utf-8'>
    <title> Document </title>
</head>
<body>

    <!-- 블록 요소 -->
    <h1>블록요소</h1>
    <p>p요소는 블록 형태입니다.</p>
    <div>div 요소 역시 블록속성입니다.</div>

    <!-- 인라인 태그 -->
    <strong> Strong 요소 </strong>
    <a> a 요소 </a>
    <span> span 요소 </span>

</body>
</html>

```

<br>

### 여러 가지 요소

| 태그 | 내용 |
|----|----|
| p 태그  | 문단 |
| br 태그 | 줄 바꾸기 |
| a 태그 | 'href' : 이동할 페이지 주소, 'target' : 링크 걸린 페이지를 여는 방법(_self, _blank) 'title' : 마우스를 올렸을 때 보여주는 제목 |
| img 태그 | 'src' : 이미지의 경로 |


<br>

### Emmet

반복적으로 작성하는 태그를 쉽게 생성

| 명령어 | 결과값 |
|--|--|
| html:5 + tab | 자동 html 틀 생성 |
| h3 + tab | 자동  h3 생성 |
