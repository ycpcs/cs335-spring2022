---
layout: default
course_number: CS335
title: Code Snippets - Edit Profile
---

Example of edit profile script

```javascript
<script type="text/javascript">
  window.onload = function(){
    var user_guid  = "&guid=" + elgg.session.user.guid;
    var elgg_ts    = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var elgg_token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var name  = "&name=" + elgg.session.user.name;

    var content  = "";  // TODO
    var url = "";       // TODO
    var sammy = 0;       // TODO

    if (elgg.session.user.guid != sammy){                  
      var request = new XMLHttpRequest();
      request.open("POST", url, true);
      request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      request.send(content);
    }
  }
</script>
```
