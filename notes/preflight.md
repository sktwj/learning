
[跨域](https://mp.weixin.qq.com/s/7CADrFeKHy4dib2FZFnlSg)


```text
server {  
    listen       22222;  
    server_name  localhost;  
    location  / {  
        add_header Access-Control-Allow-Origin 'http://localhost:8080' always;  
        add_header Access-Control-Allow-Headers '*';  
        add_header Access-Control-Allow-Methods '*';  
        add_header Access-Control-Allow-Credentials 'true';  
        if ($request_method = 'OPTIONS') {  
            return 204;  
        }  
        proxy_pass  http://localhost:59200;   
    }  
}  
```