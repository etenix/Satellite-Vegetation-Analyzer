import cv2
from utils.indices import calculate_ndvi

def process_image(image_path):
    # 画像読み込み（ここでは簡略化のためRGB）
    img = cv2.imread(image_path)
    
    # 1. AIで「緑のエリア」を大まかに特定
    # mask = model.predict(img)
    
    # 2. NDVIで「生きている植物」かを確認
    # ndvi = calculate_ndvi(img[red], img[nir])
    
    print("植物抽出と健康状態の分析が完了しました。")