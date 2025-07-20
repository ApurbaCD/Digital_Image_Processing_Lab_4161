import matplotlib.pyplot as plt

def main():
    img_path = '/home/apd/code/CSE_Lab/CSE_4_1/DIP/Image/image.png'
    img=plt.imread(img_path)
    img_4D=plt.imread(img_path)
    print(img.shape)
    
    #convert 4D image into 3D image 
    img_3D=img_4D[:,:,:3]
    print(img_3D.shape)
    
    #print some value of image
    
    print(img_3D[:10,:10,0])
    print(img_3D.max(),img_3D.min())
    
    #display loaded image 
    
    plt.imshow(img_3D)
    plt.show()
    plt.close()

if __name__ == '__main__':

    main()
