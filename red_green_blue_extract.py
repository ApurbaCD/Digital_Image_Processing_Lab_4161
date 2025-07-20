import matplotlib.pyplot as plt 

def main():
    img_path1='/home/apd/code/CSE_Lab/CSE_4_1/DIP/Image/image6.jpg'
    img_path2='/home/apd/code/CSE_Lab/CSE_4_1/DIP/Image/image5.jpg'
    
    img1=plt.imread(img_path1)
    img2=plt.imread(img_path2)
    
    #if img1.shape[2] == 4:
    #    img = img[:, :, :3]
    
    #if img2.shape[2] == 4:
     #   img = img[:, :, :3]
        
    #if img.shape[2] == 4:
        #img = img[:, :, :3]
        
    print("image dtype",img1.dtype)
    print("image dtype",img2.dtype)
    
    print(img1.shape)
    print(img2.shape)
    
    #Extract channels for colorful image
    
    red_channel=img1[:,:,0]
    green_channel=img1[:,:,1]
    blue_channel=img1[:,:,2]
    
    plt.figure(figsize=(16,8))
    
    plt.subplot(2,4,1)
    plt.imshow(img1)
    plt.title('Original Image')
    plt.axis('off')
    
    
    plt.subplot(2,4,2)
    plt.imshow(red_channel,cmap='Reds')
    plt.title('Red channel')
    plt.axis('off')
    
    plt.subplot(2,4,3)
    plt.imshow(green_channel,cmap='Greens')
    plt.title('Green channel')
    plt.axis('off')
    
    plt.subplot(2,4,4)
    plt.imshow(blue_channel,cmap='Blues')
    plt.title('Blue channel')
    plt.axis('off')
    
    
    #showing gray image and extract in the plt.imshow()
    
    plt.subplot(2,4,5)
    plt.imshow(img2)
    plt.title('Gray Image')
    plt.axis('off')
    
    plt.subplot(2,4,6)
    plt.imshow(img2[:,:],cmap='Reds')
    plt.title('Red channel')
    plt.axis('off')
    
    plt.subplot(2,4,7)
    plt.imshow(img2[:,:],cmap='Greens')
    plt.title('Green channel')
    plt.axis('off')
    
    plt.subplot(2,4,8)
    plt.imshow(img2[:,:],cmap='Blues')
    plt.title('Blue channel')
    plt.axis('off')
    
 
    plt.show()
    plt.close()
    
    
    
if __name__=='__main__':
    main()
    
    
