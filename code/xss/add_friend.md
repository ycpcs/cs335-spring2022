---
layout: default
course_number: CS335
title: Code Snippets - Add a Friend
---

Example of add a friend script

```javascript
<script type="text/javascript">
  window.onload = function () {

    var elgg_ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;          
    var elgg_token = "&__elgg_token=" + elgg.security.token.__elgg_token;

    var url = ""; // TODO                 

    var request = new XMLHttpRequest();
    request.open("GET", url, true);
    request.send();
}
</script>
```
