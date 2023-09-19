from typing import List

from scipy.spatial import Voronoi
import torch

def get_centroid(pts):
    n = pts.size(0)
    return torch.sum(pts[:,0])/n , torch.sum(pts[:,1])/n

def get_waypoints(map : torch.Tensor, N : int, range : float):
    free_idx = torch.argwhere(map==0)
    waypoints = free_idx[torch.randint(free_idx.size()[0],(map.size(0),N))]
    


if __name__ == "__main__":
    import torchvision
    #from cocomas import maps
    map_file = "cocomas/maps/empty.png"
    map = torchvision.io.read_image(map_file, torchvision.io.ImageReadMode.GRAY)/255
    get_waypoints(map, 10, 5)

