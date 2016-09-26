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

### 여러 가지 요소

| 태그 | 내용 |
|----|----|
| p 태그  | 문단 |
| br 태그 | 줄 바꾸기 |
