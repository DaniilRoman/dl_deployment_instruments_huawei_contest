from torch.tensor import Tensor
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor, Compose, Normalize, Resize


class ImageFolderCalibDataset:
    def __init__(self, root: str) -> None:
        self.dataset = ImageFolder(
            root=root,
            transform=Compose([
                Resize((300, 300)),
                ToTensor(),
                Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ])
        )

    def __len__(self) -> int:
        return len(self.dataset)

    def __getitem__(self, idx: int) -> Tensor:
        image, _ = self.dataset[idx]
        image = image[None, ...]  # add batch dimension
        return image
