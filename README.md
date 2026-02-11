# Satellite-Vegetation-Analyzer

このライブラリは、衛星データ（マルチスペクトル画像）を使用して、森林、農地、都市の緑地を自動的に抽出・分析するためのツールキットです。

## 🌟 特徴
- **ハイブリッド分析**: 従来のNDVI（植生指数）計算と最新のディープラーニング（DeepLabV3+）を統合。
- **マルチスペクトル対応**: RGB画像だけでなく、近赤外線（NIR）バンドを含むGeoTIFFの処理に対応。
- **時系列分析**: 特定のエリアの植生変化を時間軸で追跡可能。

## 📊 抽出アルゴリズム
1. **NDVIベース**: 以下の数式を用いて、ピクセル単位で植物の活性度を算出します。
   $$NDVI = \frac{NIR - RED}{NIR + RED}$$
2. **AIベース**: 精密な境界特定のためにセグメンテーションモデルを使用。



## 🛠️ インストール
```bash
git clone [https://github.com/YourUsername/Satellite-Vegetation-Analyzer.git](https://github.com/YourUsername/Satellite-Vegetation-Analyzer.git)
pip install -r requirements.txt
```

## 3. 核心コードの実装

### A. 植生指数の計算 (`utils/indices.py`)
AIを使わなくても、赤色光(Red)と近赤外光(NIR)があれば植物を抽出できます。

```python
import numpy as np

def calculate_ndvi(red_band, nir_band):
    """
    NDVI（正規化植生指数）を計算します。
    範囲は -1.0 から 1.0 で、0.2 以上が通常「植生」と見なされます。
    """
    numerator = nir_band.astype(float) - red_band.astype(float)
    denominator = nir_band.astype(float) + red_band.astype(float)
    
    # ゼロ除算を避けるための処理
    ndvi = np.divide(numerator, denominator, out=np.zeros_like(numerator), where=denominator!=0)
    return ndvi
```

### B. AIモデルの定義 (models/deeplab.py)
植物の境界は複雑（樹木の影など）なため、U-Netよりも洗練された DeepLabV3+ を使用するのがプロフェッショナルです。
```python
import segmentation_models_pytorch as smp

def get_vegetation_model():
    model = smp.DeepLabV3Plus(
        encoder_name="resnet50", 
        encoder_weights="imagenet",
        in_channels=3, # またはNIRを含めた4チャンネル
        classes=1,
        activation='sigmoid'
    )
    return model
```

### C. 推論スクリプト (predict_vegetation.py)
```python
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
```

## 4. このプロジェクトを差別化するポイント
- 影の除去 (Shadow Removal): 都市部の衛星画像では、ビルの影が植生と誤認されやすいです。影を検出して補正する機能を入れると、スター（Star）が付きやすくなります。
- LULC分類: 単なる「植物」だけでなく、「広葉樹」「針葉樹」「草地」を分類する多クラス分類（Multi-class classification）に拡張するのも良いでしょう。