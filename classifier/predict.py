
import torch
import timm
from torchvision import transforms
from PIL import Image
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "oralcancer_vit.pth"

model = timm.create_model(
    'vit_base_patch16_224',
    pretrained=False,
    num_classes=2
)

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=torch.device('cpu'),
        weights_only=True
    )
)

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
     transforms.Normalize([0.5]*3, [0.5]*3)
])

def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image)
        pred = torch.argmax(output, dim=1).item()
        print(pred)
        return "Cancer" if pred == 0 else "Non Cancer"


