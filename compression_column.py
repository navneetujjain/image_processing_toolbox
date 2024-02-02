'''import numpy as np
import matplotlib.pyplot as plt
import imageio
import cv2

def compress_column(image):
    compressed_image = []
    for col in image.T:
        compressed_col = []
        for i in range(1, len(col), 2):
            x = (col[i] + col[i-1]) * 0.707
            compressed_col.append(x)
        compressed_image.append(compressed_col)
    return np.array(compressed_image).T

def expand_column(compressed_image):
    expanded_image = []
    for compressed_col in compressed_image.T:
        expanded_col = []
        for value in compressed_col:
            x = value * 0.707
            expanded_col.extend([x, x])
        expanded_image.append(expanded_col)
    return np.array(expanded_image).T

def column_compress_image(image_path):
    original_image = imageio.imread(image_path, pilmode='L')
    original_image = original_image / np.max(original_image)
    
    compressed_by_2 = compress_column(original_image)
    compressed_by_4 = compress_column(compressed_by_2)
    
    expanded_to_2 = expand_column(compressed_by_4)
    expanded_image = expand_column(expanded_to_2)
    
    plt.figure(figsize=(7, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(compressed_by_4, cmap='gray')
    plt.title('Compressed Image By 4')

    plt.subplot(1, 3, 3)
    plt.imshow(expanded_image, cmap='gray')
    plt.title('Recovered Image')

    plt.tight_layout()
    plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
import imageio
import cv2

def compress_column(image):
    compressed_image = []
    for col in image.T:
        compressed_col = []
        for i in range(1, len(col), 2):
            x = (col[i] + col[i-1]) * 0.707
            compressed_col.append(x)
        compressed_image.append(compressed_col)
    return np.array(compressed_image).T

def expand_column(compressed_image):
    expanded_image = []
    for compressed_col in compressed_image.T:
        expanded_col = []
        for value in compressed_col:
            x = value * 0.707
            expanded_col.extend([x, x])
        expanded_image.append(expanded_col)
    return np.array(expanded_image).T

def column_compress_image(image_path):
    original_image = imageio.imread(image_path, pilmode='L')
    original_image = original_image / np.max(original_image)
    
    compressed_by_2 = compress_column(original_image)
    compressed_by_4 = compress_column(compressed_by_2)
    
    expanded_to_2 = expand_column(compressed_by_4)
    expanded_image = expand_column(expanded_to_2)
    
    # Create a blank image with the same size as the original image
    blank_image = np.ones_like(original_image)
    
    # Set the compressed image on the blank image
    blank_image[:compressed_by_4.shape[0], :compressed_by_4.shape[1]] = compressed_by_4
    
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(blank_image, cmap='gray')
    plt.title('Compressed Image')

    plt.subplot(1, 3, 3)
    plt.imshow(expanded_image, cmap='gray')
    plt.title('Recovered Image')

    plt.tight_layout()
    plt.show()

# Example usage
#column_compress_image('path/to/your/image.jpg')
