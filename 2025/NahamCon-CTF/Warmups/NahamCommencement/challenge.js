function a(t) {
    let r = '';
    for (let i = 0; i < t.length; i++) {
        const c = t[i];
        if (/[a-zA-Z]/.test(c)) {
            const d = c.charCodeAt(0);
            const o = (d >= 97) ? 97 : 65;
            const x = (d - o + 16) % 26 + o;
            r += String.fromCharCode(x);
        } else {
            r += c;
        }
    }
    return r;
}

function b(t, k) {
    let r = '';
    let j = 0;
    for (let i = 0; i < t.length; i++) {
        const c = t[i];
        if (/[a-zA-Z]/.test(c)) {
            const u = c === c.toUpperCase();
            const l = c.toLowerCase();
            const d = l.charCodeAt(0) - 97;
            const m = k[j % k.length].toLowerCase();
            const n = m.charCodeAt(0) - 97;
            const e = (d + n) % 26;
            let f = String.fromCharCode(e + 97);
            if (u) {
                f = f.toUpperCase();
            }
            r += f;
            j++;
        } else {
            r += c;
        }
    }
    return r;
}

function c(s) {
    return btoa(s);
}

document.addEventListener('DOMContentLoaded', function () {
    const x1 = "dqxqcius";
    const x2 = "YeaTtgUnzezBqiwa2025";
    const x3 = "ZHF4cWNpdXM=";
    const k = "nahamcon";


    const f = document.getElementById('loginForm');
    const u = document.getElementById('username');
    const p = document.getElementById('password');
    const s = document.getElementById('spinner');
    const d = document.getElementById('result');

    f.addEventListener('submit', function (e) {
        e.preventDefault();

        const q = u.value;
        const w = p.value;


        const q1 = a(q);

        const w1 = b(w, k);

        if (q1 !== x1 || w1 !== x2) {
            d.textContent = "Access denied. Client-side validation failed. Try again.";
            d.className = "error";
            d.style.display = "block";
            return;
        }

        s.style.display = "block";
        d.style.display = "none";

        const g = new FormData();
        g.append('username', q);
        g.append('password', w);

        fetch('/login', {
            method: 'POST',
            body: g
        })
            .then(h => h.json())
            .then(z => {
                s.style.display = "none";
                d.style.display = "block";

                if (z.success) {
                    console.log("🎉 Server authentication successful!");
                    d.innerHTML = `
                    <p>${z.message}</p>
                    <p class="flag">🙌🎉${z.flag}🎉🙌</p>
                `;
                    d.className = "success";
                } else {
                    console.log("❌ Server authentication failed");
                    d.textContent = z.message;
                    d.className = "error";
                }
            })
            .catch(err => {
                console.error("🚨 Network error:", err);
                s.style.display = "none";
                d.style.display = "block";
                d.textContent = "An error occurred while processing your request.";
                d.className = "error";
            });
    });

});