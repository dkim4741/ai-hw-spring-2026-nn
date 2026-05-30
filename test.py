import torch
import torchvision
import torchvision.transforms as transforms
from model import SimpleMLP

def test():
    # Convert images to tensors
    transform = transforms.ToTensor()

    # Load data and model weights directly
    test_dataset = torchvision.datasets.MNIST(
        root="./data",
        train=False,
        download=True,
        transform=transform
    )

    test_loader = torch.utils.data.DataLoader(
        dataset=test_dataset,
        batch_size=64,
        shuffle=False
    )

    # Create model
    model = SimpleMLP()

    # Load trained weights
    model.load_state_dict(torch.load("mnist_mlp.pth"))
    model.eval()

    correct, total = 0, 0

    # Evaluation loop without gradients
    with torch.no_grad():
        for images, labels in test_loader:
            # Forward pass
            outputs = model(images)

            # predicted = outputs.argmax(dim=1)
            correct += (outputs.argmax(dim=1) == labels).sum().item()
            total += labels.size(0)

    print(f"[Result] Accuracy: {100 * correct / total:.2f}%")

if __name__ == "__main__":
    test()