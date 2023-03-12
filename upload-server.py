from http.server import BaseHTTPRequestHandler, HTTPServer

class FileUploadHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        file_content = self.rfile.read(content_length)
        with open('uploaded_file.txt', 'w') as f:
            f.write(file_content.decode('utf-8'))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully.')
        
if __name__ == '__main__':
    server_address = ('', 80)
    httpd = HTTPServer(server_address, FileUploadHandler)
    httpd.serve_forever()
