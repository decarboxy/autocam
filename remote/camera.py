import io
import picamera
import time

def capture_frame(width, height):
    """
    capture a frame to an IO bytestream
    :param width: integer width in pixels
    :param height: integer height in pixels
    :return BytesIO stream containing the file
    """
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (width, height)
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, 'jpeg')
    return stream

if __name__ == "__main__":
    with open("foo.jpg", 'wb') as outfile:
        stream = capture_frame(800, 600)
        outfile.write(stream.getvalue())