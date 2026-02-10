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