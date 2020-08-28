import networkx as nx
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json


joining=500
percentage=0.2
topup=percentage*joining



def createTree(name):
    trees[name]=nx.DiGraph() 
    wallet[name]=0
    G=trees[name]
    G.add_node(name)


def addNodeEdge(u,v):
    all_trees=list(trees.keys())
    for x in all_trees:
        G=trees[x]
        nodes=list(G.nodes())
        if(u in nodes):
            G.add_node(v)
            G.add_edge(u,v)
    createTree(v)
    
def displayGraph():
    all_trees=list(trees.keys())
    for x in all_trees:
        G=trees[x]
        plt.title('Tree of user : '+x)
        pos = nx.spring_layout(G)
        f = plt.figure()
        nx.draw(G, pos, with_labels=True,node_color='yellow',arrows=True)
        file_name="Tree_"+x+".png"
        f.savefig(file_name,dpi=300)

def calculateWalletBalance():
    users=list(wallet.keys())
    for x in users:
        G=trees[x]
        nodes=list(G.nodes())
        levels=dict()
        paths=[]
        for y in nodes:
            if(x!=y):
                level_len=len(list(nx.shortest_path(G, source=x, target=y)))-2
                levels[y]=level_len
                paths.append(level_len)
        for z in paths:
                wallet[x]+=(topup)/2**z
    

def displayStats():
    print("")
    print("STATISTICS : ")
    print("Joining Fee =",joining)   
    print("Percentage = "+str(percentage*100))
    print("WALLET STATS :")
    print(wallet)

    global treesDict
    treesDict=dict()
    all_trees=list(trees.keys())
    for x in all_trees:
        G=trees[x]
        treesDict[x]=nx.to_dict_of_dicts(G)


def startTree(ref,usr,walletData,treeData):
    global wallet
    global trees
    wallet=walletData
    trees=treeData

    for x in (list(trees.keys())):
        G=nx.from_dict_of_dicts(treeData[x])
        trees[x]=G
    print(trees)
    addNodeEdge(ref,usr)
    calculateWalletBalance()
    displayStats()
    #displayGraph()
    return(treesDict,wallet)
    