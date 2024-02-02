'''import numpy as np
import matplotlib.pyplot as plt
import imageio

def compress_row(image):
    compressed_image = []
    for row in image:
        compressed_row = []
        for i in range(1, len(row), 2):
            x = (row[i] + row[i-1]) * 0.707
            compressed_row.append(x)
        compressed_image.append(compressed_row)
    return np.array(compressed_image)

def expand_row(compressed_image):
    expanded_image = []
    for compressed_row in compressed_image:
        expanded_row = []
        for value in compressed_row:
            x = value * 0.707
            expanded_row.extend([x, x])
        expanded_image.append(expanded_row)
    return np.array(expanded_image)

def row_compress_image(image_path):
    original_image = imageio.imread(image_path, pilmode='L')
    original_image = original_image / np.max(original_image)
    
    compressed_by_2 = compress_row(original_image)
    compressed_by_2 = compressed_by_2 / np.max(compressed_by_2)
    
    compressed_by_4 = compress_row(compressed_by_2)
    
    expanded_to_2 = expand_row(compressed_by_4)
    expanded_image = expand_row(expanded_to_2)
    
    plt.figure(figsize=(7, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(compressed_by_4, cmap='gray')
    plt.title('Compressed Image by 4')

    plt.subplot(1, 3, 3)
    plt.imshow(expanded_image, cmap='gray')
    plt.title('Recovered Image')

    plt.tight_layout()
    plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
import imageio

def compress_row(image):
    compressed_image = []
    for row in image:
        compressed_row = []
        for i in range(1, len(row), 2):
            x = (row[i] + row[i-1]) * 0.707
            compressed_row.append(x)
        compressed_image.append(compressed_row)
    return np.array(compressed_image)

def expand_row(compressed_image):
    expanded_image = []
    for compressed_row in compressed_image:
        expanded_row = []
        for value in compressed_row:
            x = value * 0.707
            expanded_row.extend([x, x])
        expanded_image.append(expanded_row)
    return np.array(expanded_image)

def row_compress_image(image_path):
    original_image = imageio.imread(image_path, pilmode='L')
    original_image = original_image / np.max(original_image)
    
    compressed_by_2 = compress_row(original_image)
    compressed_by_2 = compressed_by_2 / np.max(compressed_by_2)
    
    compressed_by_4 = compress_row(compressed_by_2)
    
    expanded_to_2 = expand_row(compressed_by_4)
    expanded_image = expand_row(expanded_to_2)
    
    # Create a blank image with the same size as the original image
    blank_image = np.ones_like(original_image)
    
    # Set the compressed image on the blank image
    blank_image[:compressed_by_4.shape[0], :compressed_by_4.shape[1]] = compressed_by_4
    
    plt.figure(figsize=(7, 5))

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