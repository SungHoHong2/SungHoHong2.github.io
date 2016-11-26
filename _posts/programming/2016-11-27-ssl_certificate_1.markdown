---
published: true
title: ssl certificate tips 
layout: post
category: programming
permalink: /programming/ssl_certificate_1
---


#### Generate a private key

```
$ openssl genrsa -des3 -out server.key 1024


Generating RSA private key, 1024 bit long modulus
.........................................................++++++
........++++++
e is 65537 (0x10001)
Enter PEM pass phrase:
Verifying password - Enter PEM pass phrase:

```

<br>

#### Generate a CSR 

```

$ openssl req -new -key server.key -out server.csr


Country Name (2 letter code) [GB]:CH
State or Province Name (full name) [Berkshire]:Bern
Locality Name (eg, city) [Newbury]:Oberdiessbach
Organization Name (eg, company) [My Company Ltd]:Akadia AG
Organizational Unit Name (eg, section) []:Information Technology
Common Name (eg, your name or your server's hostname) []:public.akadia.com
Email Address []:martin dot zahn at akadia dot ch
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:


```


<br>


#### Remove paraphrase from key 


```

$ cp server.key server.key.org
$ openssl rsa -in server.key.org -out server.key

The newly created server.key file has no more passphrase in it.

-rw-r--r-- 1 root root 745 Jun 29 12:19 server.csr
-rw-r--r-- 1 root root 891 Jun 29 13:22 server.key
-rw-r--r-- 1 root root 963 Jun 29 13:22 server.key.org


```


<br>

#### Generate self signed certificate 


```

$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt


```




#### Use it in node.js 

```

var fs = require('fs');

var options = {
    key: fs.readFileSync('./cert/server.key'),
    cert: fs.readFileSync('./cert/server.crt'),
    requestCert: false,
    rejectUnauthorized: false
}

var express = require('express'),
    app = express(),
    server = require('https').createServer(options, app),
    io = require('socket.io').listen(server);


app.get('/',function(req, res){
    console.log(process.env.PORT);
    res.sendfile(__dirname + '/index.html')
});


server.listen(process.env.PORT || 8000);

io.sockets.on('connection',function(socket){
    socket.on('send message', function(data){
        io.sockets.emit('new message', data);
        socket.broadcast.emit('new message',data);
    });
});


```

