from flask import Flask, render_template, request
import base64
import json

app = Flask(__name__, template_folder='templates')

@app.route('/base64encodeString', methods=['GET', 'POST'])
def base64encodeString():
    if request.method == 'POST':
        base64_string = request.form.get('base64_string')
        altered_line = request.form.get('altered_line')
        custom_value = request.form.get('custom_value')

        # Perform base64 decoding and alteration logic here
        decoded_string = base64.b64decode(base64_string).decode('utf-8')

        if altered_line and custom_value:
            try:
                altered_line = int(altered_line)
                if 0 <= altered_line < len(decoded_string):
                    modified_string = decoded_string[:altered_line] + custom_value + decoded_string[altered_line+1:]
                    encoded_string = base64.b64encode(modified_string.encode('utf-8')).decode('utf-8')
                    return render_template('result.html', decoded_string=decoded_string, modified_string=modified_string, encoded_string=encoded_string)
                else:
                    raise ValueError("Invalid altered_line value")
            except ValueError:
                pass

        encoded_string = base64.b64encode(decoded_string.encode('utf-8')).decode('utf-8')
        return render_template('result.html', decoded_string=decoded_string, modified_string=decoded_string, encoded_string=encoded_string)

    return render_template('base64encode.html')

@app.route('/base64decodeString', methods=['GET', 'POST'])
def base64decodeString():
    if request.method == 'POST':
        base64_string = request.form.get('base64_string')

        # Perform base64 decoding logic
        decoded_string = base64.b64decode(base64_string).decode('utf-8')

        return render_template('result.html', decoded_string=decoded_string, modified_string=decoded_string, encoded_string=None)

    return render_template('base64decode.html')

@app.route('/JSONFormatString', methods=['GET', 'POST'])
def JSONFormatString():
    if request.method == 'POST':
        json_string = request.form.get('json_string')

        # Perform JSON formatting logic
        try:
            formatted_json = json.dumps(json.loads(json_string), indent=4)
        except json.JSONDecodeError:
            formatted_json = None

        return render_template('result.html', decoded_string=None, modified_string=None, encoded_string=None, formatted_json=formatted_json)

    return render_template('jsonformat.html')

if __name__ == '__main__':
    app.run(host='206.189.228.251', port=5000)

