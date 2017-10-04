#coding:utf-8

userinfo = {'mxs': {'math':100, 'english':80, 'phyics':90},
            'ydl': {'math': 90, 'english':90, 'phyics':100}}

import recommendations
from recommendations import critics



def testGetUserInfo():
    print critics['Gene Seymour']
    print critics['Gene Seymour']['You, Me and Dupree']

def calDistance():
    dist = recommendations.sim_distance(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
    print dist
    dist = recommendations.sim_pearson(recommendations.critics,  'Lisa Rose', 'Gene Seymour')
    print dist

def getMatches(n):
    mathes = recommendations.topMatches(recommendations.critics, 'Toby', n)
    print mathes

def getRecommend():
    recds = recommendations.getRecommendations(recommendations.critics, 'Toby')
    print recds

def getTransform():
    movies = recommendations.transformPrefs(recommendations.critics)
    print movies

    results = {}
    results.setdefault('name', {})

    results['name']['age'] = 20
    print results

def getRecommendItem():
    itemsimr = recommendations.calculateSimilarItems(recommendations.critics)
    print itemsimr


def getTanimoto():
    a = ['a', 'b', 'c']
    b = ['a', 'b', 'd']
    tanimoto = recommendations.sim_tanimoto(a, b)
    print tanimoto

if __name__ == '__main__':
    testGetUserInfo()
    calDistance()
    n = 3
    getMatches(n)
    getRecommend()
    getTransform()
    getRecommendItem()
    getTanimoto()

