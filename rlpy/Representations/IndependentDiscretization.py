"""Independent Discretization"""

from .Representation import Representation
import numpy as np

__copyright__ = "Copyright 2013, RLPy http://www.acl.mit.edu/RLPy"
__credits__ = ["Alborz Geramifard", "Robert H. Klein", "Christoph Dann",
               "William Dabney", "Jonathan P. How"]
__license__ = "BSD 3-Clause"
__author__ = "Alborz Geramifard"


class IndependentDiscretization(Representation):

    def __init__(self, domain, discretization=20):
        self.setBinsPerDimension(domain, discretization)
        self.features_num = int(sum(self.bins_per_dim))
        self.maxFeatureIDperDimension = np.cumsum(self.bins_per_dim) - 1
        super(
            IndependentDiscretization,
            self).__init__(
            domain,
            discretization)

    def phi_nonTerminal(self, s):
        F_s = np.zeros(
            self.features_num,
            'bool')
        F_s[self.activeInitialFeatures(s)] = 1
        return F_s

    def getDimNumber(self, f):
        # Returns the dimension number corresponding to this feature
        dim = np.searchsorted(self.maxFeatureIDperDimension, f)
        return dim

    def getFeatureName(self, id):
        if hasattr(self.domain, 'DimNames'):
            dim = np.searchsorted(self.maxFeatureIDperDimension, id)
            # Find the index of the feature in the corresponding dimension
            index_in_dim = id
            if dim != 0:
                index_in_dim = id - self.maxFeatureIDperDimension[dim - 1]
            print self.domain.DimNames[dim]
            f_name = self.domain.DimNames[dim] + '=' + str(index_in_dim)

    def featureType(self):
        return bool