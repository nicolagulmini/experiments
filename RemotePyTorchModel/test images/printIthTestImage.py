import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# same transformation as training set
transform = transforms.Compose(
    [transforms.ToTensor()])

# Create datasets for training & validation, download if necessary
training_set = torchvision.datasets.FashionMNIST('./data', train=True, transform=transform, download=True)
classes = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot')

i = 3

fig = plt.figure(frameon=False)
fig.set_size_inches(28/100, 28/100)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(training_set[i][0][0], aspect='auto', cmap='grey')
fig.savefig("test"+str(i)+".png", dpi=100)

print('class is:', classes[training_set[i][1]])