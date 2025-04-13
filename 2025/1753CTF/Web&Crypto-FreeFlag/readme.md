# 1753 CTF - Free Flag

## Approach

Check every minute backwards (enumerate all timezones), you will get the result in minutes.

Also, we noticed most of the flags in this event only contain lowercase letters, digits, and underscores. So I filtered the result with regex `/^[0-9A-Za-z_]+$/`.

```js
const CryptoJS = require("./crypto-js.js");

function format(timezone, date) {
  const pad0 = (num) => (num < 10 ? "0" : "") + num;
  const yyyy = date.getFullYear();
  const mm = pad0(date.getMonth() + 1);
  const dd = pad0(date.getDate());
  const h = pad0(date.getHours());
  const m = pad0(date.getMinutes());
  return `${timezone}-${mm}/${dd}/${yyyy}-${h}:${m}`;
}

const flag = [
  0x45, 0x00, 0x50, 0x39, 0x08, 0x6f, 0x4d, 0x5b, 0x58, 0x06, 0x66, 0x40, 0x58,
  0x4c, 0x6d, 0x5d, 0x16, 0x6e, 0x4f, 0x00, 0x43, 0x6b, 0x47, 0x0a, 0x44, 0x5a,
  0x5b, 0x5f, 0x51, 0x66, 0x50, 0x57,
];
timezones = Intl.supportedValuesOf("timeZone");
timestamp = new Date().getTime();

function check(result) {
  // if (!/^[\\x21-\\x7E]+$/.test(result)) return false;
  if (!/^[0-9A-Za-z_]+$/.test(result)) return false;
  return true;
}

for (let minutesBack = 0; minutesBack < 60 * 24 * 90; minutesBack++) {
  for (const timezone of timezones) {
    const date = new Date(timestamp - minutesBack * 60 * 1000);
    const base = format(timezone, date);
    const hash = CryptoJS.MD5(base).toString();
    const result = flag
      .map((x, i) => String.fromCharCode(x ^ hash.charCodeAt(i)))
      .join("");
    if (check(result)) {
      console.log(`${result}  (${base})`);
    }
  }
}

// see_i_told_you_it_was_working_b4  (Europe/Warsaw-02/13/2025-20:37)
```

## Flag

```
1753c{see_i_told_you_it_was_working_b4}
```
