from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import html
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8000

CORRECT_USERNAME = "student"
CORRECT_PASSWORD = "Test123"


class LoginHandler(BaseHTTPRequestHandler):

    def send_html(self, content, status=200):

        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode("utf-8"))

    def do_GET(self):

        if self.path == "/":

            page = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>IDS Practical Login</title>
            </head>

            <body>

            <h2>TY BSc CS - IDS Practical</h2>

            <form method="POST" action="/login">

                <label>Username:</label>
                <input type="text" name="username">

                <br><br>

                <label>Password:</label>
                <input type="password" name="password">

                <br><br>

                <button type="submit">Login</button>

            </form>

            </body>
            </html>
            """

            self.send_html(page)

        else:
            self.send_html("<h2>404 - Page Not Found</h2>", 404)

    def do_POST(self):

        if self.path != "/login":

            self.send_html("<h2>404 - Page Not Found</h2>", 404)
            return

        content_length = int(self.headers.get("Content-Length", 0))

        data = self.rfile.read(content_length).decode("utf-8")

        form_data = parse_qs(data)

        username = form_data.get("username", [""])[0]
        password = form_data.get("password", [""])[0]

        current_time = datetime.now().strftime("%H:%M:%S")

        print(
            f"[{current_time}] "
            f"Login attempt - "
            f"Username: {username}"
        )

        if (
            username == CORRECT_USERNAME
            and password == CORRECT_PASSWORD
        ):

            result = """
            <h2>Login Successful</h2>
            <p>Test account authenticated.</p>
            <a href="/">Try Again</a>
            """

        else:

            result = """
            <h2>Login Failed</h2>
            <p>Invalid username or password.</p>
            <a href="/">Try Again</a>
            """

        page = f"""
        <!DOCTYPE html>

        <html>

        <head>
            <title>Login Result</title>
        </head>

        <body>

        {result}

        </body>

        </html>
        """

        self.send_html(page)


server = HTTPServer((HOST, PORT), LoginHandler)

print("=" * 50)
print("TY BSc CS - IDS Practical")
print("=" * 50)
print()
print("Local Login Server Started")
print()
print("Open this address in your browser:")
print()
print("http://127.0.0.1:8000")
print()
print("Test username : student")
print("Test password : Test123")
print()
print("Press CTRL+C to stop the server.")
print("=" * 50)

server.serve_forever()