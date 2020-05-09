```
# Enable granularity CORS in nginx

server {

    listen truedoc-nginx:80;

    client_max_body_size 5M;  # Max allowed document filesize is 4M + some its stuff = (approx.) 5M

    server_name truedoc-app.localhost;

    location / {

        # CORS
        # How does it work? See: https://learn.javascript.ru/fetch-crossorigin
        # Nginx example: https://enable-cors.org/server_nginx.html

        set $CORS_SITES 'http://truedoc-ui.localhost';
        set $CORS_METHODS 'POST,GET';
        set $CORS_HEADERS 'Content-Type,Authorization';

        # 'always' required at the end because nginx sends these headers
        # only for following HTTP codes: 200, 201, 204, 206, 301, 302, 303, 304, 307 and 308
        # but some projects responses have another codes (like: 406, 409).
        # See: https://nginx.org/ru/docs/http/ngx_http_headers_module.html#add_header

        if ($request_method = 'OPTIONS') {

            add_header 'Access-Control-Allow-Origin' '$CORS_SITES' always;
            add_header 'Access-Control-Allow-Methods' '$CORS_METHODS' always;
            add_header 'Access-Control-Allow-Headers' '$CORS_HEADERS' always;

            return 204; # "No content"
        }

        if ($request_method = 'POST') {

            add_header 'Access-Control-Allow-Origin' '$CORS_SITES' always;
            add_header 'Access-Control-Allow-Methods' '$CORS_METHODS' always;
            add_header 'Access-Control-Allow-Headers' '$CORS_HEADERS' always;
        }

        if ($request_method = 'GET') {

            add_header 'Access-Control-Allow-Origin' '$CORS_SITES' always;
            add_header 'Access-Control-Allow-Methods' '$CORS_METHODS' always;
            add_header 'Access-Control-Allow-Headers' '$CORS_HEADERS' always;
        }

        proxy_pass http://truedoc-app:5000;

        proxy_buffering on;
        proxy_buffers 12 12k;
        proxy_redirect off;

        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
    }
}
```
