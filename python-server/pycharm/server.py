import asyncio
import socket
from _thread import *
import re
import Cadastral
import io

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 44344
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitting for a Connection')
ServerSocket.listen(5)

def int_to_bytes(value, length):
    result = []

    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)

    result.reverse()

    return bytes(bytearray(result))

def threaded_client(connection):
    coords_reader_size = connection.recv(4)
    print(1, coords_reader_size, int.from_bytes(coords_reader_size, byteorder='big'))
    image_reader_size = connection.recv(4)
    print(2, image_reader_size, int.from_bytes(image_reader_size, byteorder='big'))
    coords_data = connection.recv(int.from_bytes(coords_reader_size, byteorder='big'))
    print(3, coords_data, re.sub('[west<>\\n/aouhnr]', '', coords_data.decode('utf-8')).rstrip(' ').lstrip(' ').split('          '))
    image_data = b''
    while True:
        if len(image_data) >= int.from_bytes(image_reader_size, byteorder='big'):
            break
        image_data += connection.recv(64)
    print(4, image_data)
    print(coords_reader_size, image_reader_size, coords_data, image_data)
    print(type(image_data))
    print(len(image_data))

    f = open('./image.jpg', 'wb')
    f.write(image_data)
    f.close()

    #print('send 1 byte')
    #connection.sendall(bytes([1]))

    teststr = "Отправка сообщнеия клиенту с сервера.                               "

    print('send len of msg', len(teststr).to_bytes(4, byteorder='big'), len(teststr))
    connection.sendall(len(teststr).to_bytes(4, byteorder='big'))
    print('send test text')
    connection.sendall(str.encode(teststr))

    cadastral = Cadastral.Cadastral('/home/rmrf/Downloads/v1.kmz')
    #cadastral = Cadastral.Cadastral()
    #x, y = cadastral.getCoords(fixX=0.00300000000, fixY=0.00170000000)
    strcoords = re.sub('[west<>\\n/aouhnr]', '', coords_data.decode('utf-8')).rstrip(' ').lstrip(' ').split('          ')
    print(strcoords)
    x, y = cadastral.setAndGetCoords(float(strcoords[0]), float(strcoords[1]), float(strcoords[2]), float(strcoords[3]), fixX=0.00300000000, fixY=0.00170000000)
    #asyncio.get_event_loop().run_until_complete(cadastral.getScreenOfCadastralMapByCoords_BetaVersion())
    #loop = asyncio.get_event_loop()
    #cororun(cadastral.getScreenOfCadastralMapByCoords_BetaVersion())
    print('Получение кадастрового участка с карты росеестра.')
    img = cadastral.getScreenOfCadastralMapByCoords_BetaVersion(url='https://pkk.rosreestr.ru/#/search/{},{}/{}'.format(str(y), str(x), str(17)))
    #img.save('testtesttest.png')
    #loop.close()
    #asyncio.get_event_loop().run_until_complete()
    print('координаты участка')
    print(x, y)
    #image = cadastral.scaleScreen('i-want-to-die.png')
    #image = cadastral.scaleScreen(img)
    image = img

    image = cadastral.scaleScreen(image)
    image.save('testtesttest.png')
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()

    #import struct
    #struct.pack('>i', len(imgByteArr))

    #print('!!!!!!!!!! send len of image', len(imgByteArr).to_bytes(4, byteorder='big'), len(imgByteArr))
    #connection.sendall(len(imgByteArr).to_bytes(4, byteorder='big'))

    print('!!!!!!!!!! send len of image', len(imgByteArr).to_bytes(4, byteorder='big'), len(imgByteArr))
    connection.sendall(len(imgByteArr).to_bytes(4, byteorder='big'))
    print('!!!!!!!!!! send image')
    connection.sendall(imgByteArr)


    print('Connection closed')
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()


















#cadastral = Cadastral.Cadastral('/home/rmrf/Downloads/v1.kmz')
    # print(data.decode('utf-8'))
    # cadastral = Cadastral.Cadastral(data.decode('utf-8'))
    # cadastral.getCoords(fixX=0.00300000000, fixY=0.00170000000)
    # asyncio.get_event_loop().run_until_complete(
    #     cadastral.getScreenOfCadastralMapByCoords_BetaVersion(headless=True, imagesavename='example.png',
    #                                                           enablejavascreept=True,
    #                                                           viewresolution={'width': 900, 'height': 600},
    #                                                           scalepageparameter=17))
    # image = cadastral.scaleScreen('i-want-to-die.png')
    # connection.sendall(image)





# s = '          35.7988817468766          35.8119157103966          55.8231743212821          55.8305106504981        '
# s = s.rstrip(' ').lstrip(' ').split('          ')
# print(s)


