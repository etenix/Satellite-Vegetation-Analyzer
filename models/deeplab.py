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