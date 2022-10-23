from http.server import SimpleHTTPRequestHandler, HTTPServer
 
server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)  #サーバインスタンスを生成
server.serve_forever()   #常時受けつけモードを指定。