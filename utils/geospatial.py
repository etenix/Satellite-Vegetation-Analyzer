import rasterio
import numpy as np

def load_satellite_data(file_path):
    """
    GeoTIFFファイルからRed, Green, Blue, NIRバンドを抽出します。
    """
    with rasterio.open(file_path) as dataset:
        # バンド数を取得
        count = dataset.count
        print(f"ファイル名: {file_path}")
        print(f"バンド数: {count}, 解像度: {dataset.width}x{dataset.height}")

        # 一般的な衛星データ（Sentinel-2など）のバンド構成を想定
        # 通常、B2=Blue, B3=Green, B4=Red, B8=NIR
        red = dataset.read(1)   # バンド1 (Redと仮定)
        green = dataset.read(2) # バンド2 (Green)
        blue = dataset.read(3)  # バンド3 (Blue)
        
        # NIRが存在する場合
        nir = dataset.read(4) if count >= 4 else None
        
        # 地理情報（座標変換用）
        transform = dataset.transform
        crs = dataset.crs
        
    return {"red": red, "green": green, "blue": blue, "nir": nir, "transform": transform, "crs": crs}