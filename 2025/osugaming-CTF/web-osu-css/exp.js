const list = Array.from(document.querySelectorAll("#n"));

function test(n) {
    for (let i = 0; i < list.length; i++) list[i].open = false;
    for (let i = 0; i < n; i++) list[i].open = true;
}

test(746)

// osu{1m_n0t_4fr4id_0f_the_b1g_bl4ck_4nym0r3}