# PassGen
A simple program that generates a safe and secure password, then saves the password in a file that can be encrypted and decrypted.

# How To Use
Make sure you have Python 3.x downloaded on your system from https://www.python.org

Double click "main.py" to run the program, this will bring up a simple GUI interface and create a new file called "key.key". That is your key file that you must use for encrypting and decrypting the file which your password is stored.

Type in the text field how long you want the generated password to be (recommended is 12). After you have entered how long you want the generated password to be, click on the "Generate Password" button. Your password will then appear on the interface and be saved to a file called "password.txt".

You can then choose to encrypt the file with the "Encrypt Password" button, make sure that the "key.key" and "password.txt" file is in the same directory as "main.py" for encrypting and decrypting. Encrypting the file will generate a file called "password.txt.encrypted" and delete "password.txt". It is recommended to clear out your recycle bin after this since the normal "pasword.txt" will be inside.

To then decrypt the file, make sure that "password.txt.encrypted" and "key.key" are in the same directory as "main.py". Then simply click the "Decrypt Password" button. this will generate the decrypted "password.txt" file and delete the encrypted "password.txt.encrypted" file.

It is recommended that between use of the program, you keep "key.key" in a secure location such as a USB. Anyone with the key can decrypt the password.
