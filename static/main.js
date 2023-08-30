function decodeAndModifyBase64() {
    // Get the base64 string and other inputs from the form
    var base64String = document.getElementById('base64_string').value;
    var alteredLine = document.getElementById('altered_line').value;
    var customValue = document.getElementById('custom_value').value;

    // Perform base64 decoding
    var decodedString = atob(base64String);

    // Declare modifiedString variable
    var modifiedString;

    // Perform modification logic
    var modifiedString;
    if (decodedString.includes(alteredLine)) {
        modifiedString = decodedString.replace(alteredLine, customValue);
    } else {
        modifiedString = "altered_line not found";
    }

    // Perform base64 encoding
    var encodedString = btoa(modifiedString);

    // Update the result elements with the modified output
    document.getElementById('decoded_string').textContent = decodedString;
    document.getElementById('modified_string').textContent = modifiedString;
    document.getElementById('encoded_string').textContent = encodedString;
}

