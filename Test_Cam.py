import asyncio
import websockets
import cv2
import base64

async def send_frames():
    uri = "ws://<서버_IP>:5000"
    async with websockets.connect(uri) as websocket:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # 프레임을 JPG로 인코딩 후 base64로 변환
            _, buffer = cv2.imencode('.jpg', frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')
            
            # WebSocket을 통해 프레임 전송
            await websocket.send(frame_base64)

        cap.release()

asyncio.get_event_loop().run_until_complete(send_frames())
