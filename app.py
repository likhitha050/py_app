from flask import Flask, render_template_string

app = Flask(__name__)

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kubernetes Pipeline</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }
        h1 { color: #333; font-size: 24px; margin-bottom: 10px; }
        .status-dot {
            height: 12px;
            width: 12px;
            background-color: #28a745;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        .status-text { color: #666; font-size: 14px; margin-bottom: 20px; }
        .message-box {
            background-color: #e8f0fe;
            color: #1967d2;
            padding: 15px;
            border-radius: 8px;
            font-weight: 500;
            border: 1px solid #d2e3fc;
        }
        .footer { margin-top: 20px; font-size: 12px; color: #aaa; }
    </style>
</head>
<body>

    <div class="card">
        <h1>Deployment Manager</h1>
        <div class="status-text">
            <span class="status-dot"></span>Active on Port {{ port }}
        </div>
        
        <div class="message-box">
            {{ message }}
        </div>

        <div class="footer">
            Powered by Jenkins & Kubernetes
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    # The message you want to display
    msg = "Hello form jenkins pipeline integrated with kubernetes!!"
    
    # Render the HTML and inject the message and port variables
    return render_template_string(PAGE_TEMPLATE, message=msg, port=8090)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
