from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        message = "<h1>🎉 Jenkins CI/CD 자동 배포 성공! (버전 1)</h1>"
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    print("서버가 8000번 포트에서 시작됩니다...")
    server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
    server.serve_forever()