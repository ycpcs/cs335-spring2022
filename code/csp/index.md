---
layout: default
course_number: CS335
title: Code Snippets - Content Security Policy
---

Index Page

```html
<html>
  <h2 >CSP Test</h2>
  <p>1. Inline: Correct Nonce: <span id='area1'>Failed</span></p>
  <p>2. Inline: Wrong Nonce: <span id='area2'>Failed</span></p>
  <p>3. Inline: No Nonce: <span id='area3'>Failed</span></p>
  <p>4. From self: <span id='area4'>Failed</span></p>
  <p>5. From example68.com: <span id='area5'>Failed</span></p>
  <p>6. From example79.com: <span id='area6'>Failed</span></p>

  <script type="text/javascript" nonce="1rA2345">
    document.getElementById('area1').innerHTML = "OK";
  </script>

  <script type="text/javascript" nonce="2rB3333">
    document.getElementById('area2').innerHTML = "OK";
  </script>

  <script type="text/javascript">
    document.getElementById('area3').innerHTML = "OK";
  </script>

  <script src="script1.js"> </script>
  <script src="http://www.example68.com:8090/script2.js"> </script>
  <script src="http://www.example79.com:8090/script3.js"> </script>

  <button onclick="alert('hello')">
    Click me
  </button>
</html>
```
