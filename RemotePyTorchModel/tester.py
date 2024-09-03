import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
import model
import torchvision.transforms as transforms
from PIL import Image

classes = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot')

# Define the device to use (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the image
image_path = "test.png"
image = Image.open(image_path).convert('L')

transform = transforms.Compose(
    [transforms.ToTensor()])

#print('image shape:', transform(image).shape)

# Preprocess the image
image = transform(image).unsqueeze(0).to(device)  # Add batch dimension and move to device
trainedClassifier = model.NeuralNetwork().to(device)
trainedClassifier.load_state_dict(torch.load("fashionMnist_Classifier.pth", weights_only=True))
trainedClassifier.eval()

# Predict the class
with torch.no_grad():
    output = trainedClassifier(image)
    predicted_class = torch.argmax(output, dim=1).item()

# Print the predicted class
print(f"Predicted Class: {classes[predicted_class]}")
