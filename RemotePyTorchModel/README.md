## Server-side PyTorch fashion-MNIST classifier

I trained and saved a very simple PyTorch classifier, used by a Fastapi API that receives POST requests and sends back the predictions over the received images.
It has a cache to save the most requested predictions, to avoid querying the model and save time.
