# Complete project details at https://RandomNerdTutorials.com
import random
from machine import Pin, ADC, PWM, Timer

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"

  # Convert the accl list to a string
  accl_str = ", ".join(map(str, accl))
    
  html = """
  <html>
  <head>
      <title>ESP Web Server</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="icon" href="data:,">
      <style>
          html {
              font-family: Helvetica;
              display: inline-block;
              margin: 0px auto;
              text-align: center;
          }
          h1 {
              color: #0F3376;
              padding: 2vh;
          }
          p {
              font-size: 1.5rem;
          }
          .button {
              display: inline-block;
              background-color: #e7bd3b;
              border: none;
              border-radius: 4px;
              color: white;
              padding: 16px 40px;
              text-decoration: none;
              font-size: 30px;
              margin: 2px;
              cursor: pointer;
          }
          .button2 {
              background-color: #4286f4;
          }
      </style>
  </head>
  <body>
      <h1>ESP32 Web Server</h1>
      <p>LED-1 state: <strong>"""+gpio_state +"""</strong></p>
      <p><a href="/?led=on"><button class="button">ON</button></a></p>
      <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
      <p>LED-2 state: <strong>"""+ gpio_state + accl_str +"""</strong></p>
      <p><a href="/?led=on"><button class="button">ON</button></a></p>
      <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
  </body>
  </html>"""

  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

accl= []
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  print("Received")
  if False:
    accl.append(random.random())
  else:
    nVal = pot.read()
    vVal = nVal*3.3/4095 - 0.03
    print("Voltage", vVal)
    accl.append(vVal)

  if led_on == 6:
    print('LED ON', accl)
    led.value(1)
  if led_off == 6:
    print('LED OFF', accl)
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

