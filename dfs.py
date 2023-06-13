def dfs(graph, start, len, visited=None):
    try:
        if visited is None:  #проверка посещена ли вершина!
            visited = set()  #???
        visited.add(start)   
    except Exception as e:
        print ("Node is not valid" + start) #непон!
        raise e

    print (start)
    print("Length is ", len)

    for next in graph[start] - visited: #для посещения вершин
        dfs(graph, next, len+1, visited)

    return visited


graph = {'0': set(['2']),
         '1': set(['3']),
         '2': set(['0']),
         '3': set(['1'])}

length = 0

dfs(graph, '5', length)
