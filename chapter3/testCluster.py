#coding:utf-8

import clusters

def getBlogData():
    rows = 1
    cols = 2
    blognames, words, data = clusters.readfile('blogdata.txt')

    print blognames[rows]
    print words[cols]
    print data[rows][cols]

    clust = clusters.hcluster(data)

    clusters.printclust(clust, blognames)


    # v1 = [1,2,3]
    #
    # v2 = [0,3,3]
    # a = clusters.pearson(v1, v2)
    # print a
    #
    # distances = {}
    # distances[(1,2)] = 3
    # print distances
    # distances[(2,1)] = 4
    # print distances
    # lowestpair = (1,2)
    # print lowestpair[0]

def getKCluster():
    #第一是博客名称，第二是单词本身，第三是词频
    blognames, words, data = clusters.readfile('blogdata.txt')
    # num = [data[i][0] for i in range(len(blognames))]
    # print num

    #data是list，每个元素是一篇博客中，对应单词频度
    #k为聚类的个数
    kclust = clusters.kcluster(data, k=10)
    print kclust

    # print len(data[0])
    # print len(data)
    # for row in data:
    #     print row
    #     print '\n'
    # ranges = [(min([row[i] for row in data]), max([row[i] for row in data]))
    #           for i in range(len(data[0]))]
    #
    # print type(ranges)
    # print ranges[1]
if __name__ == '__main__':
    # getBlogData()
    getKCluster()