import base64
import io
import cv2

filename = "/home/ubuntu/reconstructed.jpg"

img = cv2.imread(filename)
height, width, channels = img.shape
print(height)
print(width)
print(channels)

retval, buffer = cv2.imencode('.jpg', img)

jpg_as_text = base64.b64encode(buffer)

#print(jpg_as_text)

base64_string = jpg_as_text.decode('ascii')

with open('/home/ubuntu/testImage2', 'wb') as file_to_save:
    file_to_save.write(base64_string)
