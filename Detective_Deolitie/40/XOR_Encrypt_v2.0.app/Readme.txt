This Is a Simple GUI XOR encryption program , XOR encryption provides
a decent level of security by obfuscation .A Secure way to encrypt your 
data is to use a strong password , higher the relative length of your
password as compared with the data higher the more secure your file will 
be . If you are looking for securing your sensitive data with a high level 
encryption algorithms which will take hundreds of year of computional bruteforce
to decode  THEN THIS IS NOT THE SOFTWARE FOR YOU . 

Your Password is saved as SHA256 hash in the encrypted file.


a.exe CLI reference

a.exe <file path> <encrypt:1/decrypt:2> <overwrite or not> <password>

example:
to encrypt file D:/randomint.txt with password "12345678" 

a.exe D:/randomint.txt 1 1 12345678

this will replace the orignal file 

decryption command will be 

a.exe D:/randomint.txt 2 1 12345678


messages STDOUT

'1' if everything goeswell
'2' if file is not readable
'3' if password is incorrect
'4' out of memory  