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
            expanded_row.extend([value, value])
        expanded_image.append(expanded_row)
    return np.array(expanded_image)

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

def process_image(image_path):
    original_image = imageio.imread(image_path, pilmode='L')
    original_image = original_image / np.max(original_image)
    
    compressed_by_2 = compress_column(original_image)
    compressed_by_2 = compress_row(compressed_by_2)
    
    expanded_image = expand_row(compressed_by_2)
    expanded_image = expand_column(expanded_image)
    
    plt.figure(figsize=(7, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(compressed_by_2, cmap='gray')
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
            expanded_row.extend([value, value])
        expanded_image.append(expanded_row)
    return np.array(expanded_image)

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

def process_image(image_path):
    original_image = imageio.imread(image_path, pilmode='L')
    original_image = original_image / np.max(original_image)
    
    compressed_by_2 = compress_column(original_image)
    compressed_by_2 = compress_row(compressed_by_2)
    
    expanded_image = expand_row(compressed_by_2)
    expanded_image = expand_column(expanded_image)
    
    # Create a blank image with the same size as the original image
    blank_image = np.ones_like(original_image)
    
    # Set the compressed image on the blank image
    blank_image[:compressed_by_2.shape[0], :compressed_by_2.shape[1]] = compressed_by_2
    
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
