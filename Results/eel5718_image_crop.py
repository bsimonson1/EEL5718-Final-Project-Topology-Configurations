
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def main():
    images = [
            mpimg.imread('linear_topo.png'),
            mpimg.imread('mesh_topo.png'),
            mpimg.imread('tree_topo.png'), 
            mpimg.imread('ring_topo.png'), 
            mpimg.imread('hybrid_topo.png'), 
            mpimg.imread('star_topo.png')
            ]

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 8))
    axes = axes.flatten()
    for i, ax in enumerate(axes):
        ax.imshow(images[i])
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()