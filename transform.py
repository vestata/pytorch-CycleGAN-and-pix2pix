import torch
from torchvision import transforms
from PIL import Image
import os

# 設定
model_path = '/home/nini/pytorch-CycleGAN-and-pix2pix/checkpoints/tmp2/latest_net_G.pth'  # 模型文件路徑
input_folder = '/home/  nini/pytorch-CycleGAN-and-pix2pix/ttt/test'   # 輸入圖片目錄
output_folder = '/home/nini/pytorch-CycleGAN-and-pix2pix/resultpath_to_save_results' # 輸出圖片目錄
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 加載模型
model = torch.load(model_path, map_location=device)
model.eval()

# 圖像轉换器
transform = transforms.Compose([
    transforms.Resize((256, 256)),  # 轉换圖片大小到 256x256
    transforms.ToTensor(),          # 將圖片轉为 tensor
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # 正規化
])

def process_and_save_image(image_path):
    img = Image.open(image_path).convert('RGB')
    original_size = img.size  # 保存原始尺寸
    img_tensor = transform(img).unsqueeze(0).to(device)

    # 進行預測
    with torch.no_grad():
        output_tensor = model(img_tensor)
        output_tensor = (output_tensor * 0.5 + 0.5)  # 取消正規化
        output_image = transforms.ToPILImage()(output_tensor.squeeze(0))

    # 還原圖片大小
    output_image = output_image.resize(original_size)
    
    # 保存輸出圖片
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    output_image.save(output_folder)

# 確保輸出目錄存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 處理目錄下的每張圖片
for image_filename in os.listdir(input_folder):
    image_path = os.path.join(input_folder, image_filename)
    process_and_save_image(image_path)

print(f"所有圖片處理完畢，結果保存在 {output_folder}")