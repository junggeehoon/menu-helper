from PyQt5.QtWidgets import QFileDialog

def get_image_file():
    try:
        path, _ = QFileDialog.getOpenFileName(None, '이미지 선택', '', 'Images (*.png *.jpg *.jpeg)')
        return path
    except:
        raise Exception("지원하지 않는 파일 형식입니다.")

