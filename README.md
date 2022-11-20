# image_processing

## The package image_processing is used to perform:
	
- Rgb2Yiq
- Yiq2Rgb
- RgbNegative
- YNegative
- Correlation
- Rgb2hsb
- Hsb2rgb
- Saturation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_processing

```bash
pip install image_processing
```

## Usage

```python
import matplotlib.pyplot as plt
from image_processing.processing import functions

image = functions.open("lena.jpg")
result = functions.correlation(image, 3, 3, "sobelV", 0, True)

plt.imshow(result)
plt.show()
```

## Author
Kelvin Brenand

## License
[MIT](https://choosealicense.com/licenses/mit/)
