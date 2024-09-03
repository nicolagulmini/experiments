import model
import torch
import torchvision.transforms as transforms
import io
import PIL.Image as Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

class Wrap():
	def __init__(self):
		self.trainedClassifier = model.NeuralNetwork().to(device)
		self.trainedClassifier.load_state_dict(torch.load("fashionMnist_Classifier.pth", weights_only=True))

	def eval(self, raw_image):
		image = Image.open(io.BytesIO(raw_image))
		image = image.convert('L')
		transform = transforms.Compose(
		    [transforms.ToTensor()])

		#print('image shape:', transform(image).shape)

		image = transform(image).unsqueeze(0).to(device)  # Add batch dimension and move to device
		self.trainedClassifier.eval()

		# Predict the class
		with torch.no_grad():
		    output = self.trainedClassifier(image)
		    predicted_class = torch.argmax(output, dim=1).item()

		# Print the predicted class
		return {'Predicted class:': classes[predicted_class]}