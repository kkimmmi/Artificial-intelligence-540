from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    x = np.load(filename)
    u_mean = np.mean(x, axis=0)
    center = (x - u_mean)
    return center

def get_covariance(dataset):
    n = len(dataset)
    covariance = np.dot(np.transpose(dataset),dataset)/(n-1)
    return covariance

def get_eig(S, m):
    n = len(S)
    eig_val, eig_vect = eigh(S,subset_by_index = [n - m, n -1],
     eigvals_only=False) 
    eig_val = np.diag(np.sort(eig_val)[::-1])
    eig_vect = np.flip(eig_vect,1)
    return eig_val, eig_vect

def get_eig_prop(S, prop):
    sum_eig_val=sum(eigh(S, eigvals_only=True))
    eig_val, eig_vect = eigh(S, subset_by_value=[sum_eig_val*prop, np.inf])
    eig_val = np.diag(np.sort(eig_val)[::-1])
    eig_vect = np.flip(eig_vect,1)
    return eig_val, eig_vect

def project_image(image, U):
    proj = np.dot(U,np.dot(np.transpose(U),image))
    return proj

def display_image(orig, proj):
    # reshape them 
    orig = np.transpose(orig.reshape(32,32))
    proj = np.transpose(proj.reshape(32,32))

    f, (ax1,ax2) = plt.subplots(1, 2)
    
    ax1.set_title('Original') 
    ax2.set_title('Projection')
    
    a = ax1.imshow(orig, aspect='equal')
    b = ax2.imshow(proj, aspect='equal')

    #show picture and set colorbar
    f.colorbar(a,ax=ax1,shrink=0.75)
    f.colorbar(b,shrink=0.75)
    plt.show()
