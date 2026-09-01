import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
from torchvision import transforms

mtcnn = MTCNN(image_size=160, margin=0)
model = InceptionResnetV1(pretrained='vggface2').eval()


def cloak_face(full_img):
    """Takes a full PIL image, returns the full image with the face cloaked."""

    boxes, _ = mtcnn.detect(full_img)
    if boxes is None:
        return None

    box = boxes[0]
    x1, y1, x2, y2 = [int(b) for b in box]

    face_crop = full_img.crop((x1, y1, x2, y2))
    original_size = face_crop.size
    face_resized = face_crop.resize((160, 160), Image.LANCZOS)

    to_tensor = transforms.ToTensor()
    face_tensor = to_tensor(face_resized)
    face_tensor = (face_tensor - 0.5) / 0.5
    face_tensor = face_tensor.unsqueeze(0)

    with torch.no_grad():
        original_embedding = model(face_tensor)

    adv_face = face_tensor.clone()
    noise = torch.randn_like(adv_face) * 0.01
    adv_face = adv_face + noise
    adv_face.requires_grad = True

    epsilon = 0.05
    steps = 100
    optimizer = torch.optim.Adam([adv_face], lr=0.01)

    for step in range(steps):
        optimizer.zero_grad()
        current_embedding = model(adv_face)
        distance = torch.nn.functional.mse_loss(current_embedding, original_embedding)
        loss = -distance
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            perturbation = torch.clamp(adv_face - face_tensor, -epsilon, epsilon)
            adv_face.data = face_tensor + perturbation

    final_face_tensor = adv_face.squeeze(0).detach()
    to_pil = transforms.ToPILImage()
    cloaked_face_img = to_pil((final_face_tensor * 0.5 + 0.5).clamp(0, 1))
    cloaked_face_resized = cloaked_face_img.resize(original_size, Image.LANCZOS)

    final_full_img = full_img.copy()
    final_full_img.paste(cloaked_face_resized, (x1, y1))

    return final_full_img


if __name__ == '__main__':
    full_img = Image.open('test_photo.jpg').convert('RGB')
    result = cloak_face(full_img)
    result.save('cloaked_full_photo.jpg')
    print("Saved cloaked_full_photo.jpg")