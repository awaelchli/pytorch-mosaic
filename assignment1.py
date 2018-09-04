import numpy as np
import pickle
from PIL import Image
from sklearn.neighbors import NearestNeighbors
from base import Base


class Assignment1(Base):

    def __init__(self):
        super(Assignment1, self).__init__()
        self.data = pickle.load(open('./features/cifar10/raw.pkl', 'rb'))
        self.nn = self.get_model()
        self.nn.fit(self.data.reshape(len(self.data), -1))

    def get_model(self):
        """
        TO BE IMPLEMENTED BY STUDENT

        """
        return NearestNeighbors(n_neighbors=1, metric=self.distance)

    def get_patch(self, tile):
        _, inds = self.nn.kneighbors(tile.reshape(1, -1))
        patch = self.data[inds[0]]
        return patch

    def feature(self, x):
        """
        TO BE IMPLEMENTED BY STUDENT

        Compute the average color across the patch x.

        :param x: The image patch of size 32 x 32 x 3 flattened as a long vector of size 1 x 3072
        :return: The average pixel color
        """

        return np.mean(x.reshape(32, 32, 3), axis=(0, 1))

    def distance(self, x, y):
        """
        TO BE IMPLEMENTED BY STUDENT

        """
        return np.linalg.norm(self.feature(x) - self.feature(y))


if __name__ == '__main__':
    """ 
    Assignment 1a - Average Patch Features 
    Assignment 1b - Nearest Neighbor Search
    
    """

    # The program will start execution here
    # Change the filename to load your favourite picture
    file = './images/lion.jpg'

    img = Image.open(file).convert('RGB')
    target_image = np.array(img) / 255

    # This will execute the Mosaicking algorithm of Assignment 1
    main = Assignment1()
    output_image = main.mosaic(target_image)

    # Saving the image inside in project root folder
    output_image *= 255
    im = Image.fromarray(output_image.astype('uint8'))
    im.save('mosaic.png')