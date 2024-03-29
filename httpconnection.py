from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
# 200 OK
conn.request('GET', '/')
response =  conn.getresponse()
print(response.status, response.reason)

if response.status == 200:
    body = response.read()
    print(body)


# 실패
# GET /hello.html HTTP/1.1
# 404 File Not Found - Body가 없으면 브라우저에 내장되어있는 404 페이지로 안내해줌
conn.request('GET', '/hello.html')
response =  conn.getresponse()
print(response.status, response.reason)