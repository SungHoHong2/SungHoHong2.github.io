---
published: true
title: HTML 초급 1일차
layout: post
category: programming
permalink: /programming_kr/html_5_1
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
| ol > li 태그 | 번호가 추가된 리스트 |
| ul > li 태그 | 번호가 없는 리스트 |
| dl > dt, dd 태그 | 정의 목록 |
| div, span 태그 | 레이아웃 요소 |

<br>

### Emmet

반복적으로 작성하는 태그를 쉽게 생성

| 명령어 | 결과값 |
|--|--|
| html:5 + tab | 자동 html 틀 생성 |
| h3 + tab | 자동  h3 생성 |
| ol>li + tab | 자동 ol과 li 태그 생성 |
| p#body + tab | 자동으로 p 태그와 아이디 body 생성 |
| a[href=1][content=1]*4 | a 태그에 괄호 안에 있는 속성값들을 총 4개 생성 |
| a{click me } | a 태그 안에 텍스트를 입력 |
| col#col-$*5 | 아이디 값에 자동으로 번호 매김 |

<br>

### 클래스와 아이디 속성

- 첫 글자는 알파벳으로 시작
- 두 번째는 알파벳 숫자 - 사용가능
- 클래스는 전체에 적용, id는 하나만 선언


<br>


### CSS 호출 방식

마크업 언어가 실제로 표시되는 방법을 기술하는 언어, 레이아웃과 스타일을 정의할 때 주로 사용. 'Cascading Style Sheet'라고 한다.

```CSS

  selector {
    property : value;
  }

  #body-title{
      font-size: 14px;
      font-weight:bold;
      color: DarkSlateGrey;
  }

```

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset = 'utf-8'>
    <title> Document </title>
    <style>
      #body-title{
          font-size: 100px;
          font-weight:bold;
          color: red;
      }
    </style>
    <link rel = "stylesheet" href = "css1.css"/>

</head>
<body>
  <div id = 'body-title'>howdy this is the css </body>
  <div style = "font-size : 100px; font-weight:bold; color: blue; ">howdy this is the css </body>
  <div id = 'body-title2'>howdy this is the css </body>
</body>
</html>

```

<br>

### CSS 선택자

```css

/* 전체 선택자 */
*{ padding: 0; margin: 0;}

/* 타입 선택자 */
h1{ color : red; }
p{ color : blue; }

/* 클래스 선택자 */
.section{ color: #333 }
p.section-title{ color : #efefef}

/* ID값 입력 */
#index-title { font-size : 18px; }
p#index-description{ font-size: 12px; color : #999;}

/* 하위 선택자 */
section ul {color : red }
section > ul { color : blue }

/* 인접 형제 선택자 */
/* 우선순위가 같은 경우에는 가장 마지막에 있는 CSS가 실행된다. */
h1+ul{ background: Azure }
h1~ul{ background: Azure; color: DarkBlue }

/* 속성 선택자 */
CSS[attribute~="value"] /* selector is used to select elements with an attribute value containing a specified word. */
                        /* title="flower", title="summer flower", and title="flower new", but not title="my-flower" or title="flowers".*/
CSS[attribute|="value"] /* selector is used to select elements with the specified attribute starting with the specified value. */
                        /* class="top-text" */
CSS[attribute^="value"] /* selector is used to select elements whose attribute value begins with a specified value. */
CSS[attribute$="value"] /* selector is used to select elements whose attribute value ends with a specified value. */
CSS[attribute*="value"] /* The [attribute*="value"] selector is used to select elements whose attribute value contains a specified value. */


E:link
E:visited
E:active
E:hover
E:focus  /* input 입력 가능한 상태일 때 */
E:first-line /* 첫번째 줄 */
E:first-letter /* 첫번쨰 글짜 */
E:before /* indent */
E:after /* 마지막 부분 indent */

```

<br>

### CSS 순서도

1. important
1. inline style (아예 태그 안에 스타일 입력하는 것)
2. ID  
3. Class
4. Tag

```css

  p {
    font-size: 30px !important;
    color : green !important;
  }

```

<br>

### CSS 서체

만약 컴퓨터에 돋움이 존재하지 않으면 특정 서체가 나타나지 않는다. 따라서 최악의 경우 여러가지 가지수를 지정해줘야 한다.

```css

  /* 서체 지정 */
  body{ font-family: "돋움" }

  /* 글자 크기 */
  /* px, em 부모의 크기에 * 배율 */
  body { font-size : 14px; }
  h1 { font-size: 28px(2em); /* 2*14px */ }

  /* 글자 스타일 */
  body{ font-style: italic }

  /* 줄 길이 */
  body{ line-height: 10px; } /* default 값은 em으로 입력되어 있다. */

  /* 문자 정렬 */
  body{text-align: left; text-align: justify}

  /* 들여쓰기 */
  body{text-indent: 10px; }

  /* 글자 간격 */
  p{letter-spacing: 10px}

  /* 자간 간격 */
  p{word-spacing: 12px }

  /* 수직 정렬 */
  div{vertical-align: top;}

  /* 띄어쓰기 적용 */
  div{white-space: pre;}

```
