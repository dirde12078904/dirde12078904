import gradio as gr
import uuid
import socket
def sketch_recognition(img):
    def getTuringText(self, text):
        user_ip = self.getHostIP()
        mac_id = self.getMacID()
        turing_url_data = dict(key=self.app_key, info=text, userid=mac_id)

    def getHostIP(self):
        socket_info = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_info.connect('8.8.8.8', 80)
        ip = socket_info.getsockname()[0]
        return ip

    def getMaID(self):
        node = uuid.getnode()
        mac = uuid.UUID(int=node).hex[-12:]
        return mac
gr.Interface(fn=sketch_recognition, inputs="sketchpad", outputs="label").launch(share=True)