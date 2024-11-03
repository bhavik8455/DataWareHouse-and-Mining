import numpy as np
import pandas as pd


def pagerank_calculate(adjacency_matrix,num_iteration,dumping_factor,num_nodes):
    pagerank = np.ones(num_nodes)/num_nodes
    print(f"Iteration 0 {pagerank}")

    pagerank_history = pd.DataFrame(index=[f"Page {chr(65+i)}" for i in range(num_nodes)],
                                    columns =[f"Iteration {i}" for i in range(num_iteration+1)] )
    pagerank_history.loc[:,'Iteration 0'] = np.round(pagerank,2)

    for iteration in range(num_iteration):
        new_pagerank = np.zeros(num_nodes)

        for i in range(num_nodes):
            incoming_link = np.where(adjacency_matrix[:,i]>0)[0]
            incoming_rank = sum((pagerank[j]/np.sum(adjacency_matrix[j])) for j in incoming_link if np.sum(adjacency_matrix[j])>0)

            new_pagerank[i] = (1-dumping_factor) + dumping_factor*(incoming_rank)

            incoming_str = "+".join(f"({np.round(pagerank[j],2)}/{np.round(np.sum(adjacency_matrix[j]),2)})"
                                    for j in incoming_link if np.sum(adjacency_matrix[j])>0)
            pagerank = new_pagerank

            
            print(f"PAGE{(65+i)} = (1-{dumping_factor}) + ({dumping_factor})*[{incoming_str}])")

        pagerank = new_pagerank
        pagerank_history.loc[:,f'Iteration {iteration+1}'] = np.round(pagerank,2)


    print("Final Pagerank")
    print(pagerank)

    print("Final Table")
    print(pagerank_history)
            

num_nodes = int(input("Enter the number of Nodes : "))

adjacency_matrix = []
print("Enter the matrix")
for _ in range(num_nodes):
    row = list(map(int,input().split()))
    adjacency_matrix.append(row)

adjacency_matrix = np.array(adjacency_matrix)

num_iteration = int(input("Enter the number of Iterations  : "))
dumping_factor = float(input("Enter the dumping factor between 0 and 1 : "))

pagerank_calculate(adjacency_matrix,num_iteration,dumping_factor,num_nodes)
