import model
import torch

class Wrap():
	def __init__(self):
		self.network = model.SimpleNet()

	def eval(self, x1, x2, t1, t2):
		x = torch.tensor([[x1, x2]])
		target = torch.tensor([[t1, t2]])
		net = model.SimpleNet()
		result = net.train_and_ev(target, x)
		return result.tolist()