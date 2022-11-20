# image_processing_KB

## The package image_processing_KB is used to perform:
	
- Rgb2Yiq
- Yiq2Rgb
- RgbNegative
- YNegative
- Correlation
- Rgb2hsb
- Hsb2rgb
- Saturation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_processing_KB

```bash
pip install image_processing_KB
```

## Usage

```python
import matplotlib.pyplot as plt
from image_processing_KB.processing import functions

image = functions.open("lena.jpg")
result = functions.correlation(image, 3, 3, "sobelV", 0, True)

plt.imshow(result)
plt.show()
```

## Author
Kelvin Brenand

## License
[MIT](https://choosealicense.com/licenses/mit/)
