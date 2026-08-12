# HTTP Request/Response Log

## Request 1 — Get Post 1

### Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

### Response

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2026 14:28:10 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 292
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1785194657"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1785194657"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1785194663
Age: 13990
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2a02a407d5f0e6e-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```
### Annotation

Status:  200 OK — the request was successful, and the server returned the requested data.

Content-Type:  application/json; charset=utf-8 — the server is sending the response in JSON format, using UTF-8 to represent the text.

Content-Length: 292 — the response data is 292 bytes in size.

Connection: keep-alive — the connection between the client and server can stay open so it can be reused for other requests.

Access-Control-Allow-Credentials: true — the server allows credentials, such as cookies, to be sent with approved requests from another website.

## Request 2 — Get Post 2

### Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/2
```

### Response

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2026 16:20:45 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 278
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"116-jnDuMpjju89+9j7e0BqkdFsVRjs"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=iXrXLjMshK%2BpdYafrnUJfREGdGA4ZlzQlCMxdLFlz8w%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786349193"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=iXrXLjMshK%2BpdYafrnUJfREGdGA4ZlzQlCMxdLFlz8w%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786349193"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786349214
Age: 6901
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2a0cf264a223bf2-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
}
```

### Annotation

- **Status:** `200 OK` — the server successfully processed the request and returned the requested resource.
- **Content-Type:** `application/json` — the response body is formatted as JSON.

## Request 3 — Get User 1

### Request

```bash
curl -i https://jsonplaceholder.typicode.com/users/1
```

### Response

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2026 16:24:15 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 509
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"1fd-+2Y3G3w049iSZtw5t1mzSnunngE"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=GIwyebBgV7ZP9c3UF77flf3I4W3a8sXS5tSGoy7EShQ%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786526571"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=GIwyebBgV7ZP9c3UF77flf3I4W3a8sXS5tSGoy7EShQ%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786526571"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786526575
Age: 25283
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2a0d4492a883a32-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
```

### Annotation

- **Status:** `200 OK` — the server successfully processed the request and returned the requested resource.
- **Content-Type:** `application/json` — the response body is formatted as JSON.

## Request 4 — Get Comment 1

### Request

```bash
curl -i https://jsonplaceholder.typicode.com/comments/1
```

### Response

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2026 16:25:42 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 268
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"10c-KJ4I9RM/+33TKdV8CFsIvqsDSP0"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=qjc6D6WxXr1%2FATaLsDP1HoKXXOPPOthx5sNm30prTA0%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786539766"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=qjc6D6WxXr1%2FATaLsDP1HoKXXOPPOthx5sNm30prTA0%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786539766"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786539775
Age: 12176
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a2a0d66a5fb340f9-BOM
alt-svc: h3=":443"; ma=86400

{
  "postId": 1,
  "id": 1,
  "name": "id labore ex et quam laborum",
  "email": "Eliseo@gardner.biz",
  "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
}
```

### Annotation

- **Status:** `200 OK` — the server successfully processed the request and returned the requested resource.
- **Content-Type:** `application/json` — the response body is formatted as JSON.

## Request 5 — Non-existent Post

### Request

```bash
curl -i https://jsonplaceholder.typicode.com/posts/999999
```

### Response

```
HTTP/1.1 404 Not Found
Date: Wed, 12 Aug 2026 16:26:21 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 2
Connection: keep-alive
access-control-allow-credentials: true
Cache-Control: max-age=43200
etag: W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=udRWZzbCMSZFw%2FiD99LqKxNH7JQ34reb%2F0Q%2B7yB8K3s%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786551981"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=udRWZzbCMSZFw%2FiD99LqKxNH7JQ34reb%2F0Q%2B7yB8K3s%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786551981"
Server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786552015
cf-cache-status: MISS
CF-RAY: a2a0d7569d5bff70-BOM
alt-svc: h3=":443"; ma=86400

{}
```

### Annotation

- **Status:** `404 Not Found` — the server was reached, but the requested resource does not exist.
- **Content-Type:** `application/json` — the response body is formatted as JSON.