# import Cadastral
# import asyncio
# import io
# from PIL import Image, ImageDraw, ImageFont
# import re
# import sys, struct
#
# # def convert_string_to_bytes(string):
# #     bytes = b''
# #     for i in string:
# #         bytes += struct.pack("B", ord(i))
# #     return bytes
# #
# #
# # stream = io.BytesIO(imagebite)
# # image = Image.open(stream).convert("RGBA")
# # stream.close()
# # image.save('out.jpg')
#
# async def handle_getResultsFromServerByImage(reader, writer):
#     coords_reader_size = await reader.read(4)
#     print(1, coords_reader_size, int.from_bytes(coords_reader_size, byteorder='big'))
#     image_reader_size = await reader.read(4)
#     print(2, image_reader_size, int.from_bytes(image_reader_size, byteorder='big'))
#     coords_data = await reader.read(int.from_bytes(coords_reader_size, byteorder='big'))
#     print(3, coords_data, re.sub('[west<>\\n/aouhnr]', '', coords_data.decode('utf-8')).rstrip(' ').lstrip(' ').split('          '))
#     image_data = b''
#     while True:
#         if len(image_data) >= int.from_bytes(image_reader_size, byteorder='big'):
#             break
#         image_data += await reader.read(64)
#     print(4, image_data)
#     print(coords_reader_size, image_reader_size, coords_data, image_data)
#     print(type(image_data))
#     print(len(image_data))
#
#
#
#
#     f = open('./image.jpg', 'wb')
#     f.write(image_data)
#     f.close()
#
#     #print('send 1 byte')
#     #connection.sendall(bytes([1]))
#
#     teststr = """Test text. Тестовое сообщение.
# Уважаемые участники, сегодня в 19.00 состоится минута молчания, которую мы не можем пропустить, отдавая дань памяти всем тем, кто одержал победу в ВОВ. Поэтому чек-поинт начнём в 18.30 и прервемся в 18.55 на минуту молчания. Продолжим с 19.15. Ваши кураторы подготовят таймслоты, согласно этому перерыву
# And I am really happy. I am still an undergraduat
# End. Конец."""
#
#     print('send len of msg', len(teststr).to_bytes(4, byteorder='big'), len(teststr))
#     #await reader.sendall(len(teststr).to_bytes(4, byteorder='big'))
#     writer.write(len(teststr).to_bytes(4, byteorder='big'))
#     #await writer.drain()
#     print('send test text')
#     #await reader.sendall(str.encode(teststr))
#     writer.write(str.encode(teststr))
#     #await writer.drain()
#
#
#
#
#
#     # reply = 'Server Says: ' + data.decode('utf-8')
#     # if not data:
#     #     break
#     # connection.sendall(str.encode(reply))
#
#
#     cadastral = Cadastral.Cadastral('/home/rmrf/Downloads/v1.kmz')
#     #cadastral = Cadastral.Cadastral()
#     #x, y = cadastral.getCoords(fixX=0.00300000000, fixY=0.00170000000)
#     strcoords = re.sub('[west<>\\n/aouhnr]', '', coords_data.decode('utf-8')).rstrip(' ').lstrip(' ').split('          ')
#     print(strcoords)
#     x, y = cadastral.setAndGetCoords(float(strcoords[0]), float(strcoords[1]), float(strcoords[2]), float(strcoords[3]), fixX=0.00300000000, fixY=0.00170000000)
#     await cadastral.getScreenOfCadastralMapByCoords_BetaVersion()
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(cadastral.getScreenOfCadastralMapByCoords_BetaVersion())
#     # loop.close()
#     #asyncio.get_event_loop().run_until_complete()
#     print(x, y)
#     image = cadastral.scaleScreen('i-want-to-die.png')
#
#     imgByteArr = io.BytesIO()
#     image.save(imgByteArr, format='PNG')
#     imgByteArr = imgByteArr.getvalue()
#
#     print('!!!!!!!!!! send len of image', len(imgByteArr).to_bytes(4, byteorder='big'), len(imgByteArr))
#     #reader.sendall(len(imgByteArr).to_bytes(4, byteorder='big'))
#     writer.write(len(imgByteArr).to_bytes(4, byteorder='big'))
#     #await writer.drain()
#     print('!!!!!!!!!! send image')
#     #reader.sendall(imgByteArr)
#     writer.write(imgByteArr)
#     #await writer.drain()
#
#     print("Close the connection")
#     writer.close()
#     await writer.wait_closed()
#
# async def main():
#     server = await asyncio.start_server(handle_getResultsFromServerByImage, '127.0.0.1', 44344)
#
#     addr = server.sockets[0].getsockname()
#     print(f'Serving on {addr}')
#
#     async with server:
#         await server.serve_forever()
#
# asyncio.run(main())
#
#
#
#
#
