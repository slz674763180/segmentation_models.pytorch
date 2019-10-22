import segmentation_models_pytorch as smp
model = smp.Unet('resnet34', classes=3, activation='softmax')