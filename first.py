import matplotlib.pyplot as plt

def main():
    img_path = '/home/apd/code/CSE_Lab/CSE_4_1/DIP/Image/image1.png'
    img = plt.imread(img_path)

    print("Image dtype:", img.dtype)
    print("Image shape:", img.shape)
    print("Image max value:", img.max())
    print("Image min value:", img.min())

    #Remove alpha channel if present
    if img.shape[2] == 4:
        img = img[:, :, :3]

    img_inverted = img.max() - img
    print("Inverted image shape:", img_inverted.shape)

    plt.imshow(img_inverted)
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()

