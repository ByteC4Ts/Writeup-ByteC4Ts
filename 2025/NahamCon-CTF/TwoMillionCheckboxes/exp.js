let ws = new WebSocket("ws://" + window.location.host + "/ws");
let nums = (l, r) => Array.from({length: r - l + 1}, (_, i) => i + l);

for (let i = 0; i < 20; i++) {
    ws.send(JSON.stringify({
        action: "check",
        numbers: nums(i * 100000, (i + 1) * 100000),
    }));
}
