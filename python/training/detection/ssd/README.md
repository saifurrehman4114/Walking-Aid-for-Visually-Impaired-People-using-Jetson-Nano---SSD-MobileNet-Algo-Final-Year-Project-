# SSD-based Object Detection in PyTorch

Data on which I have trained this model is in the following link:

https://drive.google.com/drive/folders/1SXUKru6zTs9BHBOtAS_4GNyW9Lx4pB4i?usp=sharing

Trained Model files are in the following link and the best model file with less loss is converted into ONNX format:

https://drive.google.com/drive/folders/1ExNsCVFC9VIQEhqDTUWdpsMhbf05WNtw?usp=sharing

This repo implements [SSD (Single Shot MultiBox Detector)](https://arxiv.org/abs/1512.02325) in PyTorch for object detection, using MobileNet backbones.  It also has out-of-box support for retraining on Google Open Images dataset.  

> For documentation, please refer to Object Detection portion of the **[Hello AI World](https://github.com/dusty-nv/jetson-inference/tree/dev#training)** tutorial:
> [Re-training SSD-Mobilenet](https://github.com/dusty-nv/jetson-inference/blob/dev/docs/pytorch-ssd.md)

Thanks to @qfgaohao for the upstream implementation from:  [https://github.com/qfgaohao/pytorch-ssd](https://github.com/qfgaohao/pytorch-ssd)

